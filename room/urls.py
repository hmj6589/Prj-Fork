from django.urls import path
from . import views

urlpatterns = [
    path('', views.LectureroomList.as_view()),
    # path('<int:pk>/', views.)
]