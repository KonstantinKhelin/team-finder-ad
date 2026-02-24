from django.urls import path
from . import views
app_name = 'projects'

urlpatterns = [
    path('project/list/', views.project_list , name='list'),
    path('project/create/', views.project_create , name='create'),
    path('project/<int:project_id>/', views.project_detail , name='detail'),
    path('project/<int:project_id>/edit/', views.project_create , name='edit'),
    path('project/<int:project_id>/complete/', views.project_complete , name='complete'), # post при нажатии "Завершить проект"

    path('project/<int:project_id>/skills/<skill_id>/remove/', views. , name='remove_skill'), #post
    path('project/skills/add/', views.skill_add , name='add'), #post
    path('project/skills/<str:skill_name>/', views.skill_search , name='search'), #get
]