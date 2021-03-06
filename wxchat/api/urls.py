#-*-coding:utf-8-*-
from django.conf.urls import url
from django.views.decorators.cache import cache_page

__author__ = 'malixin'

from .views import (
    DoginfoListAPIView,
    DoginfoCreateAPIView,
    DogLossListAPIView,
    DogLossDetailAPIView,
    DogbreedListAPIView,
    DogBreedDetailAPIView,
    DogOwnerListAPIView,
    DogadoptListAPIView,
    DogdeliveryListAPIView,
    DogdeliveryDeliveryAPIView,
    DogBuyListAPIView,
    DogSaleListAPIView,
    DogFreshmanListAPIView,
    SwiperImageListAPIView,
    DogInstitutionListAPIView,
    AreaCodeListAPIView,
    MyInfoListAPIView,
    UpdateLossView,
    UpdateOwnerView)

urlpatterns = [
    url(r'^doginfolist/$', DoginfoListAPIView.as_view(), name='doginfolist'),
    url(r'^doginfocreate/$', DoginfoCreateAPIView.as_view(), name='doginfocreate'),
    url(r'^doglosslist/$', DogLossListAPIView.as_view(), name='dog-loss-list'),
    url(r'^dogbreedlist/$', DogbreedListAPIView.as_view(), name='dog-breed-list'),
    url(r'^doglossdetail/(?P<pk>\d+)/$', DogLossDetailAPIView.as_view(), name='api-dog-loss-detail'),
    url(r'^dogbreeddetail/(?P<pk>\d+)/$', DogBreedDetailAPIView.as_view(), name='api-dog-breed-detail'),
    url(r'^dogownerlist/$', DogOwnerListAPIView.as_view(), name='dog-owner-list'),
    url(r'^dogadoptlist/$', DogadoptListAPIView.as_view(), name='dog-adopt-list'),
    url(r'^dogdeliverylist/$', DogdeliveryListAPIView.as_view(), name='dog-delivery-list'),
    url(r'^dogdeliverydetail/(?P<pk>\d+)/$', DogdeliveryDeliveryAPIView.as_view(), name='api-dog-delivery-detail'),
    url(r'^dogbuylist/$', DogBuyListAPIView.as_view(), name='dog-buy-list'),
    url(r'^dogsalelist/$', DogSaleListAPIView.as_view(), name='dog-sale-list'),
    url(r'^freshmanlist/$', DogFreshmanListAPIView.as_view(), name='dog-freshman-list'),
    url(r'^swiperimagelist/$',  cache_page(60 * 15)(SwiperImageListAPIView.as_view()), name='swiper-image-list'),
    url(r'^doginstitutionlist/$', DogInstitutionListAPIView.as_view(), name='dog-institution-list'),
    url(r'^arealist/$', AreaCodeListAPIView.as_view(), name='area-code-list'),
    url(r'^myinfolist/$', MyInfoListAPIView.as_view(), name='my-info-list'),
     #更新找到标志
    url(r'^updateloss/(?P<pk>\d+)/$', UpdateLossView.as_view(),name='update-loss'),
    url(r'^updateowner/(?P<pk>\d+)/$', UpdateOwnerView.as_view(),name='update-owner'),


]

