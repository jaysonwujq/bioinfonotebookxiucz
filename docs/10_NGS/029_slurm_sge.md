# SLURM
```
1、SLURM系统里-n 2，2是指任务数，一个脚本同时执行2次还是串行执行呢。
2、大多数生信任务是单进程多线程
3、SLURM系统的四种执行方式：串行、并行MPI、单节点openmp(生信常用)、MPI+openmp
4、#BATCH -t 2-00:00:00
5、pestat -p/-w 查看节点情况
```

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