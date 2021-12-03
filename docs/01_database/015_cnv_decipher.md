

## annovar 注释decipher数据库

```
$ perl table_annovar.pl W001.avinput /your/path/of/annovar/humandb/ --buildver hg19 -remove -out sample -protocol refGene,cytoBand,omim201806,gwasCatalog,CCRS,phastConsElements100way,phastConsElements46way,phastConsElements46wayPlacental,phastConsElements46wayPrimates,tfbsConsSites,rmsk,dgvMerged,HIP,Constraint -operation g,r,r,r,r,r,r,r,r,r,r,r,r,r -nastring . --thread 12

```

HIP和Constraint的数据来源于DECIPHER，可以作为参考，下面记录一下如何下载并转换格式。
```
# DECIPHER数据库提供了在线的可视化的检索方式，可以查看相关变异的很多信息，包括表型、致病性等，这些信息都是临床或科研单位上传的。其中DECIPHER可供下载的数据包括以下三种
# Haploinsufficiency Predictions:
#    Updated predictions of haploinsufficiency as described by Huang et al. (2010, PLoS Genetics). Available as a Bed file for download from the link above.
$ wget https://decipher.sanger.ac.uk/files/downloads/HI_Predictions_Version3.bed.gz
# Population Copy-Number Variation Frequencies
#    Common copy-number variants and their frequencies, as used and displayed in DECIPHER.
$ wget https://decipher.sanger.ac.uk/files/downloads/population_cnv.txt.gz
# Development Disorder Genotype – Phenotype Database (DDG2P) 
#    a curated list of genes reported to be associated with developmental disorders, compiled by clinicians as part of the DDD study to facilitate clinical feedback of likely causal variants. Please note: This file is maintained by the European Bioinformatics Institute. Its contents may differ from DECIPHER due to different update cycles.
$ wget http://www.ebi.ac.uk/gene2phenotype/downloads/DDG2P.csv.gz
# 上面是下载了三个数据库，当然下面只用到了两个，还有一个频率数据库笔者也不知道怎么去注释和使用比较好
# 上述三个数据库直接用gunzip去解压就行
# pLI:
    $ awk -F "\t" '{print 0"\t"$3"\t"$5"\t"$6"\t"$20}' Constraint.txt > hg19_Constraint.txt
    $ sed -i '1d' hg19_Constraint.txt
# HIP:
    $ sed -i '1d' HI_Predictions_Version3.bed 
    $ bedtools sort -i HI_Predictions_Version3.bed > HIP.txt
    $ awk -F "\t" '{print 0"\t"$1"\t"$2"\t"$3"\t"$4}' HIP.txt > hg19_HIP.txt
```