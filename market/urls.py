from django.urls import path

from market import views

urlpatterns = [
    path('product/create', views.ProductCreateView.as_view()),
    path('product/list', views.ProductListView.as_view()),
    path('product/<pk>', views.ProductView.as_view()),

    path('contact/create', views.ContactCreateView.as_view()),
    path('contact/list', views.ContactListView.as_view()),
    path('contact/<pk>', views.ContactView.as_view()),

    path('company/create', views.CompanyCreateView.as_view()),
    path('company/list', views.CompanyListView.as_view()),
    path('company/<pk>', views.CompanyView.as_view()),

    path('supplier/create', views.BaseModelCreateView.as_view()),
    path('supplier/list', views.BaseModelListView.as_view()),
    path('supplier/<pk>', views.BaseModelView.as_view()),
]
