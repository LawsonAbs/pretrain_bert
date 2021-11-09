<!--
 * @Author: LawsonAbs
 * @Date: 2021-09-04 22:07:40
 * @LastEditTime: 2021-11-09 14:50:10
 * @FilePath: /pretrain_bert/README.md
-->
# 0. 环境要求
执行本代码的环境要求如下：
- 安装包版本
torch                              1.8.1
tqdm                               4.61.0
transformers                       4.7.0
visdom                             0.1.8.9
python                             3.8.3
pandas                             1.0.5
- 显卡
GeForce RTX 2080Ti * 1
对应Nvidia驱动 Driver Version: 455.45.01，CUDA Version: 11.1 。使用如上配置，应可在机器上顺利执行。


# 1. 任务
在特定任务的数据集上进行预训练BERT.