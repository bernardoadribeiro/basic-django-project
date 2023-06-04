from django.urls import path
from projects import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.project_detail, name='project_detail'),
]
