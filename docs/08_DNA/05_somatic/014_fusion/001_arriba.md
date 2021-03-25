## database
```
hg19+RefSeq 
    +GENCODE19 
    +ENSEMBL87

hg38+RefSeq
    +ENSEMBL93
    +GENCODE28

GRCh37+ENSEMBL87 
      +RefSeq

GRCh38+RefSeq
      +GENCODE19
      +ENSEMBL93
      +GENCODE28

hs37d5+RefSeq
      +GENCODE19      
      +ENSEMBL87
```


```
STAR --chimOutType WithinBAM， then this file contains all the information needed by Arriba to find fusions 

     --chimOutType SeparateSAMold, the main output file lacks chimeric alignments.
```