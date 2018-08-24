#-*-coding:utf-8-*-
from django.conf.urls import url

__author__ = 'malixin'

from .views import GoodsListAPIView, CountAPIView, CreateShopCartAPIView, GoodsTypeListAPIView, ShopCartView, ScoresLimitAPIView

urlpatterns = [
    url(r'^goodslist/$', GoodsListAPIView.as_view(), name='goods-list'),
    url(r'^ordercartcount/$', CountAPIView.as_view(), name='order-cart-count'),
    url(r'^addshopcart/$', CreateShopCartAPIView.as_view(), name='shop-cart-add'),
    url(r'^goodstype/$', GoodsTypeListAPIView.as_view(), name='goods-type-list'),
    url(r'^shopcart/$', ShopCartView.as_view(), name='shop-cart'),
    url(r'^scoreslimit/$', ScoresLimitAPIView.as_view(), name='scores-limit'),

]

