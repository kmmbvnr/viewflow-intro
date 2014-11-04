from viewflow import flow
from viewflow.base import Flow, this
from viewflow.contrib import celery

from . import models, views, tasks


class HelloWorldFlow(Flow):
    process_cls = models.HelloWorldProcess

    start = flow.Start(views.CreateRequestView) \
        .Next(this.approve)

    approve = flow.View(views.ApproveRequestView) \
        .Next(this.is_approved)

    is_approved = flow.If(lambda p: p.approved) \
        .OnTrue(this.send)\
        .OnFalse(this.end)

    send = celery.Job(tasks.send) \
        .Next(this.end)

    end = flow.End()
