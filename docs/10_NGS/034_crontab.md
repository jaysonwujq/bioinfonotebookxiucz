```
分 时 日 月 星期 要运行的命令

第1列分钟0～59
第2列小时0～23（0表示子夜）
第3列日1～31
第4列月1～12
第5列星期0～7（0和7表示星期天）
第6列要运行的命令



echo $(date) >> /home/ubuntu/c.log

实例1：每1分钟执行一次myCommand
* * * * * myCommand
* * * * * echo $(date) >> /home/ubuntu/c.log

实例2：每小时的第3和第15分钟执行
3,15 * * * * myCommand
实例3：在上午8点到11点的第3和第15分钟执行
3,15 8-11 * * * myCommand
实例4：每隔两天的上午8点到11点的第3和第15分钟执行
3,15 8-11 */2  *  * myCommand
实例5：每周一上午8点到11点的第3和第15分钟执行
3,15 8-11 * * 1 myCommand
实例6：每晚的21:30重启smb
30 21 * * * /etc/init.d/smb restart

3.2.2 每天8点到17点的第15和第45分钟执行

15,45 8-17 * * * echo $(date) >> /home/ubuntu/c.log

3.2.3 每周一上午8点30分钟执行

30 8 * * 1 echo $(date) >> /home/ubuntu/c.log

3.2.4 每月1、15日01:00执行

0 1 1,15 * * echo $(date) >> /home/ubuntu/c.log

3.2.5 每一小时执行一次

* */1 * * * echo $(date) >> /home/ubuntu/c.log

3.2.6 晚上11点到早上7点之间每隔一小时执行一次

* 23-7/1 * * * echo $(date) >> /home/ubuntu/c.log

# 每天自动触发统计通知
* * */1 * * curl http://*domain.com/statnotify

```
https://crontab.guru/#*/59_*_*_*_*