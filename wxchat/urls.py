# -*-coding:utf-8-*-
__author__ = 'malxin'

from django.conf.urls import url
from django.views.generic import TemplateView

from wxchat.views import doginstitution, DoginstitutionAdd,DogFemaleDetailView
from wxchat.views import DogAdoptDetailView, dogadoptAdd, DogdeliveryAdd,DogdeliveryDetailView,FreshmanDetailView
from wxchat.views import wechat,createMenu, deleteMenu, getMenu, getUserinfo, redirectUrl, auth2, \
    authlist, dogLoss,dogLossAdd, createTestData,DogLossDetailView,dogBreedAdd,dogBreed,DogBreedDetailView,\
    DogOwnerDetailView, dogOwnerAdd,dogAdopt,dogBuyAdd,DogBuyDetailView, DogSaleDetailView, dogSaleAdd
from wxchat.views import freshman,dogTrade,updateUserinfo,shareAction



urlpatterns = [

    url(r'^$', wechat),  # 微信入口

    url(r'^menu/$', TemplateView.as_view(template_name='index.html')),  # 菜单操作
    url(r'^createmenu/$', createMenu),
    url(r'^getmenu/$', getMenu),
    url(r'^delmenu/$', deleteMenu),

    url(r'^redirect/(?P<item>[\w-]+)$', redirectUrl),

    # 用户信息
    url(r'^getuserinfo/$', getUserinfo),

    # 寻狗寻主人
    url(r'^dogloss/$', dogLoss, name='dog-loss'),
    url(r'^doglossadd/$', dogLossAdd, name='dog-loss-add'),
    url(r'^doglossdetail/(?P<pk>\d+)$', DogLossDetailView.as_view(), name='dog-loss-detail'),
    url(r'^dogowneradd/$', dogOwnerAdd, name='dog-owner-add'),
    url(r'^dogownerdetail/(?P<pk>\d+)$', DogOwnerDetailView.as_view(), name='dog-owner-detail'),

    # 宠物领养和送养
    url(r'^dogadopt/$', dogAdopt, name='dog-adoption'),
    url(r'^dogadoptadd/$', dogadoptAdd, name='dog-adopt-add'),
    url(r'^dogadoptdetail/(?P<pk>\d+)$', DogAdoptDetailView.as_view(), name='dog-adopt-detail'),

    url(r'^dogdeliveryadd/$', DogdeliveryAdd, name='dog-delivery-add'),
    url(r'^dogdeliverydetail/(?P<pk>\d+)$', DogdeliveryDetailView.as_view(), name='dog-delivery-detail'),

    # 配种
    url(r'^dogbreed/$', dogBreed, name='dog-breed'),
    url(r'^dogbreedadd/$', dogBreedAdd, name='dog-breed-add'),
    url(r'^dogbreeddetail/(?P<pk>\d+)$', DogBreedDetailView.as_view(), name='dog-breed-detail'),
    url(r'^dogfemaledetail/(?P<pk>\d+)$', DogFemaleDetailView.as_view(), name='dog-female-detail'),

    # 新手学堂
    url(r'^freshman/$', freshman, name='fresh-man'),
    url(r'^freshmandetail/(?P<pk>\d+)$', FreshmanDetailView.as_view(), name='dog-freshman-detail'),

    # 加盟宠物医疗机构
    url(r'^doginstitution/$', doginstitution, name='dog-institution'),
    url(r'^doginstitutionadd/$', DoginstitutionAdd, name='dog-institution-add'),

    # 宠物求购
    url(r'^dogtrade/$', dogTrade, name='dog-trade'),
    url(r'^dogbuyadd/$', dogBuyAdd, name='dog-buy-add'),
    url(r'^dogbuydetail/(?P<pk>\d+)$', DogBuyDetailView.as_view(), name='dog-buy-detail'),
    # 宠物销售
    url(r'^dogsaleadd/$', dogSaleAdd, name='dog-sale-add'),
    url(r'^dogsaledetail/(?P<pk>\d+)$', DogSaleDetailView.as_view(), name='dog-sale-detail'),
    # 宠物出售

    #分享
    url(r'^dogshare/$', shareAction,name='dog-share'),

    # 网页授权测试
    url(r'^auth2/$', auth2),
    url(r'^authlist/$', authlist),
    url(r'^createdata/$', createTestData),
    url(r'^updateuserinfo/$', updateUserinfo),
]
