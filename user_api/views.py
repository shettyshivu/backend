from .serializers import companySerializer, investorSerializer
from .models import company, investor
from rest_framework import generics

class companyList(generics.ListCreateAPIView):
    queryset = company.objects.all()
    serializer_class = companySerializer

class companyDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = company.objects.all()
    serializer_class = companySerializer


class investorList(generics.ListCreateAPIView):
    queryset = investor.objects.all()
    serializer_class = investorSerializer

class investDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = investor.objects.all()
    serializer_class = investorSerializer