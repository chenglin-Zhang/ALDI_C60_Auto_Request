# ALDI_C60_Auto_Request

## os 模块

```
os.getcwd()：查看当前所在路径。
os.listdir(path):列举目录下的所有文件。返回的是列表类型。
os.path.abspath(path):返回path的绝对路径。
os.path.split(path):将路径分解为(文件夹,文件名)，返回的是元组类型。
os.path.join(path1,path2,...):将path进行组合，若其中有绝对路径，则之前的path将被删除。
os.path.dirname(path):返回path中的文件夹部分，结果不包含'\' 
os.path.basename(path):返回path中的文件名。

os.path.getmtime(path):文件或文件夹的最后修改时间，从新纪元到访问时的秒数。
os.path.getatime(path):文件或文件夹的最后访问时间，从新纪元到访问时的秒数。
os.path.getctime(path):文件或文件夹的创建时间，从新纪元到访问时的秒数。

os.path.getsize(path):文件或文件夹的大小，若是文件夹返回0。
os.path.exists(path):文件或文件夹是否存在，返回True 或 False。
```



写文件

![img](https://img2018.cnblogs.com/blog/1150129/201906/1150129-20190604111410731-619344652.png)



dict <-> json

dumps()：将字典转换为JSON格式的字符串

loads()：将JSON格式的字符串转化为字典

dump()：将字典转换为JSON格式的字符串，并将转化后的结果写入文件

load()：从文件读取JSON格式的字符串，并将其转化为字典

eval(): 字符串转json



切割字符串

```
str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( );       # 以空格为分隔符，包含 \n
print str.split(' ', 1 ); # 以空格为分隔符，分隔成两个
```



同时遍历list

```
for (k,v) in zip(k_list, v_list)
```

