### 安装依赖库

```
# tornado 安装
pip install tornado

# mysql 数据库操作库
pip install Tornado-MySQL
```

### mysql 数据库相关配置
- config/database.py

```
Mysql_config = dict(
    driver='mysql',
    host='127.0.0.1',
    port=3306,
    database='blog',
    user='root',
    password='12345678',
)
```

### 启动

```
# 项目文件根目录下,执行
python __main__.py

# 或项目文件外一层,执行
python tornado_web
```

> 项目的基本结构是搭建完成了. 
> 简单实现了首页列表和详情页的查询操作.
> mysql 数据库的操作还是不那么顺当,具体内容实现就暂时不实现了.
> 如果有像 php 的 laravel 有封装的那么好的数据库操作 api 就好了.

### 项目基本结构

```html
root
├──config/                 * 相关配置文件(数据库,静态资源路径等)
├──controllers/            * 控制器集合,
├──databases/              * 数据库操作相关,数据库实例化函数等
├──models/                 * 数据模型操作
├──routes/                 * 路由的集中配置
├──static/                 * 静态资源目录
├──utils/                  * 公用工具包
├──views/                  * 视图模板文件集合
├──__main__.py             * 入口文件
└──entry.py                * 入口主要逻辑
```
