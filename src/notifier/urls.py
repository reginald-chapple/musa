from django.urls import include, path

from . import views

urlpatterns = [
    path('notifications/', include(([
        path('', views.notifications, name='notifications'),
        path('test/', views.test, name='test'),
    ], 'notifications'))),
]