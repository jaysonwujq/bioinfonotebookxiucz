<!-- TOC -->

- [1. pre](#1-pre)
- [2. Call](#2-call)
    - [2.1.](#21)
    - [2.2. Active Regions](#22-active-regions)
- [3. PON](#3-pon)
- [4. MuTect2 filters](#4-mutect2-filters)
    - [4.1.](#41)
    - [4.2. FILTER and FORMAT](#42-filter-and-format)
    - [4.3.](#43)
        - [4.3.1. mutect2的AF（AF calculation in Mutect2）](#431-mutect2的afaf-calculation-in-mutect2)
    - [4.4. Contamination 样本间污染评估](#44-contamination-样本间污染评估)
        - [4.4.1. ContEst（gatk3）](#441-contestgatk3)
        - [4.4.2.](#442)
            - [4.4.2.1. getpileupsummaries](#4421-getpileupsummaries)
- [5. This produces a six-column table as shown. The `alt_count` is the count of reads that support the ALT allele in the germline resource. The `allele_frequency` corresponds to that given in the germline resource. Counts for `other_alt_count` refer to reads that support all other alleles.](#5-this-produces-a-six-column-table-as-shown-the alt_count is-the-count-of-reads-that-support-the-alt-allele-in-the-germline-resource-the allele_frequency corresponds-to-that-given-in-the-germline-resource-counts-for other_alt_count refer-to-reads-that-support-all-other-alleles)
    - [5.1. Mutect2 bamout reports fewer reads than VCF AD](#51-mutect2-bamout-reports-fewer-reads-than-vcf-ad)
            - [5.1.0.2. Ref_Info](#5102-ref_info)
    - [5.2. 方法](#52-方法)
        - [5.2.1. 定义活跃区域](#521-定义活跃区域)
        - [5.2.2. Assembling Haplotypes](#522-assembling-haplotypes)
        - [5.2.3. Somatic Genotyping](#523-somatic-genotyping)
        - [5.2.4. 过滤](#524-过滤)
            - [5.2.4.1.](#5241)
    - [5.3. Results](#53-results)
        - [5.3.1. DREAM Challenge](#531-dream-challenge)
        - [5.3.2. Normal-Normal Calls](#532-normal-normal-calls)
        - [5.3.3. Normal mixtures](#533-normal-mixtures)
        - [5.3.4. workflow](#534-workflow)
        - [5.3.5. 参数理解](#535-参数理解)
        - [5.3.6. 参数理解](#536-参数理解)
        - [5.3.7. strand bias](#537-strand-bias)
    - [5.4. source-code](#54-source-code)
    - [5.5. 算法](#55-算法)
    - [5.6. 教程](#56-教程)

<!-- /TOC -->


# 1. pre
![](./pics/202101115.png)
![](./pics/202101113.png)
![](./pics/202101114.png)

# 2. Call
The thresholds used by MuTect2 to consider a variant as being **real and somatic** (leading to the annotation “PASS”)：
+ are by default TLOD > 6.3 and NLOD > 2.2. 
+ For dbSNP variants, a higher NLOD threshold of 5.5 is used
+ For dbSNP and COSMIC database variants, NLOD > 2.2.  

## 2.1.  
与HaplotypeCaller一样，Mutect2通过在active region中对单倍型（决定同一性状的紧密连锁的基因构成的基因型）进行局部重新组装来判断SNV和InDel。 也就是说，当Mutect2遇到显示体细胞变异迹象的active region时，它会丢弃现有的映射信息，并完全重新组装该区域中的reads，以生成候选变异单倍型。 像HaplotypeCaller一样，Mutect2然后通过Pair-HMM算法将每个reads与每个单倍型对齐，以获得似然矩阵。 最后，它应用贝叶斯体细胞似然模型来获得体细胞变异与测序错误的对数比。

## 2.2. Active Regions
+ Modified	sta*s*c	threshold	for	soma*c	scenario	uses	LOD	≥	4.0	in	favor	of	
the	reference	model		
+ Reads	differentially	filtered:	
  + Tumor	is	strict:	MAPQ	≥	Q20;	discard	discrepant	overlapping	reads	
  + Normal	is	permissive:	MAPQ	≥	Q0;	keep	alternate	read	from	discrepant	
overlapping	reads	

> 怎么执行：https://gatk.broadinstitute.org/hc/en-us/community/posts/360065192491-mutect2-realignment

# 3. PON

+ Then, variants identified by MuTect2 in at least two normal samples were compiled together into one PoN VCF file.

# 4. MuTect2 filters
## 4.1.  

## 4.2. FILTER and FORMAT
Filter | Threshold | Key | Explanation | Version
--- | ---| --- | --- | ---
t_lod | | | | 
clustered_events | max-events-in-region | ECNT | mutations sharing an assembly region |
duplicate_evidence | unique-alt-read-count | - | unique insert start/end pairs of alt reads |
multiallelic | max-alt-alleles-count | - | passing alt alleles at a site | 
base_quality | min-median-base-quality | MBQ | median base quality of alt reads |
mapping quality | min-median-mapping-quality | MMQ | median mapping quality of alt reads | 
fragment length | max-median-fragment-length-difference | - | difference of alt and ref reads’ median fragment lengths |
read position | min-median-read-position |  | median distance of alt mutations from end of read  |
panel of normals | panel-of-normals |  | presence in panel of normals | 


---
> base_quality
+ base_quality(alt的碱基质量值的中位数)标签出现在了filter列，它在call的时候估算的参数为MBQ=0，而我们设置的min-median-base-quality参数为20，因为0<20,所以base_quality的标签出现在了tag里边。
> clustered_events
+ 活动区域发生多次突变，且突变位点距离在3bp及以上。(为什么大于3bp呢？因为2个的话很有可能是可以合并的同一个。)
+ max-events-in-region is the maximum allowable number of called variants co-occurring in a single assembly region. If the number of called variants exceeds this they will all be filtered.
+ Variants coming from an assembly region with more than this many events are filtered.
> germline_risk
+ 该位点是germline event的最大后验概率， 根据模型计算P_GERMLINE值，大于设定值就会添加germline_risk的标签。
+ Maximum posterior probability that an allele is a germline variant.
+ max-germline-posterior is the maximum posterior probability, as determined by the above germline probability model, that a variant is a germline event.
> artifact_in_normal
+ 当tumor和control成对call的时候，会对control组的normal样本单独设置对数比阈值，该阈值越高，过滤标准越严格，因为认为normal全部是假阳性，所以会设置较低的LOD值。
+ normal-artifact-lod is the maximum acceptable likelihood of an allele in the normal by the somatic likelihoods model. This is different from the normal likelihood that goes into the germline model, which makes a diploid assumption. Here we compute the normal likelihood as if it were a tumor in order to detect artifacts.
> strict_strand
+ 表示alt等位基因在两个方向均为显示（Evidence for alt allele is not represented in both directions）
> strand_artifact
+ 链偏移，表示仅来自于一条read方向的alt等位基因（Evidence for alt allele comes from one read direction only）
+ max-strand-artifact-probability is the posterior probability of a strand artifact, as determined by the model described above, required to apply the strand artifact filter.
+ 链偏好性的后验概率，根据计算的SA_POST_PROB，大于设定值则过滤；还有第二层补充条件；
+ This is necessary but not sufficient – we also require the estimated max a posteriori allele fraction to be less than min-strand-artifact-allele-fraction.The second condition prevents filtering real variants that also have significant strand bias, i.e. a true variant that also has some artifactual reads.
+ 如果链偏好性的最大后验概率比SA_MAP_AF（MAP estimates of allele fraction given
变异频率的最大后验概率）值小，会保留，以防将真阳性位点加上strand_artifact标签。
+ Filter a variant if the probability of strand artifact exceeds this number
```
Generally, we find the likelihood of strand bias is 1/10,000. And for example in your first PASS variant example with SB=8,17,5,0: 5,0 or 0,5 has a 1/16 likelihood of occurring, which is much more probable than the 1/10,000.
```
> mapping_quality
> fragment_length
+ tumor-normal成对call才会出现的
> read_position
+ 位点到read末尾的最近读取端的最小中值长度。DENELS的位置是由读数末尾最远的一端测量的。
> weak_evidence：表示突变为达到阈值（Mutation does not meet likelihood threshold），低于 -emit-lod 阈值
> t_lod
+ tumor-lod is the minimum likelihood of an allele as determined by the somatic likelihoods model required to pass.似然模型中认为该点是体细胞变异的最小似然比，默认是5.3,若小于5.3则添加tlod标签。
> orientation bias
+ OxoG artifacts stem from oxidation of guanine to 8-oxoguanine, which results in G to T transversions. If samples were derived from histological slides, then consider the FFPE (formalin-fixed paraffin-embedded) artifact. FFPE artifacts stem from formaldehyde deamination of cytosines, which results in C to T transitions.（doi：10.1093/nar/gks1443）
+ 鸟嘌呤（guanine）氧化成8-氧代鸟嘌呤（8-oxoguanine）是在基因组文库制备过程中，最常见的加接头前的伪影（artifacts）之一；形成的主要原因，是由于样品中的热量、剪切和金属污染共同产生（doi：10.1093/nar/gks1443）。
8-氧代鸟嘌呤碱基（8-oxoguanine）可与胞嘧啶（cytosine）或腺嘌呤（adenine）配对，最终导致 PCR 扩增过程中 G→T 的碱基颠换。 当模板链上的G被氧化时，将会使得A比C更具有亲和力。因此，在PCR过程中，reads1中将表现为G>T的替换，而在reads2中引入C>A的替换。
+ 源码：https://github.com/broadinstitute/gatk-protected/blob/master/src/main/java/org/broadinstitute/hellbender/tools/exome/FilterByOrientationBias.java
+ 相关文章：https://academic.oup.com/bib/article/22/6/bbab186/6278604；https://pubmed.ncbi.nlm.nih.gov/34015811/；


## 4.3. #
### 4.3.1. mutect2的AF（AF calculation in Mutect2）
> One possibility is that there are reads supporting one or the other allele that aren't being counted in the AD values because they're not considered informative for the purposes of the genotyping, but they are being counted in the allele fraction estimation. Another is that there are reads supporting some other allele that is not called, but is present in some minor fraction, and is therefore counted in the AF estimation as well. In both cases you would see them if you look at read data in the bam file (preferably the "bamout" that can be generated as documented for HaplotypeCaller).

> Because the DP in the INFO field is unfiltered and the DP in the FORMAT field is filtered, you know none of the reads were filtered out by the engine's built-in read filters.

https://gatk.broadinstitute.org/hc/en-us/articles/360035532252?id=6005

https://gatk.broadinstitute.org/hc/en-us/community/posts/360057830232-Wrong-Calculation-of-DP-AD-AF

https://github.com/broadinstitute/gatk/issues/6067

## 4.4. Contamination 样本间污染评估
This tool borrows from ContEst by Cibulskis et al the idea of estimating contamination from ref reads at hom alt sites. However, ContEst uses a probabilistic model that assumes a diploid genotype with no copy number variation and independent contaminating reads. That is, ContEst assumes that each contaminating read is drawn randomly and independently from a different human. This tool uses a simpler estimate of contamination that relaxes these assumptions. In particular, it works in the presence of copy number variations and with an arbitrary number of contaminating samples. In addition, this tool is designed to work well with no matched normal data. However, one can run GetPileupSummaries on a matched normal bam file and input the result to this tool.

### 4.4.1. ContEst（gatk3） 
+ Low	levels	of	cross-sample	contamina*on	is	common	
+ Contaminant	sites	vary	from	patient	homozygous	sites	
![](./pics/20210111.png)
![](./pics/202101111.png)
![](./pics/202101112.png)
Three major classes of DNA contamination exist: 
+ **cross-individual**
+ within-individual
+ cross-species

```
This example will produce an output file which should look like the following:

name    population      population_fit  contamination   confidence_interval_95_width    confidence_interval_95_low      confidence_interval_95_high     sites
META    CEU     n/a     8.2     0.9     7.7     8.6     733

Here we can see that ContEst found that the file was approximately 8.2 percent contaminated, with a 95% confidence interval from 7.7 to 8.6. 
```
结论：
ContEst produces accurate estimates even with average coverage <5×.

### 4.4.2.  
+ 对肿瘤BAM运行GetPileupSummaries以总结tumor样本在已知变异位点集上的reads支持情况。
+ 如果存在配对样本，会对正常样本运行GetPileupSummaries以总结tumor样本在已知变异位点集上的reads支持情况。
+ 对已知变异位点集采用CalculateContamination来估计污染比例，segments.table文件的最后一列用来判断突变位点是否为样本污的位点。

需要指出几点：在默认参数中，此工具只考虑样本中纯和备用位点：等位基因频率范围在0.01-0.2（相关参数是--minimum-population-allele-frequency和--maximum-population-allele-frequency）,这样设计的理论基础是：如果某个纯和备用位点的人群频率较低，当发生样本交叉污染时，我们更容易观测到ref allele（或更常见allele）的出现，这样我们可以更准确地定量污染比例。


#### 4.4.2.1. getpileupsummaries
```
#<METADATA>SAMPLE=AG945-2
contig	position	ref_count	alt_count	other_alt_count	allele_frequency
chr1	17365	3	2	0	0.136
chr1	17385	8	0	0	0.122
chr1	69761	0	0	0	0.113
```
# 5. This produces a six-column table as shown. The `alt_count` is the count of reads that support the ALT allele in the germline resource. The `allele_frequency` corresponds to that given in the germline resource. Counts for `other_alt_count` refer to reads that support all other alleles.


https://github.com/mikdio/SOBDetector


----
## 5.1. Mutect2 bamout reports fewer reads than VCF AD
#### 5.1.0.2. Ref_Info
https://gatk.broadinstitute.org/hc/en-us/community/posts/360060670091--GATK-v4-1-6-0-Mutect2-bamout-reports-fewer-reads-than-VCF-AD


## 5.2. 方法

### 5.2.1. 定义活跃区域
Mutect2 triages sites for possible somatic variation and determines intervals over which to assemble reads by assigning each site’s read pileup a log odds for somatic activity via a simplified version of the somatic genotyping model, below. A site is considered “active” if its log odds exceed some threshold. Like HaplotypeCaller, Mutect2 chooses for assembly intervals that surround each active site with some margin. The details of this are discussed in the supplemental material.
### 5.2.2. Assembling Haplotypes
### 5.2.3. Somatic Genotyping

### 5.2.4. 过滤
FilterMutectCalls首先估计每个候选突变是体细胞变异的可能性，而不是胚系变异或测序错误等。然后，它选择使估计的F分数最大化的概率阈值（recall和precision的 harmonic mean），并进行相应过滤。错误概率是从几种不同的错误模型中得出的，其中最简单的是硬过滤器，当注释超过某个阈值时，它们会将错误概率分配为1。
+ Hardfilter:
Error probabilities are derived from several different error models, the simplest of which are hard filters that assign an error probability of 1 when an annotation exceeds some threshold. These include filters for variants with an excess of low-quality supporting bases, poor mapping quality, support coming exclusively near the end of reads, a large mismatch in lengths between variant- and reference-supporting fragments, and local haplotypes with too many variants.

+ PON:
+ probabilistic models:
  + germline model
  + The normal artifact model
  + The contamination model
  + short tandem repeat (STR) model
  + strand bias and orientation bias artifacts

#### 5.2.4.1.  
## 5.3. Results
### 5.3.1. DREAM Challenge
### 5.3.2. Normal-Normal Calls
A popular way to measure the false positive rate of somatic variant callers is to assign one normal sample as a “tumor” and a technical replicate of the same sample as the “matched normal.”
### 5.3.3. Normal mixtures

### 5.3.4. workflow
```
#GATK 3
java -jar GenomeAnalysisTK.jar \
-T MuTect2 \
-R <reference> \
-L <region> \
-I:tumor <tumor.bam> \
-I:normal <normal.bam> \
--normal_panel <pon.vcf> \                        
--cosmic <cosmic.vcf> \
--dbsnp <dbsnp.vcf> \
--contamination_fraction_to_filter 0.02 \                   
-o <mutect_variants.vcf> \
--output_mode EMIT_VARIANTS_ONLY \
--disable_auto_index_creation_and_locking_when_reading_rods
```
### 5.3.5. 参数理解
GATK Mutect2 官网文档中有关于--cosmic和--dbsnp两个参数的描述：

 >“MuTect2 has the ability to use COSMIC data in conjunction with dbSNP to adjust the threshold for evidence of a variant in the normal. If a variant is present in dbSNP, but not in COSMIC, then more evidence is required from the normal sample to prove the variant is not present in germline.”

```
```
### 5.3.6. 参数理解
`--disable-read-filter MateOnSameContigOrNoMappedMateReadFilter`, 禁用此过滤器，目的是为了将配对的read map到不同染色体上的那些reads也纳入考虑，从而使得可供分析的read更多。


### 5.3.7. strand bias


FS is Phred-scaled p-value using Fisher’s Exact Test to detect strand bias (the variation being seen on only the forward or only the reverse strand) in the reads. More bias is indicative of false positive calls.


One nice explanation could be found in this samtools mailing list post

If you have only reads in one strand you can not "have" strand bias, or at least you can not measure it, since the other strand has 0 reads.

The strand bias measure if the proportion of alleles is statistically different between strands. As you don't have reads in the other strand, you can not measure it. You can only measure allele bias (departure of the 0.5 if you are expecting germline heterozygotes)

You can also read here that GATK keeps SNPs with strand bias p-value < 60 for filtering SNP (equivalent to p-value > 0.000001). But they also mention here that A higher score indicates a higher probability that a particular  decision is correct, while conversely, a lower score indicates a  higher probability that the decision is incorrect.
----https://www.biostars.org/p/244911/

```
chr10   3875262 .       A       G       32      .       DP=16;AF1=0.5001;CI95=0.5,0.5;DP4=5,0,9,0;MQ=20;FQ=9.52;PV4=1,1,1,0.097 GT:PL:GQ        0/1:62,0,36:39
```

```
sb <-
matrix(c(3, 1, 1, 3),
       nrow = 2,
       dimnames = list(c("ref_forward", "ref_reverse"),
                       c("alt_forward", "alt_reverse")))
fisher.test(sb, alternative = "greater")

#ref_forward = number of forward reads supporting the reference
#ref_reverse = number of reverse reads supporting the reference
#alt_forward = number of forward reads supporting the variant
#alt_reverse = number of reverse reads supporting the variant
```
https://sourceforge.net/p/samtools/mailman/samtools-help/thread/4E177430.7030802@bcgsc.ca/

## 5.4. source-code
gatk3:https://github.com/broadgsa/gatk-protected/blob/master/protected/gatk-tools-protected/src/main/java/org/broadinstitute/gatk/tools/walkers/cancer/m2/MuTect2.java#L806

gatk3: https://github.com/broadinstitute/mutect/blob/69b7a37fcafe8a68f7470436f24e44df740f1c41/src/org/broadinstitute/cga/tools/gatk/walkers/cancer/mutect/MuTectArgumentCollection.java

gatk4:https://github.com/broadinstitute/gatk/blob/master/src/main/java/org/broadinstitute/hellbender/tools/walkers/mutect/filtering/M2FiltersArgumentCollection.java

## 5.5. 算法
Icy☜♬☞冬至 17:09:00
https://www.strand-ngs.com/files/promotions/SNP-WhitePaper-GATK.pdf

Icy☜♬☞冬至 17:09:01
https://resources.qiagenbioinformatics.com/white-papers/White_paper_on_probabilistic_variant_caller_1.1.pdf

https://best-practices-for-processing-hts-data.readthedocs.io/en/latest/mutect2_pitfalls.html


## 5.6. 教程
https://notebooks.githubusercontent.com/view/ipynb?browser=chrome&color_mode=auto&commit=e1946f5f8f025a416872d27bbb4fe86b9c68179e&device=unknown&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6761746b2d776f726b666c6f77732f6761746b342d6a7570797465722d6e6f7465626f6f6b2d7475746f7269616c732f653139343666356638663032356134313638373264323762626234666538366239633638313739652f6e6f7465626f6f6b732f446179332d536f6d617469632f312d736f6d617469632d6d7574656374322d7475746f7269616c2e6970796e62&logged_in=false&nwo=gatk-workflows%2Fgatk4-jupyter-notebook-tutorials&path=notebooks%2FDay3-Somatic%2F1-somatic-mutect2-tutorial.ipynb&platform=android&repository_id=183114910&repository_type=Repository&version=98
