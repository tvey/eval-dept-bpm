from django.urls import path

from bpm.users.views import example

app_name = 'users'

urlpatterns = [
    path('', view=example, name='example'),
]
