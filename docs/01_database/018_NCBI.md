#
https://bioinformatics.cvr.ac.uk/ncbi-entrez-direct-unix-e-utilities/

Compare Accession, Version, and GI number
> https://www.ncbi.nlm.nih.gov/Class/MLACourse/Modules/Format/exercises/qa_accession_vs_gi.html


https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?mode=c#SG4


## 根据登录号下载序列/gb
```
http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=CP000962&rettype=fasta&retmode=text

acc_id=CP000962
wget -c "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=${acc_id}&rettype=fasta&retmode=text" -O ${acc_id}.fasta

http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=CP000962&rettype=gb&retmode=text

```
1. <http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?> This is command telling your computer program (or your browser) to talk to the NCBI API tool efetch.
2. <db=nuccore> This command tells the NCBI API that you’d like it to look in this particular database for some data. Other databases that the NCBI has available can be found [here](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi).
3. <id=CP000962> This command tells the NCBI API efetch the ID of the genome you want to find.
4. <rettype=gb&retmode=text> These two commands tells the NCBI how the data is returned. You’ll note that in the two examples above this command varied slightly. In the first, we asked for only the FASTA sequence, while in the second, we asked for the Genbank file. Here’s some elusive documentation on where to find these “return” objects.

