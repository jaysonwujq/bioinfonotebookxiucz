## 拆分fasta
```
#!/usr/ben/env python
import re
from Bio import SeqIO

d = {}
with open("sequence.fasta") as fh:
    for seq_record in SeqIO.parse(fh, "fasta"):
        seqname = seq_record.id
        print(seqname)
        d[seqname]  = open(f"{seqname}.fa", "w")
        d[seqname].write(seq_record.format("fasta"))

```

```
 seqkit -w 0 split -i --id-regexp '.*-(\w+_\w+)\.*$' test.fa -O new_files
```