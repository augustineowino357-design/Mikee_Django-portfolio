from django.contrib import admin
from django.urls import path
from projects import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.portfolio_index, name='portfolio_index'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
]