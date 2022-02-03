from django.urls import path

from web_admin.views import CreateNew

app_name = 'web_admin'

urlpatterns = [
    path('', CreateNew.as_view(), name='create_new'),
]
