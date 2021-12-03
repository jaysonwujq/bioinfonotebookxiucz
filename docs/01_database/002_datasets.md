https://www.synapse.org/#!Synapse:syn312572/wiki/60873

https://umccr.org/blog/bwa-mem-vs-minimap2/
- We downloaded 2 datasets with curated somatic variants: - ICGC medulloblastoma. Tumor: 103x, normal: 89x (downsampled from tumor: 314x, normal: 272x).
  - https://www.nature.com/articles/ncomms10001
- COLO829 metastatic melanoma cell line. Tumor: 81x, normal: 79x
  - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4837349/

# 1000g
http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/phase3/data/

# na12878
http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/phase3/data/NA12878/

https://www.internationalgenome.org/data-portal/sample/NA12878

## cnv
https://www.ncbi.nlm.nih.gov/sra/?term=SRR622461
+  ILLUMINA (Illumina HiSeq 2000) run: 92.5M spots, 18.7G bases, 4.8Gb downloads
+ 1000 Genomes on GRCh38
  + SRR622461 low coverage wgs
    + ftp:/­/­ftp.­sra.­ebi.­ac.­uk/­vol1/­fastq/­SRR622/­SRR622461/­SRR622461_2.­fastq.­gz 
```
/home/zhangbo/.aspera/connect/bin/ascp -QT -l 300m -P33001 -i ~/.aspera/connect/etc/asperaweb_id_dsa.openssh era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR622/SRR622461/SRR622461.fastq.gz . && mv SRR622461.fastq.gz SRR622461_Illumina_sequencing_of_HapMap_individual_NA12878_aligned_by_BI_downsampled_to_5x_coverage.fastq.gz
/home/zhangbo/.aspera/connect/bin/ascp -QT -l 300m -P33001 -i ~/.aspera/connect/etc/asperaweb_id_dsa.openssh era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR622/SRR622461/SRR622461_1.fastq.gz . && mv SRR622461_1.fastq.gz SRR622461_Illumina_sequencing_of_HapMap_individual_NA12878_aligned_by_BI_downsampled_to_5x_coverage_1.fastq.gz
/home/zhangbo/.aspera/connect/bin/ascp -QT -l 300m -P33001 -i ~/.aspera/connect/etc/asperaweb_id_dsa.openssh era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR622/SRR622461/SRR622461_2.fastq.gz . && mv SRR622461_2.fastq.gz SRR622461_Illumina_sequencing_of_HapMap_individual_NA12878_aligned_by_BI_downsampled_to_5x_coverage_2.fastq.gz
```
+ 1000 Genomes phase 3 release
  + ftp:/­/­ftp.­1000genomes.­ebi.­ac.­uk/­vol1/­ftp/­phase3/­data/­NA12878/­sequence_read/­SRR622461_1.­filt.­fastq.­gz 
```
 ll
total 13580512
drwxr-xr-x 2 zhangbo med           4096 Apr  8 17:26 .
drwxr-xr-x 6 zhangbo zhangbo       4096 Apr  8 15:54 ..
-rw-r--r-- 1 zhangbo med     4515787433 Apr  8 17:40 SRR622461_1.filt.fastq.gz
-rw-r--r-- 1 zhangbo med     4598249219 Apr  8 17:11 SRR622461_Illumina_sequencing_of_HapMap_individua
l_NA12878_aligned_by_BI_downsampled_to_5x_coverage_1.fastq.gz
-rw-r--r-- 1 zhangbo med     4792383631 Apr  8 17:16 SRR622461_Illumina_sequencing_of_HapMap_individua
l_NA12878_aligned_by_BI_downsampled_to_5x_coverage_2.fastq.gz
-rw-r--r-- 1 zhangbo med            318 Apr  8 17:08 SRR622461_Illumina_sequencing_of_HapMap_individua
l_NA12878_aligned_by_BI_downsampled_to_5x_coverage.fastq.gz
```
### cnv golden dataset
https://doi.org/10.1371/journal.pcbi.1007069.s004

https://mp.weixin.qq.com/s/LYBcfMILpvHL2LnguB2ebg

