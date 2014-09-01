from django.views import generic
from viewflow import views as flow_views


class CreateRequestView(flow_views.StartViewMixin,
                        generic.UpdateView):
    fields = ["text"]

    def get_object(self):
        return self.activation.process


class ApproveRequestView(flow_views.TaskViewMixin,
                         generic.UpdateView):
    fields = ["approved"]

    def get_object(self):
        return self.activation.process

