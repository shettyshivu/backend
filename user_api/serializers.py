from rest_framework import serializers
from .models import company,investor

class companySerializer(serializers.ModelSerializer):
    class Meta:
        model = company
        fields = '__all__'



class investorSerializer(serializers.ModelSerializer):
    class Meta:
        model = investor
        fields = '__all__'