```
$ bedtools --version
bedtools v2.18.0
#output depth of coverage for all regions in the BAM file, sequential positions at the same read depth are merged into a single region
bedtools genomecov -ibam [BAM] -bga -split > CoverageTotal.bedgraph

#output the per base read depth for each region in the BED file
bedtools coverage -a [BED] -b [BAM] -d > PerBaseDepthBED.bedgraph

#get percent genome covered
zero=$(bedtools genomecov -ibam [BAM] -g [ref.fasta] -bga | awk '$4==0 {bpCountZero+=($3-$2)} {print bpCountZero}' | tail -1)
nonzero=$(bedtools genomecov -ibam [BAM] -g [ref.fasta] -bga | awk '$4>0 {bpCountNonZero+=($3-$2)} {print bpCountNonZero}' | tail -1)
percent=$(bc <<< "scale=6; ($nonzero / ($zero + $nonzero))*100")
```
