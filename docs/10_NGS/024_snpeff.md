# 构建本地数据库
以`JX549382.1`为例，在`snpEff/data`文件夹中建立文件夹
```
[zhangbo@mu01 data]$ tree
.
├── genomes
│   ├── JX549382.1.fasta
│   ├── JX549382.1.fa -> JX549382.1.fasta
│   ├── NC_045512.2.fa
│   └── sequence.fasta -> /local_data1/MED/database/mngs/nCov2019/NC_045512.2/sequence.fasta
├── JX549382.1
│   ├── genes.gff -> JX549382.1.gff3
│   └── JX549382.1.gff3
└── NC_045512.2
    ├── genes.gff
    ├── sequence.gff3 -> /local_data1/MED/database/mngs/nCov2019/NC_045512.2/sequence.gff3
    └── snpEffectPredictor.bin

#注意 `fa` `genes.gff` 命名
```
> 00:00:00	Warning: Cannot read optional protein sequence file '/local_data1/MED/programs/Annotools/snpEff/./data/JX549382.1/protein.fa', nothing done.

```
echo '# Database for JX549382.1 (JX549382.1)' >> snpEff.config
echo 'JX549382.1.genome : JX549382.1' >> snpEff.config
```
```
[zhangbo@mu01 snpEff]$ java -jar snpEff.jar build -gff3 -v JX549382.1
```

```
[zhangbo@mu01 snpEff_5.0]$ echo '# Database for SARS-CoV-2 (NC_045512.2)' >> snpEff.config
[zhangbo@mu01 snpEff_5.0]$ echo 'sars.cov.2.genome : SARS-CoV-2' >> snpEff.config
[zhangbo@mu01 snpEff_5.0]$ echo '        sars.cov.2.chromosomes : NC_045512' >> snpEff.config
[zhangbo@mu01 snpEff_5.0]$ exec/snpeff build -genbank -v sars.cov.2
```