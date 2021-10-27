示例文件“otu_table.txt”为来自16S测序所获得的细菌OTUs丰度表格，共计120个样本，其中60个来自环境c（c组），60个来自环境h（h组）。
接下来使用该数据：

（1）任一OTUs的丰度都很难作为判别两种不同环境的标准，因此接下来综合考虑所有OTUs的丰度并进行建模，目的是找到能够稳定区分两种环境的代表性OTUs组合（作为生物标志物）；

（2）通过代表性OTUs的丰度构建预测模型，即仅通过这些OTUs的丰度就能够判断样本分类。

```
#读取 OTUs 丰度表
otu <- read.table('otu_table.txt', sep = '\t', row.names = 1, header = TRUE, fill = TRUE)
 
#过滤低丰度 OTUs 类群，它们对分类贡献度低，且影响计算效率
#120 个样本，就按 OTUs 丰度的行和不小于 120 为准吧
otu <- otu[which(rowSums(otu) >= 120), ]
 
#合并分组，得到能够被 randomForest 识别计算的格式
group <- read.table('group.txt', sep = '\t', row.names = 1, header = TRUE, fill = TRUE)
otu <- data.frame(t(otu))
otu_group <- cbind(otu, group)
otu_group$groups <- factor(otu_group$groups)

#将总数据集分为训练集（占 70%）和测试集（占 30%）
set.seed(123)
select_train <- sample(120, 120*0.7)
otu_train <- otu_group[select_train, ]
otu_test <- otu_group[-select_train, ]

#randomForest 包的随机森林
library(randomForest)
 
#随机森林计算（默认生成 500 棵决策树），详情 ?randomForest
set.seed(123)
otu_train.forest <- randomForest(groups ~ ., data = otu_train, importance = TRUE)
otu_train.forest
 
plot(margin(otu_train.forest, otu_train$groups), main = '观测值被判断正确的概率图')
```
