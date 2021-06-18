
## Data Resources Required
https://data.broadinstitute.org/Trinity/CTAT_RESOURCE_LIB/
plug-n是已经建立好的reference lib, 而source里面包含了所需的原始文件。从原始文件构建reference lib的命令如下:

```
tar xvf GRCh37_v19_CTAT_lib_Feb092018.source_data.tar.gz
cd GRCh37_v19_CTAT_lib_Feb092018/

export PATH="/local_data1/MED/programs/RNAtools/gmap-2020-06-04/bin:$PATH"
export PATH="/local_data1/MED/programs/RNAtools/STAR-2.7.8a/bin/Linux_x86_64_static:$PATH"
export PATH="/local_data1/MED/programs/zhangbo/hmmer-3.3.1/bin/:$PATH"
/local_data1/MED/programs/FUSIONtools/STAR-Fusion-v1.10.0/ctat-genome-lib-builder/prep_genome_lib.pl --genome_fa /local_data1/MED/database/hg19/gatk_bundle/ucsc.hg19.fasta --gtf /local_data1/MED/database/hg19/rnaseq/hg19_GENCODE37lift37/gencode.v37lift37.annotation.gtf --dfam_db human --fusion_annot_lib fusion_lib.Mar2021.dat.gz --human_gencode_filter --pfam_db current --output_dir ctat_genome_lib_build_dir --CPU 14


#/local_data1/MED/programs/FUSIONtools/STAR-Fusion-v1.8.1/ctat-genome-lib-builder/util/rebuild_indices.pl .

```

## 解压后的原始文件
### source data
```
GRCh37_gencode_v19_CTAT_lib_Mar012021.source.tar.gz

build_ctat_lib.sh
_dfam_db_prep_chckpts
__dfam_ref_annot.cdsplus.fa
fusion_lib.Mar2021.dat.gz
__gencode_refinement_chkpts
gencode.v19.annotation.gtf
gencode.v19.annotation.gtf.revised.custom.gtf
gencode.v19.annotation.gtf.revised.gtf
GRCh37.p13.genome.primary.fa
GRCh37.p13.genome.primary.fa.pseudo_masked.fa
__loc_chkpts
__paralogs
para.mask.list
_pfam_db_prep_chckpts
PFAM.domtblout.dat.gz
ref_annot.cdna.fa
ref_annot.cdna.fa.allvsall.outfmt6.toGenes.sorted.gz
ref_annot.cdsplus.dfam_masked.fa
ref_annot.cdsplus.dfam_masked.fa.allvsall.outfmt6.genesym.best.overlaps_filt.gz
ref_annot.cdsplus.fa
ref_annot.pep.fa
```
### plug-n-play data
```
[ctat_genome_lib_build_dir]$ ls
AnnotFilterRule.pm        ref_annot.gtf.gene_spans
blast_pairs.dat.gz        ref_annot.gtf.mini.sortu
blast_pairs.idx           ref_annot.pep
__chkpts                  ref_annot.prot_info.dbm
fusion_annot_lib.gz       ref_genome.fa
fusion_annot_lib.idx      ref_genome.fa.fai
pfam_domains.dbm          ref_genome.fa.nhr
PFAM.domtblout.dat.gz     ref_genome.fa.nin
ref_annot.cdna.fa         ref_genome.fa.nsq
ref_annot.cdna.fa.idx     ref_genome.fa.star.idx
ref_annot.cds             trans.blast.align_coords.align_coords.dat
ref_annot.cdsplus.fa      trans.blast.align_coords.align_coords.dbm
ref_annot.cdsplus.fa.idx  trans.blast.dat.gz
ref_annot.gtf
```

http://note.youdao.com/noteshare?id=365f4e006571dab8d6b4e411eca81e57
## 其工作原理分为三步：

+ ①先将reads通过STAR比对到参考基因组，筛选出split和discordant reads作为候选的融合基因序列；
+ ②将候选融合基因序列与参考基因序列进行比对，根据overlaps预测出融合基因；
+ ③对预测结果做过滤，去除假阳性结果。

## 检出率

+ I change the option "--alignSplicedMateMapLminOverLmate" from the default value 0.66 to a lower one

## 设计引物来对该融合转录本进行验证