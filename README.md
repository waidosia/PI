# 基于Pyecharts + Flask + Pingpong 智能家居数字大屏系统

 本篇README.md面向开发者
 
## 目录

- [上手指南](#上手指南)
  - [开发前的配置要求](#开发前的配置要求)
- [文件目录说明](#文件目录说明)
- [开发的架构](#开发的架构)
- [使用到的框架](#使用到的框架)
  - [如何参与开源项目](#如何参与开源项目)
- [版本控制](#版本控制)
- [作者](#作者)

### 上手指南
![](https://pic-1300802512.cos.ap-guangzhou.myqcloud.com/5ktyv8w77b-1648191059229.png)

###### 开发前要求

1. ESP8266、esp32
2. 树莓派

###### 执行
```shell
python server.py
```

### 文件目录说明（仅展示树莓派相关文件）
```
PI
├── /db/
|  |——database.sqlite 
|  └──db.py 
├── /other/
|  |──send.py 
├── README.md
├── templates 
|  |——index.html
|  |——login.html
|  └── ...
├── client.py
├── login_s
├── pyecharts_tool.py
├── scratch.py
└── server.py
```





### 开发的架构 

### 部署

暂无

### 使用到的框架

- [flask](https://github.com/pallets/flask)
- [pyecharts](https://github.com/pyecharts/pyecharts)
- [mqtt](https://github.com/emqx/MQTTX)



### 版本控制

该项目使用Git进行版本管理。您可以在repository参看当前可用版本。

