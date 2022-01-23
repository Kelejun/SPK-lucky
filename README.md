# SPK-lucky
用于 [SPKitz](https://spk.foehn.club/) [(Bilibili)](https://space.bilibili.com/252967669) [抽奖活动](https://spk.foehn.club/special-event/229/) 的开奖程序

## 关于程序

### 原理
获取表格行数，然后生成大于等于一且小于等于行数的真随机数，然后输出对应一行表格的数据。

### 使用到的第三方 Python 库
库名称|用途
---|:--:|
random|生成随机数
xlrd|读取 Excel 表格
tkinter|生成选择文件窗口

### 使用
此程序可以经过简单修改输出内容后抽取新的 Excel 表格以抽奖，**无需授权，允许自用及修改**

表格拓展名为 .xls 注意不支持 .xlsx 及 .csv 

表内格式：

表头|表头
---|:--:|
数据1-1|数据1-2
数据2-1|数据2-2
...|...

### 开发
[可乐菌](https://blog.ke-lejun.xyz)
