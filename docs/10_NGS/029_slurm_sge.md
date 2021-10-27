

```
#!/bin/bash

# Get first job id

jid=$(sbatch job1.slurm | cut -d ' ' -f4)

# Remainder jobs
for k in {2..100};
    do temp="${k}"
        jid=$(sbatch --dependency=afterok:${jid} job${k}.slurm | cut -d ' ' -f4)
    done
```

# qsub
```
#查看已结束的任务
qacct -j 4578395
```