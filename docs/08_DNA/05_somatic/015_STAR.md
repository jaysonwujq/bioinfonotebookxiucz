<!-- TOC -->


<!-- /TOC -->


sjdbOverhang

## 建立索引
```
STAR --runThreadN 6 --runMode genomeGenerate --genomeDir index_dir --genomeFastaFiles genome.fasta --sjdbGTFfile genome.gtf --sjdbOverhang 149

```

## 比对
```
STAR --twopassMode Basic --quantMode TranscriptomeSAM GeneCounts --runThreadN 6 --genomeDir index_dir --alignIntronMin 20 --alignIntronMax 50000 --outSAMtype BAM SortedByCoordinate --sjdbOverhang 149 --outSAMattrRGline ID:sample SM:sample PL:ILLUMINA --outFilterMismatchNmax 2 --outSJfilterReads Unique --outSAMmultNmax 1 --outFileNamePrefix out_prefix --outSAMmapqUnique 60 --readFilesCommand gunzip -c --readFilesIn seq1.fq.gz seq2.fq.gz

--twopassMode Basic：使用two-pass模式进行reads比对。简单来说就是先按索引进行第一次比对，而后把第一次比对发现的新剪切位点信息加入到索引中进行第二次比对。
--quantMode TranscriptomeSAM GeneCounts：将reads比对至转录本序列。
--runThreadN：线程数。
--genomeDir：索引目录。
--alignIntronMin：最短的内含子长度。（根据GTF文件计算）
--alignIntronMax：最长的内含子长度。（根据GTF文件计算）
--outSAMtype BAM SortedByCoordinate：输出BAM文件并进行排序。
--sjdbOverhang：reads长度减1。
--outSAMattrRGline：ID代表样本ID，SM代表样本名称，PL为测序平台。在使用GATK进行SNP Calling时同一SM的样本可以合并在一起。
--outFilterMismatchNmax：比对时允许的最大错配数。
--outSJfilterReads Unique：对于跨越剪切位点的reads（junction reads)，只考虑跨越唯一剪切位点的reads。
--outSAMmultNmax：每条reads输出比对结果的数量。
--outFileNamePrefix：输出文件前缀。
--outSAMmapqUnique 60：将uniquely mapping reads的MAPQ值调整为60，满足下游使用GATK进行分析的需要。
--readFilesCommand：对FASTQ文件进行操作。
--readFilesIn：输入FASTQ文件的路径。
```

```
STAR --runThreadN 4 \
    --outSAMtype BAM SortedByCoordinate \
    --outSAMstrandField intronMotif \
    --outFilterIntronMotifs RemoveNoncanonicalUnannotated \
    --outReadsUnmapped None \
    --chimSegmentMin 15 \
    --chimJunctionOverhangMin 15 \
    --chimOutType WithinBAM \
    --alignMatesGapMax 200000 \
    --alignIntronMax 200000 \
    --genomeDir $STAR_GENOME_INDEX \
    --readFilesIn $SAMPLE_FASTQ_1 $SAMPLE_FASTQ_2 \
    --outFileNamePrefix $TUTORIAL_HOME/analysis/star/$SAMPLE_ID/
    --outSAMtype BAM SortedByCoordinate \

    --outFileNamePrefix $TUTORIAL_HOME/analysis/star/$SAMPLE_ID/
```
--chimSegmentMin 20 --chimOutTypeWithinBAM

In order to obtain alignments of chimeric reads potentially supporting fusions, we have added the --chimSegmentMin 20 option to obtain chimerica reads anchored by at least 20nt on either side of the fusion boundary, and --chimOutTypeWithinBAM to report such alignments in the sam/bam output.