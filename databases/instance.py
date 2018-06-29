# coding=utf-8

from config.database import Mongo_config, Mysql_config

import asyncmongo
from tornado_mysql import pools


# mongodb 连接
def get_mongo_instance():
    return asyncmongo.Client(
        pool_id='mydb',
        host=Mongo_config['host'],
        port=Mongo_config['port'],
        dbname=Mongo_config['database']
    )


# mysql 连接
def get_mysql_instance():
    return pools.Pool(
        dict(
            host=Mysql_config['host'],
            port=Mysql_config['port'],
            user=Mysql_config['user'],
            password=Mysql_config['password'],
            db=Mysql_config['database']
        )
    )
