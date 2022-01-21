

# DNAseq SOP 文档


# 一、文档说明
## 1.1 关于手册 
该文档旨在进行曙光云 DNAseq（包括WGS 和捕获测序产品）流程使用方法介绍。 

## 1.2 面向的使用者
武汉菲沙医学临床生信分析人员。

## 1.3 信息反馈
如果对本文档有任何意见和建议，请联系：zhangbo@frasergen.com。

# 二、模块介绍
该模块主要用于DNAseq 产品方面的生信分析，包括主脚本（质控、比对、统计等）和后续分析模板等多个模块。
|模块名称|脚本名称|模块内容|
|--|:--:|--|
|主脚本|<$name.sh>|包括原始下机数据质控、比对处理、统计等小模块|
|遗传小突变脚本|<VQSR.sh>|利用GATKVQSR软件进行call 变异，最终进行结果整合|
||<freebayes.sh>|利用freebayes 软件进行call 变异，最终进行结果整合|
|无对照肿瘤小突变脚本|<$name_tumoronly_Mutect2.sh >|利用GATKMutect2软件进行call 变异，最终进行结果整合|
||<$name_tumoronly_mutect.sh >|利用GATKMutect软件进行call 变异，最终进行结果整合|
|有对照肿瘤小突变脚本|T_vs_N.mutect2.sh|利用GATKMutect2软件进行call 变异|
||||

# 三、模块使用
## 3.1 模块信息
```
模块名称：exomeseq-pip.v8.sh exomeseq.cfg8
版本号：v8 
曙光云集群路径：/public/frasergen/MED/project/zhangbo/benchmark/aitest
```
## 3.2 模块使用
```
bash exomeseq-pip.v8.sh exomeseq.cfg8
```
## 3.3 cfg参数
|参数|参数说明|
|--|--|
|tumors="ZWT"|肿瘤样本名|
|project=AItumorExonT1|项目名称|
|lanes='ZWT'|样本名|
|workdir=|工作目录|
|data=${workdir}/fastq|输入文件，其中包含sample.info 文本，分为两列：第一列为样本名，第二列为fq1,fq2的绝对路径，逗号分隔|
|output=${workdir}/out|输出文件夹路径|
|pair="pair"|默认值|
|tumorvsnormal="202111:2021NC"|肿瘤配对样本名，”肿瘤样本名：对照样本名“|
|normals="AM67-1"|对照样本名，暂无用处|
|germline="yes"|是否跑遗传流程，默认为是|
|somatic="no"|是否跑成对肿瘤流程，默认为**否**|
|tumoronly="yes"|是否跑无对照流程，对于肿瘤样本，默认为是|
|analysistype="panel"|"wgs" "panel" "wes" 对应不同的bed文件|
|bedtype="panel"|"bed"(对应安捷伦v6) "IDTv1_bed" "wgs" "panel|
|platform="BGI|platform "illumina" "BGI"|
|current_ref="hg19"|current_ref "hg19" "hg38"|
|disease_type="solidtumor"|dieseas/cancer_type: "leukemia" "liver" "kidney" "solidtumor"|
|sample_type|sample_type: "FFPE" "other"，暂无特殊要求|
|gender="male"|暂无|

> 注意: 运行脚本前，注意修改对应的参数，特别注意：platform 和 bedtype

## 3.4 测试数据
### 3.4.1 测试路径
```
cd /public/frasergen/MED/project/zhangbo/benchmark/aitest
bash exomeseq-pip.v8.sh  exomeseq.cfg8
cd out/code/
bash Running_V3.slurm
```
![image](https://user-images.githubusercontent.com/12706146/150285642-aa8bbc89-ad5c-4f8e-9bbf-355cc6cf9652.png)
> 注意检查 打印出来的内容
### 3.4.2 测试结果
```
```
---
# 四、升级日志

