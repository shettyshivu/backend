from .serializers import companySerializer
from .models import Company
from rest_framework import generics

class companyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = companySerializer

class companyDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = companySerializer