https://academic.oup.com/bioinformatics/article/34/4/585/4457361

# taxanomy
```
ls ./taxonomy/
names.dmp  nodes.dmp  nucl_gb_wgs.accession2taxid.gz  prot.accession2taxid
```

```
cd /local_data1/public_data/database/metagenome/NR/nr_classify

/local_data1/software/blast_plus/ncbi-blast-2.7.1_plus/bin/makeblastdb -dbtype prot -input_type fasta -in Archaea.fa -out Archaea
/local_data1/software/blast_plus/ncbi-blast-2.7.1_plus/bin/makeblastdb -dbtype prot -input_type fasta -in Bacteria.fa -out Bacteria
/local_data1/software/blast_plus/ncbi-blast-2.7.1_plus/bin/makeblastdb -dbtype prot -input_type fasta -in Fungi.fa -out Fungi
/local_data1/software/blast_plus/ncbi-blast-2.7.1_plus/bin/makeblastdb -dbtype prot -input_type fasta -in metagenome.fa -out metagenome
/local_data1/software/blast_plus/ncbi-blast-2.7.1_plus/bin/makeblastdb -dbtype prot -input_type fasta -in Viruses.fa -out Viruses
/local_data1/software/diamond/diamond makedb --in Archaea.fa --db Archaea --threads 4
/local_data1/software/diamond/diamond makedb --in Bacteria.fa --db Bacteria --threads 4
/local_data1/software/diamond/diamond makedb --in Fungi.fa --db Fungi --threads 4
/local_data1/software/diamond/diamond makedb --in metagenome.fa --db metagenome --threads 4
/local_data1/software/diamond/diamond makedb --in Viruses.fa --db Viruses --threads 4
gzip Archaea.fa
gzip Bacteria.fa
gzip Fungi.fa
gzip metagenome.fa
gzip Viruses.fa
```


https://github.com/jtamames/SqueezeMeta


## 人体微生物
https://mp.weixin.qq.com/s/Rsc-jb3EiQGEUb-FAWDAkA

https://umccr.org/blog/oncoviral-integration/

https://github.com/vladsaveliev/oviraptor
