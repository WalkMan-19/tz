from rest_framework import serializers

from market.models import BaseModel, Product, Contact, BusinessUnit


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ContactCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUnit
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUnit
        fields = '__all__'


class BaseModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = '__all__'
        read_only_fields = ['id']


class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = '__all__'
        read_only_fields = ['id', 'duty']
