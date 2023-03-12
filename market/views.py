from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated

from market.models import BaseModel, Product, Contact, BusinessUnit
from market.permissions import CheckStatusPermission
from market.serializers import BaseModelCreateSerializer, BaseModelSerializer, \
    ProductSerializer, ContactCreateSerializer, ContactSerializer, CompanyCreateSerializer, CompanySerializer


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, CheckStatusPermission]


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, CheckStatusPermission]


class ProductView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, CheckStatusPermission]


class ContactCreateView(generics.CreateAPIView):
    serializer_class = ContactCreateSerializer
    permission_classes = [IsAuthenticated, CheckStatusPermission]


class ContactListView(generics.ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [IsAuthenticated, CheckStatusPermission]


class ContactView(generics.RetrieveUpdateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [IsAuthenticated, CheckStatusPermission]


class CompanyCreateView(generics.CreateAPIView):
    serializer_class = CompanyCreateSerializer
    permission_classes = [IsAuthenticated, CheckStatusPermission]


class CompanyListView(generics.ListAPIView):
    serializer_class = CompanySerializer
    queryset = BusinessUnit.objects.all()
    permission_classes = [IsAuthenticated, CheckStatusPermission]


class CompanyView(generics.RetrieveUpdateAPIView):
    serializer_class = CompanySerializer
    queryset = BusinessUnit.objects.all()
    permission_classes = [IsAuthenticated, CheckStatusPermission]


class BaseModelCreateView(generics.CreateAPIView):
    serializer_class = BaseModelCreateSerializer
    permission_classes = [IsAuthenticated, CheckStatusPermission]


class BaseModelListView(generics.ListAPIView):
    queryset = BaseModel.objects.all()
    serializer_class = BaseModelSerializer
    permission_classes = [IsAuthenticated, CheckStatusPermission]
    filter_backends = [
        filters.OrderingFilter,
    ]
    ordering = ['contacts__country']


class BaseModelView(generics.RetrieveUpdateAPIView):
    queryset = BaseModel.objects.all()
    serializer_class = BaseModelSerializer
    permission_classes = [IsAuthenticated, CheckStatusPermission]
