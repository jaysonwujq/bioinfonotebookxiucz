# dbSNP
NCBI Assay ID(ss)

Reference SNP ID(rs)
对于每一个提交到dbSNP数据库的SNP位点, 首先会赋予一个唯一的ss ID。 由于不同研究结构提交的SNP会存在冗余，提取SNP位点上下游区域的序列，比对参考基因组，如果多个ss ID 比对上相同的位置，说明这几个SNP位点是冗余的，会赋予一个新的reference SNP ID, 以rs开头。

## 下载地址
```
ftp://ftp.ncbi.nih.gov/snp/organisms/human_9606/VCF/

#hg19
wget https://ftp.ncbi.nih.gov/snp/redesign/latest_release/VCF/GCF_000001405.25.gz
wget https://ftp.ncbi.nih.gov/snp/redesign/latest_release/VCF/GCF_000001405.25.gz.tbi
wget https://raw.githubusercontent.com/Shicheng-Guo/AnnotationDatabase/master/GCF_000001405.25_GRCh37.p13_assembly_report.txt

#hg38
wget https://ftp.ncbi.nih.gov/snp/redesign/latest_release/VCF/GCF_000001405.38.gz
wget https://ftp.ncbi.nih.gov/snp/redesign/latest_release/VCF/GCF_000001405.38.gz.tbi
https://raw.githubusercontent.com/Shicheng-Guo/AnnotationDatabase/master/GCF_000001405.38_GRCh38.p12_assembly_report.txt

```
以上链接的染色体名字是ncbi格式的（NC_..），关于染色体名字格式修改：https://www.biostars.org/p/98582/, 格式转化
```
python CrossMap.py vcf hg38Tohg19.over.chain.gz GCF_000001405.38.gz hg19.fa  GCF_000001405.hg19.vcf
```

## 处理
```
wget -qO- https://ftp.ncbi.nih.gov/snp/organisms/human_9606_b151_GRCh37p13/VCF/00-All.vcf.gz \
   | gunzip -c \
   | vcf2bed --sort-tmpdir=${PWD} - \
   | awk -v FS="\t" -v OFS="\t" '{ print $4, $1, $2, $3 }' \
   | sort -k1,1 \
   > hg19.dbSNPAllV151.sortedByName.txt
```

```
$ wget -qO- ftp://ftp.ncbi.nih.gov/snp/organisms/human_9606_b151_GRCh37p13/VCF/common_all_20180423.vcf.gz | gunzip -c | convert2bed --input=vcf --output=bed --sort-tmpdir=${PWD} - > hg19.snp151.bed
$grep -F rs554008981 gnomad.hg19.bed
$ grep -fF rsIDs.txt hg19.snp151.bed > matches.bed
```

###  All_20180423.vcf.gz and 00-All.vcf.gz 的区别

## 根据rs号获取对应的信息
### 
```
https://www.ncbi.nlm.nih.gov/snp/?term=rs140337953+or+rs116440577+or+rs150021059
```

```
#http://codextechnicanum.blogspot.com/2017/07/querying-ncbi-dbsnp-for-rsid-mergers_23.html
#
from Bio import Entrez
import sys

Entrez.email = 'yourEmail@institution.com'

handle = Entrez.efetch(db="snp", id="rs140337953, rs116440577, rs150021059", rettype = 'chr', retmode = 'text')
sys.stdout.write(handle.read())
handle.close()
```

## 根据gene 获取rs号
```
library(rentrez)
# for converting gene name -> gene id
gene_search <- entrez_search(db="gene", term="(PTEN[Gene Name]) AND Homo sapiens[Organism]", retmax=1)
geneId <- gene_search$ids 
# elink function
snp_links <- entrez_link(dbfrom='gene', id=geneId, db='snp')

# access results with $links
length(snp_links$links$gene_snp)
5779

head(snp_links$links$gene_snp)
'864622690' '864622594' '864622518' '864622451' '864622387' '864622341' 

#多个基因
multi_snp_links <- entrez_link(dbfrom='gene', id=c("5728", "374654"), db='snp', by_id=TRUE)
lapply(multi_snp_links, function(x) head(x$links$gene_snp))
```

### api
```
https://api.ncbi.nlm.nih.gov/variation/v0/#/
```

```
http://mulinlab.tmu.edu.cn/gwas4d
```

```
http://cbportal.org/3dsnp/
```

## 利用annovar 获取rs号信息
```
/local_data1/MED/programs/Annotools/annovar_2019Oct24/annovar/table_annovar.pl rs.snp138.txt --outfile rs.snp138.txt.anno --buildver hg19 /local_data1/MED/database/hg19/humandb --otherinfo --remove --protocol refGene --operation g   --nopolish
/local_data1/MED/programs/Annotools/annovar_2019Oct24/annovar/convert2annovar.pl  -format rsid  rs.txt   -dbsnpfile /local_data1/MED/database/hg19/humandb/hg19_snp138.txt > rs.snp138.txt
```

## 同一个rs对应不同的NC 和NG
```
https://www.pharmgkb.org/variant/PA166155091

```

## annotate bed with rs
https://www.biostars.org/p/272876/
```
import re
import requests
import xml.etree.ElementTree as ET

def rs_fetch(chrom, pos):
    """
    截至2018年5月1日，NCBI根据客户机是否 已注册。未注册的客户端限制为每秒3个请求； 注册客户每秒被授予10个请求，并且可以请求 更多。
    """
#https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=snp&term=63499726%5BPOSITION_GRCH37%5D+AND+8%5BCHR%5D
    url="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=snp&term=" + str(pos) + \
        "%5BPOSITION_GRCH37%5D+AND+" + str(chrom) + "%5BCHR%5D"
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        html = response.text
#        root = ET.fromstring(html)
#        for child in root:
#            print(child.tag, child.attrib)
        rsID = re.search("<ID>(\d+)<\/Id>",li).group(0)
        print(rsID)
    else:
        print("xx")
rs_fetch(8, 63499726)
```