from django.urls import path
from . import views

urlpatterns = [
    path('Companies/', views.companyList.as_view()),
    path('Companies/<int:pk>/', views.companyDetails.as_view()),
]
