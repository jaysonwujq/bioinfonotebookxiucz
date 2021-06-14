<!-- TOC -->

- [GenomicFeatures](#genomicfeatures)
            - [Ref_Info](#ref_info)
- [GenomicRanges](#genomicranges)

<!-- /TOC -->

# GenomicFeatures

https://www.bioconductor.org/packages/release/bioc/html/GenomicFeatures.html

https://www.bioconductor.org/packages/release/bioc/vignettes/GenomicFeatures/inst/doc/GenomicFeatures.pdf

```
BiocManager::install("TxDb.Hsapiens.UCSC.hg19.knownGene")
library(TxDb.Hsapiens.UCSC.hg19.knownGene)
txdb <- TxDb.Hsapiens.UCSC.hg19.knownGene
class(txdb)
txdb
```

获取染色体号
```
head(seqlevels(txdb))
#只保留chr1
seqlevels(txdb) <- "chr1"
seqlevels(txdb)
#恢复初始设置
seqlevels(txdb) <- seqlevels0(txdb)
head(seqlevels(txdb))
```

```
keytypes(txdb)
```

#### Ref_Info
https://www.jianshu.com/p/e0515071f175

# GenomicRanges