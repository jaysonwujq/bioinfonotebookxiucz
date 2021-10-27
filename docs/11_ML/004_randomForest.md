随机森林：
基于决策树
有监督
随机有放回
作用
样本分类：非线性分类器
回归分析
准则衡量特征的贡献程度
D3算法（J. Ross Quinlan于1986年提出），采用信息增益最大的特征；
C4.5算法（J. Ross Quinlan于1993年提出）采用信息增益比选择特征；
CART算法（Breiman等人于1984年提出）利用基尼指数最小化准则进行特征选择。
依次对对象进行分类。最后将各决策树的分类结果汇总，所有预测类别中的众数类别即为随机森林所预测的该对象的类别，分类准确率提升。

1. 集成学习(ensemble methods)
集成学习通过建立几个模型组合的来解决单一预测问题。它的工作原理是生成多个学习器模型，各自独立地学习和作出预测。这些预测最后结合成单预测，因此优于任何一个单分类的做出预测。
根据个体学习器的生成方式，目前大致可分为两大类：
a)个体学习器间存在强依赖关系、必须串行生成的序列化方法，代表是Boosting；
b)个体学习器间不存在强依赖关系、可同时生成的并行化方法，代表是Bagging和“随机森林”。

2. Bagging
Bootstrap sampling：自助采样法，简言之就是随机有放回的抽取，有一部分样本会多次出现，而另一部分样本不出现。初始数据集中约有1/3的样本未出现在采样数据集中。
Bagging: 基于自助采样法(bootstrap sampling)，将所有待训练数据放进一个黑匣子中，然后从这个bag中随机且有放回地抽一部分数据出来用于训练一个基学习器（base estimator），再将这些基学习器结合。

3. 决策树(Decision Tree)
决策树是一种基本的分类器，主要工作就是选取特征对数据集进行划分，最后把数据贴上两类不同的标签。构建好的决策树呈树形结构，可以认为是if-then规则的集合，主要优点是模型具有可读性，分类速度快。常见的决策树算法有C4.5、ID3和CART(随机森林使用)：（具体细节见附录一）
ID3 ：信息增益 最大的准则
C4.5 ：信息增益比 最大的准则
CART：回归树（ 平方误差 最小的准则）；分类树（基尼系数 最小的准则）

图片

决策树学习采用的是自顶向下的递归方法, 其基本思想是以信息熵为度量构造一棵熵值下降最快的树,到叶子节点处的熵值为零, 此时每个叶节点中的实例都属于同一类。

4. Random Forest
扰动：随机森林对Bagging只做了小改动，基学习器的多样性不仅来自样本扰动（对初始训练集有放回的采样），还有属性扰动（对样本属性的随机无放回的抽样）。
bagging + decision trees，我们得到了随机森林。将决策树作为base estimator，然后采用bagging技术训练一大堆小决策树，最后将这些小决策树组合起来，这样就得到了一片森林(随机森林)。
预测：在对预测输出进行结合时，通常对分类任务使用简单投票法，对回归任务使用简单平均法；若分类预测时两个类收到同样票数，则随机选一个或进一步考察学习器投票的置信度来确定最终胜者。

图片

5. oob error
初始数据集每次约有1/3的样本不会出现在采样数据集中，当然也就没有参加决策树的建立。我们把这1/3的数据称为袋外数据oob（out of bag）,它可以用于取代测试集误差估计方法。（第四部分有详细解释）

6. 过拟合
是指学习时选择的模型所包含的参数过多，以致于出现这一模型对已知数据预测地很好，但对未知数据预测得很差的现象。

7. 剪枝
为了尽可能正确分类训练样本，结点划分过程将不断重复，有时会造成决策树分支过多，这时候通过主动去掉一些分支来降低过拟合的风险；包括预剪枝和后剪枝。

https://mp.weixin.qq.com/s/58VAF03uO3nBPfp7eboqUA

随机森林工作过程可概括如下：
（1）假设训练集中共有N个对象、M个变量，从训练集中随机有放回地抽取N个对象构建决策树；
（2）在每一个节点随机抽取m<M个变量，将其作为分割该节点的候选变量，每一个节点处的变量数应一致；
（3）完整生成所有决策树，无需剪枝（最小节点为1）；
（4）重复（1）-（3）过程，获得大量决策树；终端节点的所属类别由节点对应的众数类别决定；
（5）对于新的观测点，用所有的树对其进行分类，其类别由多数决定原则生成。
```

install.packages("randomForest")

data(iris)
> head(iris)
  Sepal.Length Sepal.Width Petal.Length Petal.Width Species
1          5.1         3.5          1.4         0.2  setosa
2          4.9         3.0          1.4         0.2  setosa
3          4.7         3.2          1.3         0.2  setosa
4          4.6         3.1          1.5         0.2  setosa
5          5.0         3.6          1.4         0.2  setosa
6          5.4         3.9          1.7         0.4  setosa


set.seed(315)
iris.rf = randomForest(Species ~ ., data=iris, importance=TRUE, proximity=TRUE)
#显示结果，默认使用500个树，获得两个变量分离样品，错误评估矩阵
> print(iris.rf)

Call:
 randomForest(formula = Species ~ ., data = iris, importance = TRUE,      proximity = TRUE)
               Type of random forest: classification
                     Number of trees: 500
No. of variables tried at each split: 2

        OOB estimate of  error rate: 4%
Confusion matrix:
           setosa versicolor virginica class.error
setosa         50          0         0        0.00
versicolor      0         47         3        0.06
virginica       0          3        47        0.06

```
随机森林的构建过程
数据的随机性选取
待选特征的随机选取。

https://cloud.tencent.com/developer/article/1589177
