# 数据集
### 韩国人基因组计划KPGP:
+  http://opengenome.net/index.php/Main_Page
+ https://pzweuj.github.io/2018/11/16/KPGP.html

https://portals.broadinstitute.org/ccle/data


##Benchmark datasets
ICGC benchmarking exercise

```
Medulloblastoma tumour/normal pair sequenced in 6 different centres to combined 300-fold coverage used to establish 'truth'

16 ICGC project teams ran their pipelines on data from one centre (40x)

Alioto et al., Nat Commun. 2015
```

ICGC-TCGA DREAM Somatic Mutation Calling challenge

```
6 synthetic datasets based on cell line sequenced to 80x, BAM randomnly split into 2 ('tumour' and 'normal'), mutations added to one computationally

Synthetic dataset 4: 80% cellularity; 50% and 35% subclone VAF (effectively 30% and 15%)

Ewing et al., Nat Methods 2015 [leaderboards]
```

https://login.illumina.com/platform-services-manager/?rURL=https://basespace.illumina.com&clientId=basespace&clientVars=aHR0cHM6Ly9iYXNlc3BhY2UuaWxsdW1pbmEuY29tL2FuYWx5c2VzLz9vZmZzZXQ9MCZzb3J0Ynk9TW9kaWZpZWRPbiZzb3J0ZGlyPWRlc2MmbGltaXQ9MjU&redirectMethod=GET


# rnaseq 数据集
https://github.com/STAR-Fusion/STAR-Fusion_benchmarking_data


----
# NA12878
+ https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/phase3/data/NA12878/
+ https://www.internationalgenome.org/data-portal/sample/NA12878
NA12878 variation benchmark, 
ftp://ftp-trace.ncbi.nlm.nih.gov/giab/ftp/technical/svclassify_Manuscript/Supplementary_Information/

NA12878 CNV Benchmark：
> ftp://ftp-trace.ncbi.nlm.nih.gov/giab/ftp/technical/svclassify_Manuscript/Supplementary_Information、Personalis_1000_Genomes_deduplicated_deletions.bed
 filtered to retain only deletions ≥1 kb
> https://ars.els-cdn.com/content/image/1-s2.0-S0002929717304962-mmc4.txt

+ The CNVs in this GS set range from 50 bp to 453,312 bp with 1,941 and 135 autosomal deletions and duplications, respectively.


# Cancer-like mixture with Genome in a Bottle samples
This example simulates somatic cancer calling using a mixture of two Genome in a Bottle samples, NA12878 as the “tumor” mixed with NA24385 as the background. The Hartwig Medical Foundation and Utrecht Medical Center generated this “tumor/normal” pair by physical mixing of samples prior to sequencing. The GiaB FTP directory has more details on the design and truth sets. The sample has variants at 15% and 30%, providing the ability to look at lower frequency mutations.

To get the data:
```
wget https://raw.githubusercontent.com/bcbio/bcbio-nextgen/master/config/examples/cancer-giab-na12878-na24385-getdata.sh
bash cancer-giab-na12878-na24385-getdata.sh
```
https://bcbio-nextgen.readthedocs.io/en/latest/contents/somatic_variants.html#workflow4-cancer-like-mixture-with-genome-in-a-bottle-samples
