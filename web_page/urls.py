from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
     path('yolov8_tracking/', views.yolov8_tracking, name='yolov8_tracking'),
    path('object_tracked/', views.object_tracked, name='object_tracked'),   
    path('windows_tracking/',views.windows_tracking,name='windows_tracking'), 
    path('noise_tracking/',views.noise_tracking,name='noise_tracking'),
    path('noise_plot/', views.noise_plot, name='noise_plot'),
    path('head_eye_tracking/',views.head_eye_tracking,name='head_eye_tracking'),
    # path('detect_windows/', views.detect_windows, name= 'detect_windows'),

   
]
