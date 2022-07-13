fade=/public/frasergen/MED/software/zhangbo/miniconda3/envs/fade/bin/fade
fade=/public/frasergen/MED/software/QCtools/fade
filein=/public/frasergen/RNA/work/liwei/med/Test/leukemia_exon/iGeneTech-VS-Agilent/LJH-QW3/out/02_realign/LJH-QW3.recalibrated.bam
ref_hsa=/public/frasergen/MED/database/hg19/gatk_bundle/ucsc.hg19.fasta
outpre=LJH-QW3
```
$fade annotate \
-t 8 \
-b $filein $ref_hsa > $outpre.fadeanno.bam

$samtools sort -@ $cores -n $outpre.fadeanno.bam > $outpre.fadeanno.qsort.bam
$fade out -t 8 -b $outpre.fadeanno.qsort.bam > $outpre.fadeanno.filtered.bam
samtools sort -@ $cores $outpre.fadeanno.filtered.bam > $outpre.fade.bam
samtools index -@ $cores $outpre.fade.bam

/public/frasergen/MED/software/zhangbo/miniconda3/envs/fade/bin/fade stats -t 8 LJH-QW3.fadeanno.bam > LJH-QW3.fadeanno.stats.bam
```