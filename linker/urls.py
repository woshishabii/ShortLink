from django.urls import path

from . import views

app_name = 'linker'

urlpatterns = [
    path('', views.index, name='index'),
    # path('test/redirect/', views.redirect_test, name='test_redirect'),
    path('r/<str:lid>/', views.redirect_url, name='redirect'),
    path('new_link/', views.new_link, name='new_link'),
]
