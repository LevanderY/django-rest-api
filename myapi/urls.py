from django.urls import path
from .views import UsersListCreateView, UsersDetailView

urlpatterns = [
    path('users/', UsersListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UsersDetailView.as_view(), name='user-detail'),
]