from demo.celery import app as celery_app
from viewflow.flow import flow_job


@celery_app.task()
@flow_job()
def send(activation):
    print(activation.process.text)
