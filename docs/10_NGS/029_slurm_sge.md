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

fs_status
```
#!/bin/bash
#负载统计
node_list=(haba0240 haba0241 haba0242 haba0307 haba0308 haba0309 haba0303 haba0301 haba0137 haba0151 haba0315)

for node in ${node_list[@]}; do
            partition=`sinfo -n $node | grep $node | awk '{print $1}'`
        node_info=`pestat | grep $node | sed 's#*##g'`
        node_status=`echo $node_info | awk -F [' ']+ '{print $2}'`
        node_cpuUse=`echo $node_info | awk -F [' ']+ '{print $3}'`
        node_cpuAv=`expr 128 - $node_cpuUse`
        node_memUse=`echo $node_info | awk -F [' ']+ '{print $7}'`
        node_memUse_G=`expr $node_memUse / 1024 - 20`
        echo "队列: $partition 节点: $node 状态: $node_status 可用CPU: $node_cpuAv 可用内存: $node_memUse_G GB"
done
```

# qsub
```
#查看已结束的任务
qacct -j 4578395
```