[TOC]
# exomeCopy
http://www.bioconductor.org/packages/2.9/bioc/html/exomeCopy.html


## Installation

https://bmcgenomics.biomedcentral.com/articles/10.1186/1471-2164-15-661

### bug
1. 为了减少麻烦，使用R：https://cran.r-project.org/src/base/R-3/R-3.1.2.tar.gz。
2. 修改路径并运行, 
```
DECoN-master/Linux/setup.sh
#!/bin/bash

[ -w ".Rprofile" ] && rm .Rprofile

/local_data1/MED/programs/R/R-3.2.1/bin/Rscript sessionInfo.R --bootstrap-packrat > setup.log 2>&1

cp packrat/packrat_source/.Rprofile ./

```
下载依赖的包，对应版本可以搜索得到
```
https://cran.r-project.org/src/contrib/Archive/digest/digest_0.6.8.tar.gz
wget https://cran.r-project.org/src/contrib/Archive/VGAM/VGAM_0.9-8.tar.gz

source("http://bioconductor.org/biocLite.R")
biocLite("BiocParallel")

```
### 修改脚本
IdentifyFailures.R这一步似乎消耗大量的内存,这种sapply 绝了。
```
brca<-sapply(failed.calls$chr, '==',exons$Chr) & sapply(failed.calls$start, '>=',exons$Start) \
    & sapply(failed.calls$end, '<=',exons$End) | \
    sapply(failed.calls$chr, '==',exons$Chr) & sapply(failed.calls$start, '<=',exons$Start) \
    & sapply(failed.calls$end, '>=',exons$Start) | \
    sapply(failed.calls$chr, '==',exons$Chr) & sapply(failed.calls$start, '<=',exons$End) \
    & sapply(failed.calls$end, '>=',exons$End)
```

```
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install("exomeCopy", version = "3.8")
```
background:

```
> exome.samples <- grep("HG.+", colnames(mcols(example.counts)),
+     value = TRUE)
> example.counts$bg <- generateBackground(exome.samples,
+     example.counts, median)
> example.counts$log.bg <- log(example.counts$bg + 0.1)
> example.counts$bg.var <- generateBackground(exome.samples,
+     example.counts, var)
```

# ExomeDepth
https://github.com/vplagnol/ExomeDepth

- it in fact performs best on smaller panels
- ExomeDepth is primarily designed for inherited changes. 
- 
https://cran.r-project.org/web/packages/ExomeDepth/vignettes/ExomeDepth-vignette.pdf

---
# DECoN
https://wellcomeopenresearch.org/articles/1-20/v1
```
Rscript ReadInBams.R --bams bams.file --bed bed.file   --fasta fasta.file --out output.prefix

Rscript IdentifyFailures.R --Rdata summary.file --mincorr .98   --mincov 100  --exons customNumbers.file --custom FALSE --out output.prefix

Rscript makeCNVcalls.R --Rdata summary.file --transProb transition.probability   --exons customNumbers.file --custom FALSE --out output.prefix –-plot All  --plotFolder DECoNPlots

```

## INPUT
bed file:
+  the targeted 1-based BED file to be used for analysis
+  

---

# ExCopyDepth
https://static-content.springer.com/esm/art%3A10.1186%2F1471-2164-15-661/MediaObjects/12864_2014_6348_MOESM1_ESM.pdf
