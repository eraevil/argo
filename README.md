# argo
基于WebGIS技术实现Argo浮标观测数据的可视化

> 项目使用的软件和环境版本

序号|环境|版本
:---:|:---:|:---:
1|Python|3.8
2|PyCharm 专业版|2021.3
3|PostgreSQL|11.14.1
4|Navicat Premium|15.0.27
5|Debian|11.3
6|GeoServer|2.20.4
7|QGIS|3.18.2-1

> 本项目中使用的包/依赖/框架

序号|包名|版本|用途
:---:|:---:|:---:|:---
1|xarray|0.20.1|读取 nc 格式文件
2|numpy|1.21.4|科学数据操作
3|psycopg|3.0.5|数据库操作
4|psycopg-binary|3.0.5|数据库操作
5|django|4.0.4|后端框架
6|django-cors-headers|3.12.0|解决后端跨域访问的问题
7|cesuim|—|基于 WebGL 的 JavaScript 框架，显示三维地球影像和地图
8|echarts|—|完成图表可视化
9|jquery|—|JavaScript 框架

> 数据库信息

序号|项目|值
:---:|:---:|:---:
1|连接名host|'localhost'
2|端口号port|5432
3|数据库名dbname|'argodb'
4|用户名user|'postgres'


> 构建项目
```
python manage.py runserver
```

> 功能模块

* 浮标位置显示 
* 温、盐、等温、混合层、合成混合层月平均数据显示 
* 绘制温盐曲线 
* 绘制浮标轨迹图 

> 目录结构
```
argo
│   README.md
│   manage.py                # 项目入口文件
│
└───apptest                  # 后端目录
│   │   views.py             # 视图 
│   │   models.py            # 模型
|   |   urls.py              # 路由设置
|   |   ...
│   
└───static                   # 静态资源目录
│   │   
│   └───data                 # 数据
|   └───js                   # javascript资源
|   └───sql                  # 数据库备份
|   └───libs                 # Cesium、bootstrap、echarts等依赖安装位置
|   |   ...
|
└───templates/apptest        # 模板文件
└───argo                     # 项目配置
```

> 效果图

<div align=center>
<img src="https://user-images.githubusercontent.com/35321279/173275549-cee5022e-e3fb-45cf-9fa8-5a907fc63b9e.png" width="100%" height="" />
<img src="https://user-images.githubusercontent.com/35321279/173275566-9e1b0f76-4bf7-43c5-8159-cd957925ef5c.png" width="100%" height="" />
<img src="https://user-images.githubusercontent.com/35321279/173275594-9f75f6fe-f8b1-49f6-aca4-cdf62c8ab658.png" width="100%" height="" />
<img src="https://user-images.githubusercontent.com/35321279/173275620-d65d2608-d872-417d-bdf1-8fedf68d5f44.png" width="100%" height="" />
<img src="https://user-images.githubusercontent.com/35321279/173275634-fd143e71-6bbc-4c59-a9e8-ffcfb468de43.png" width="100%" height="" />
<img src="https://user-images.githubusercontent.com/35321279/173275647-5f33d270-eef2-444a-a763-d6d88aa5d400.png" width="100%" height="" />
<img src="https://user-images.githubusercontent.com/35321279/173275656-05a97794-b709-4253-ae1d-4869a406690c.png" width="100%" height="" />
<img src="https://user-images.githubusercontent.com/35321279/173275674-6b9a903f-b270-4796-b55e-af809d677c26.png" width="100%" height="" />
<img src="https://user-images.githubusercontent.com/35321279/173275683-8061c6a3-16d7-4455-bb13-685e56f43a9e.png" width="100%" height="" />
<img src="https://user-images.githubusercontent.com/35321279/173275690-5a26b6a1-6512-4e6b-b26a-314832f7e839.png" width="100%" height="" />
</div>





