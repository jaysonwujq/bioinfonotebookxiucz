#### Removing adapters
接头的种类：
https://teichlab.github.io/scg_lib_structs/methods_html/Illumina.html


http://tucf-genomics.tufts.edu/home/faq

https://shengxin.ren/article/87

https://www.jianshu.com/p/3164dca8bd61
https://www.jianshu.com/p/4817bca51cf4


https://zhuanlan.zhihu.com/p/35278810

####  Demultiplexing

```
#adapter解析；reads根据adapter不同输出到不同的文件
cutadapt -a one=TATA -a two=GCGC -o trimmed-{name}.fastq.gz input.fastq.gz
#result files: demulti-one.fastq.gz, demulti-two.fastq.gz and demulti-unknown.fastq.gz

cutadapt -a file:barcodes.fasta --no-trim --untrimmed-o untrimmed.fastq.gz -o trimmed-{name}.fastq.gz input.fastq.gz
#result files: trimmed-first.1.fastq.gz, trimmed-second.1.fastq.gz, trimmed-unknown.1.fastq.gz and trimmed-first.2.fastq.gz, trimmed-second.2.fastq.gz, trimmed-unknown.2.fastq.gz
```

https://www.jianshu.com/p/4ee2f4d2292f


[toc]

https://www.illumina.com/documents/products/datasheets/datasheet_sequencing_multiplex.pdf


1、adapter是一段短的序列已知的核酸链，用于链接序列未知的目标测序片段。

2、barcode，也称为index，是一段很短的寡居核酸链，用于在多个样品混合测序时，标记不同的样品。

3、insert是用于测序的目标片段，因为是包括在两个adapter之间，所以被称为“插入”片段。

一个常见测序片段类似与adapter--barcode--insert--adapter。测序开始时前几个碱基无法测得，第一个adapter在数据输出时被去除；由于测序仪读长限制，第二个adapter通常无法测得。所以，经常得到类似 barcode--部分insert的read。最后，把barcode去除，只保留测度insert的片段，这个操作的术语是demultiplexing。但是有时候测序时会测穿，也就是说会得到barcode--insert的read--部分adapter，那么这里就包含了接头了，这里的接头也就是大家经常说去接头要去除的部分。

## cutadpat
![image](https://github.com/xiucz/pics/blob/master/adapter.png?raw=true)
```
adapt1(5'端接头):AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT

adapt1_REV:AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT

adapt2(3'端接头):GATCGGAAGAGCACACGTCTGAACTCCAGTCACNNNNNNATCTCGTATGCCGTCTTCTGCTTG

NNNNNN：barcode
```


```
cutadapt -a adapt2 -A adapt1_REV -m 20 --pair-filter=both -o out_fq1 -p out_fq2 fq1 fq2

-a：左端reads的接头，去除read1的3‘接头序列。

-A：右端reads的接头，去除read2的3’接头序列。注意右端出现的接头是因为侧穿了，所以他的接头序列是左端reads的接头的反向互补序列

-m：表示去除接头后如果read长度小于这个m值就不要了

--pair-filter：采用双末端模式来去除接头，保持两端数据匹配

--length_tag 在输出文件中给出 序列的length 信息

```

maijinuo完整命令如下：
```
cutadapt -m 80 -q10,10 -o sample.clean_R1.fq.gz -p sample.clean_R2.fq.gz -u 9 -U 9
-a ${barcode_reverse}AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC \
-A ${barcode_reverse}AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT \
sample_R1.fq.gz sample_R2.fq.gz

-m:Throw away processed reads shorter than N bases
-q:along with --quality-base
${barcode_reverse}：防污染接头
-a:3’端通用引物
-A:5’端通用引物
sample_R1.fq.gz sample_R2.fq.gz：输入的原始数据reads1和reads2
sample.clean_R1.fq.gz  sample.clean_R2.fq.gz：过滤后的reads1和reads2


3’端通用引物 AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC GCTGATCT ATCGCGTATGCAGTCGTCTGCTTGAA

AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT
>>>>>
AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT

```

#### Ref_Info
https://www.cnblogs.com/xudongliang/p/6404958.html


**模式:**

anchor: adapters锚定在reads开始处或末尾处

+ Anchored 5’ adapters：
+ Regular 3’ adapters:
+ Anchored 5’ adapters:
+ Regular 3’ adapters 
+ Linked adapters (combined 5’ and 3’ adapter):
+

## 预测接头
https://link.zhihu.com/?target=https%3A//www.ebi.ac.uk/research/enright/software/kraken
```
minion search-adapter -i SRR.fastq

```

https://note.youdao.com/s/Z0FkXtSB