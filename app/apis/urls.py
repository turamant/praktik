from django.urls import path

from apis.views import GetListAllNew

app_name = 'api'

urlpatterns = [
    path('list/all/new/', GetListAllNew.as_view())
]
