from .serializers import companySerializer
from .models import company
from rest_framework import generics

class companyList(generics.ListCreateAPIView):
    queryset = company.objects.all()
    serializer_class = companySerializer

class companyDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = company.objects.all()
    serializer_class = companySerializer