## 版本更新
**2019Oct24：**
+ 利用annotate_variation.pl中的-downdb参数可以允许refGeneWithVer作为一个有效的基因注释
+ add -intronhgvs argument to print out HGVS notations for intronic variants;
+ add startloss and startgain as functional consequences that affects the first ATG codon; add -nofirstcodondel to table_ by default to enable calculation of amino acid changes for certain variants previously annotated as 'wholegene'; minor adjustment on nonframeshift vs startloss vs stopgain for certain variants with multiple valid notations; changed p. notation for block substitution that does not cause protein change; changed table_ so that ExAC and gnomAD are treated as float fields in VCF annotation; allow genericdb for region annotation; allow chromosome name to contain . or - for certain species; the -polish argument is ON by default in table_.pl; table_.pl can generate column headers such as Otherinfo, Otherinfo2, Otherinfo3, etc; fixed a bug of cdot notation for block substitutions that cover 5UTR and start codon


## cosmic数据库准备
```
#!/bin/bash
# ./cosmic2annovar.sh mail:passwd

for i in "CosmicCodingMuts.vcf.gz" "CosmicNonCodingVariants.vcf.gz"
do
    curl $(curl -H "Authorization: Basic $(echo "$1" | base64)" https://cancer.sanger.ac.uk/cosmic/file_download/GRCh37/cosmic/v90/VCF/$i | awk -F '"' '{print $4}') -o $i
done 


for i in "CosmicMutantExport.tsv.gz" "CosmicNCV.tsv.gz"
do
    curl $(curl -H "Authorization: Basic $(echo "$1" | base64)" https://cancer.sanger.ac.uk/cosmic/file_download/GRCh37/cosmic/v90/$i | awk -F '"' '{print $4}') -o $i
done

gunzip *.gz

./prepare_annovar_user.pl -dbtype cosmic CosmicMutantExport.tsv -vcf CosmicCodingMuts.vcf >hg19_cosmic90.txt
./prepare_annovar_user.pl -dbtype cosmic CosmicNCV.tsv -vcf CosmicNonCodingVariants.vcf >>hg19_cosmic90.txt

sort -V hg19_cosmic90.txt >hg19_cosmic90_sort.txt

mv hg19_cosmic90_sort.txt hg19_cosmic90.txt

./index_annovar.pl hg19_cosmic90.txt 1000
```


https://pzweuj.github.io/2018/07/27/annovar-clinvar.html

https://zhengzexin.com/archives/automatic_update_Clinvar_db_for_ANNOVAR/

如果想扩大剪接位点两侧突变检测范围 , 在-argument 参数后边对应 refGene数据库的位置 添加-splicing_threshold 10 ， 如： -argument '-splicing_threshold 10 -hgvs' 引号内表示对refGene 数据库进行 -splicing_threshold 10 和 -hgvs 两个处理，所以用引号引起来。

## clinvar 数据库处理
```
>>> x = b'\xe9'
>>> x.decode()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 0: unexpected end of data
>>> x.decode('latin1').encode('utf-8')
b'\xc3\xa9'
>>> x.decode('latin1')
'é'
>>> x.decode('latin1').encode('utf-8')
b'\xc3\xa9'
```