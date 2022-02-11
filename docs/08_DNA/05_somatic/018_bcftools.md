<!-- TOC -->

- [过滤](#过滤)
  - [bcftools filter](#bcftools-filter)
- [注释](#注释)
- [安装报错](#安装报错)
  - [解决zlib.h:no such file or directory](#解决zlibhno-such-file-or-directory)

<!-- /TOC -->
+ Does “multiallelic” denote “more than 2 alleles” rather than “not monomorphic”?

Yes. 2 or more alternate alleles at a site.

+ The number of SNPS+indels+others does not sum to the total number of records. Is this because an SNP can also be an indel or “other?”

A mutilallelic site may contain both a SNP and an indel for instance and hence will contribute a count to both tallies.
+ What types of variants are covered by “others” here?

complex substitutions, SVs, complex rearrangements. Basically anything not a SNP, insertion/deletion (unless represented by a symbolic allele) or MNP.
+ Why is the id[2] field blank for all sections of my output?

id field is relevant when comparing two files with bcftools stats. id will then be 0,1 or 2 and will represent sites unique to the first file, sites unique to the second file and sites common to both.

https://github.com/samtools/bcftools/issues/316

## 过滤
### bcftools filter
```
bcftools view -q 0.01 chr.all.vcf.gz 
bcftools view -q 0.01:minor chr.all.vcf.gz

```
```
bcftools view -e 'INFO/IMPUTED=1' or bcftools view -i 'INFO/IMPUTED=0'
```

```
FORMAT/AD[0:1] - number of ALT alleles
FORMAT/AD[0:0] - number of REF alleles
```
## 注释
```
export BCFTOOLS_PLUGINS=/local_data1/MED/programs/zhangbo/bcftools/bcftools-1.9/plugins/
bcftools +fill-tags my.vcf > out.vcf
```


## 安装报错
```
http://samtools.github.io/bcftools/howtos/install.html

git clone --recurse-submodules git://github.com/samtools/htslib.git
git clone git://github.com/samtools/bcftools.git
cd bcftools
 # The following is optional:
 #   autoheader && autoconf && ./configure --enable-libgsl --enable-perl-filters
make

https://raw.githubusercontent.com/samtools/bcftools/develop/INSTALL
```

### 解决zlib.h:no such file or directory
```
在~/.bashrc中屏蔽了conda的字段后，注销重新登陆，重新编译就pass了。
```

## 
https://medium.com/brown-compbiocore/building-a-consensus-sequence-with-vcf-files-db7407f3f86f