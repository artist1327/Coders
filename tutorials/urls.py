
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:tutorials_id>/', views.details, name='details'),
    path('<int:section_id>/mock_test',views.mock, name="mock"),
    path('add/', views.TopicCreate.as_view(), name='add-topic'),
    path('<int:section_id>/favourite/mock_test/', views.mock, name='mock'),
    path('<int:tutorials_id>/favourite/', views.favourite, name='favourite'),
    path('register/', views.UserFormView.as_view(), name="register"),


]
