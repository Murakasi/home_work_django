from django.urls import path
from . import views

urlpatterns = [
    path('books', views.review_list, name='api')
]