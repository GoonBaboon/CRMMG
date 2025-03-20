from .import views
from django.urls import path, include

urlpatterns = [
    path('',views.lessons_view, name='lessons_list'),
    path('<int:lesson_id>/', views.lesson_detail_view, name='lesson_detail'),
]
