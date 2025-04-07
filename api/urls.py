from django.urls import path
from .views import restfulAPI

urlpatterns = [
    path('', restfulAPI.as_view()),
    path('create/',restfulAPI.as_view()),
    path('update/<int:id>',restfulAPI.as_view()),
    path('delete/',restfulAPI.as_view()),
]
