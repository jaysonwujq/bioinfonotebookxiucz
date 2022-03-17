+ https://lbgi.fr/AnnotSV/

+ https://lbgi.fr/AnnotSV/ranking

+ https://lbgi.fr/AnnotSV/Documentation/README.AnnotSV_latest.pdf

## 安装
`make PREFIX=. install-human-annotation`

```
curl -C - -LO https://www.lbgi.fr/~geoffroy/Annotations/2007_hg19.tar.gz
curl -C - -LO https://data.monarchinitiative.org/exomiser/data/2007_phenotype.zip

#install -d -p ./share/AnnotSV/Annotations_Exomiser/2007
tar -xf 2007_hg19.tar.gz -C ./share/AnnotSV/Annotations_Exomiser/2007/
unzip 2007_phenotype.zip -d ./share/AnnotSV/Annotations_Exomiser/2007/
tar -xf Annotations_Human_3.0.9.tar.gz -C ./share/AnnotSV/

```

