# coding=utf-8
# 使用rabbitmq作为消息代理
BROKER_URL = 'amqp://dongwm:123456@localhost:5672/web_develop'
# 把任务结果存在redis中
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
# 任务序列化和反序列化使用msgpack方案
CELERY_TASK_SERIALIZER = 'msgpack'
CELERY_RESULT_SERIALIZER = 'json'
# 任务过期时间
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']
