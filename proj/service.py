from celery import Celery

print(Celery)
app = Celery('proj',
            #broker='amqp://localhost:5672',
            #backend='redis://localhost:6379',
            broker='amqp://aaa:aaa@172.1.1.11:5672/%2Faaa',
            backend='redis://172.1.1.11:6377',
            include=['proj.tasks'])
print(app)

# Optional configuration, see the application user guide.
#app.conf.update(
#    result_expires=3600,
#    )

if __name__ == '__main__':
        app.start()
