from . import views
from django.urls import path, include

urlpatterns = [

    path('', views.addtask, name="addtask"),
    path('delete/<int:taskid>/', views.delete, name="delete"),
    path('update/<int:taskid>/', views.update, name="update"),
    path('cbvhome/',views.tasklistview.as_view(),name='cbvhome'),
    path('cbvdetails/<int:pk>/', views.detailview.as_view(), name='cbvdetails'),
    path('cbvupdate/<int:pk>/', views.updateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.deleteview.as_view(), name='cbvdelete'),
]
