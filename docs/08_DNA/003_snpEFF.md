SnpEff & SnpSift 

http://pcingola.github.io/SnpEff/se_human_genomes/
```
java -jar /public/frasergen/MED/software/ANNOtools/snpEff/snpEff_5.0/snpEff.jar hg19 -canon -hgvs1LetterAa test.vcf | grep -v "^#" > test.snpEff.shift.vcf
java -jar /public/frasergen/MED/software/ANNOtools/snpEff/snpEff_5.0/snpEff.jar hg19 -canon -noShiftHgvs -hgvs1LetterAa test.vcf | grep -v "^#" > test.snpEff.noshift.vcf
```