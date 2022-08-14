from django.urls import path
from . import views

urlpatterns = [
    path('Companies/', views.companyList.as_view()),
    path('Companies/<int:pk>/', views.companyDetails.as_view()),
    path('Investors/', views.investorList.as_view()),
    path('Investors/<int:pk>/', views.investDetails.as_view()),
]
 