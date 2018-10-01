from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello_name/',views.hello_name,name='hello_name'),
    path('times2/',views.times2,name= 'times2'),
    path('<int:num1>/<int:num2>/sum/', views.sum,name ="sum")
]