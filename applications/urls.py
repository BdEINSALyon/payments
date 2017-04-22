from django.conf.urls import url

from applications.views import ApplicationList, ApplicationDetail

urlpatterns = [
    url(r'^$', ApplicationList.as_view(), name='applications'),
    url(r'^(?P<pk>[0-9]+)$', ApplicationDetail.as_view(), name='application'),
]