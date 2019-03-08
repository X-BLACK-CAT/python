
import os

# Application配置参数
settings = {
    'static_path':os.path.join(os.path.dirname(__file__),'static'),
    'cookie_secret':'raz0hZa1Tx+egdIxcMgm4vKoVK7Hmk+rpwbWDyjqL4U=',
    'xsrf_cookies':True,
    'debug':True,
}
# mysql
mysql_options = dict(
    host="127.0.0.1",
    database="ihome",
    user="root",
    password="123456"
)

# redis
redis_options = dict(
    host="127.0.0.1",
    port=6379
)

# 日志
log_level = "debug"
log_path = os.path.join(os.path.dirname(__file__),"logs/log.log")