[toc]
## 在线注释
http://grch37.ensembl.org/Homo_sapiens/Tools/VEP?db=core

## 安装
http://www.ensembl.org/info/docs/tools/vep/script/vep_download.html

# 安装
## 1. 安装perl 模块
```
Archive::Zip
DBD::mysql
DBI

export HTSLIB_DIR=/public/frasergen/MED/software/htslib-1.13
/public/frasergen/MED/software/zhangbo/PERL/cpanm -l /public/frasergen/MED/software/zhangbo/PERL/perl-5.28.2/cpanm Bio::DB::HTS
```

```
mkdir $VEP_PATH $VEP_DATA; 
```

## 2. 下载vep主体
```
cd $VEP_PATH

## Use git to download the ensembl-vep package:
git clone https://github.com/Ensembl/ensembl-vep.git
cd ensembl-vep
## or Download the Zipped package file
curl -L -O https://github.com/Ensembl/ensembl-vep/archive/release/94.zip
unzip 94.zip
cd ensembl-vep-release-94/

## update
cd ensembl-vep
git pull
git checkout release/93 #93可以换成任何版本

```
指定文件环境和路径
```
export PERL5LIB=$VEP_PATH:$PERL5LIB
export PATH=$VEP_PATH/htslib:$PATH

export VEP_PATH=$HOME/vep
export VEP_DATA=$HOME/.vep

```


### 3. 手动下载库文件


### 下载数据库

https://asia.ensembl.org/info/docs/tools/vep/script/vep_cache.html:

+ ftp://ftp.ensembl.org/pub/release-101/variation/indexed_vep_cache/
  + cache 有三种：有Ensembl转录本、RefSeq转录本及二者整合
```
homo_sapiens_merged_vep_104_GRCh37.tar.gz          13-Apr-2021 10:55         16563762788
homo_sapiens_merged_vep_104_GRCh38.tar.gz          12-Apr-2021 15:54         18507398045
homo_sapiens_refseq_vep_104_GRCh37.tar.gz          13-Apr-2021 10:56         14029086699
homo_sapiens_refseq_vep_104_GRCh38.tar.gz          12-Apr-2021 15:56         15264843771
homo_sapiens_vep_104_GRCh37.tar.gz                 13-Apr-2021 10:57         14733702560
homo_sapiens_vep_104_GRCh38.tar.gz                 12-Apr-2021 15:57         15787286822
```
+ http://ftp.ensembl.org/pub/release-104/variation/vep/

```
cd $VEP_DATA
wget -c http://ftp.ensembl.org/pub/release-104/variation/indexed_vep_cache/homo_sapiens_refseq_vep_104_GRCh37.tar.gz
```
### 3. 下载vep api
http://www.ensembl.org/info/docs/tools/vep/script/vep_download.html#requirements

```
perl INSTALL.pl --AUTO ap --SPECIES homo_sapiens --ASSEMBLY GRCh37 --DESTDIR $VEP_PATH --CACHEDIR $VEP_DATA

```
### 构建索引文件
```
perl convert_cache.pl --species homo_sapiens --version 86_GRCh37 --dir $VEP_DATA
```

# 运行
```
perl variant_effect_predictor.pl --species homo_sapiens --assembly GRCh37 --offline --no_progress --no_stats --sift b --ccds --uniprot --hgvs --symbol --numbers --domains --gene_phenotype --canonical --protein --biotype --uniprot --tsl --pubmed --variant_class --shift_hgvs 1 --check_existing --total_length --allele_number --no_escape --xref_refseq --failed 1 --vcf --minimal --flag_pick_allele --pick_order canonical,tsl,biotype,rank,ccds,length --dir $VEP_DATA --fasta $VEP_DATA/homo_sapiens/86_GRCh37/Homo_sapiens.GRCh37.75.dna.primary_assembly.fa.gz --input_file example_GRCh37.vcf --output_file example_GRCh37.vep.vcf --polyphen b --gmaf --maf_1kg --maf_esp --regulatory --custom $VEP_DATA/ExAC_nonTCGA.r0.3.1.sites.vep.vcf.gz,ExAC,vcf,exact,1,AC,AN

```
#https://gist.github.com/ckandoth/f265ea7c59a880e28b1e533a6e935697
