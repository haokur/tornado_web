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