from django.urls import path
from User.views import UserView

app_name = 'GestionPqrs'

urlpatterns = [
    path('get', UserView.as_view(), name='get-user'),
    path('create', UserView.as_view(), name='create-user'),
    path('update', UserView.as_view(), name='update-user'),
    path('delete', UserView.as_view(), name='delete-user'),
]