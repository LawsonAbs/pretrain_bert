import os
'''
Author: LawsonAbs
Date: 2021-11-08 20:48:00
LastEditTime: 2021-11-08 21:16:12
FilePath: /pretrain_bert/data/code/tools.py
'''
# 读取train+test+dev的数据，然后生成一个总得文件 raw_data.txt
def read_all_text(paths):    
    all_text = []
    for path in paths:
        # 得到指定路径下的所有文件
        file_names = os.listdir(path)
        
        for name in file_names:
            cur_path = os.path.join(path, name)
            with open(cur_path, 'r') as f:
                content = f.readlines()
                for line in content:
                    if len(line) > 50 : # 如果长度超过20，则放到结果文件中
                        all_text.append(line)

    out_path = "all_data.txt"
    with open(out_path, 'w') as f:
        for line in all_text:
            f.write(line)

if __name__ == '__main__':
    paths =["/home/lawson/program/pretrain_bert/data/raw_data/dev","/home/lawson/program/pretrain_bert/data/raw_data/train","/home/lawson/program/pretrain_bert/data/raw_data/test"]
    read_all_text(paths)