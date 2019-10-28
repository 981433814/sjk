from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index1', views.index1, name='index1'),
    path('/<int:user>', views.index, name='index'),
    path('login', views.login, name='login'),
    path('hlogin', views.hlogin, name='hlogin'),
    path('register', views.register, name='register'),
    path('test', views.forms),
    path('detail/<int:post>/', views.detail, name='detail'),
    path('useradmin', views.hradmin, name='useradmin'),
    path('send', views.send, name='send'),
    path('logout', views.logout, name='logout'),
    path('logout_hr', views.logout_hr, name='logout_hr'),
    path('apadmin', views.apadmin, name='apadmin'),
    # path('<int:detail_id>/detail/', views.detail, name='detail')
]
