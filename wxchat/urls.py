# -*-coding:utf-8-*-
from wxchat.api.views import UpdateLossView

__author__ = 'malxin'

from django.conf.urls import url
from django.views.generic import TemplateView

from wxchat.views import doginstitution, DoginstitutionAdd, DogFemaleDetailView, DogInstitutionDetailView, dogBreedNav, \
    dogAdoptNav, dogTradeNav, showMyQRCode, showQRCode, myScore, PetWorldView, createLongQRCode, ContactUsView, \
    DogSaleDelView
from wxchat.views import DogAdoptDetailView, dogadoptAdd, DogdeliveryAdd, DogdeliveryDetailView, FreshmanDetailView, \
    dogOrder, orderSuccess, DogpayNotify, DogPayOrderView, orderList
from wxchat.views import wechat, createMenu, deleteMenu, getMenu, getUserinfo, redirectUrl, auth2, \
    authlist, dogLoss, dogLossAdd,  DogLossDetailView, dogBreedAdd, dogBreed, DogBreedDetailView, \
    DogOwnerDetailView, dogOwnerAdd, dogAdopt, dogBuyAdd, DogBuyDetailView, DogSaleDetailView, dogSaleAdd
from wxchat.views import freshman, dogTrade, updateUserinfo, petWorld, dogIndex, dogLossNav, myInfo, payList, \
    getPayInfo, orderRefund, PasswordView

urlpatterns = [

    url(r'^$', wechat),  # 微信入口

    url(r'^menu/$', TemplateView.as_view(template_name='wxchat/index.html')),  # 菜单操作
    url(r'^createmenu/$', createMenu),
    url(r'^getmenu/$', getMenu),
    url(r'^delmenu/$', deleteMenu),

    url(r'^redirect/(?P<item>[\w-]+)/$', redirectUrl),

    # 用户信息
    url(r'^getuserinfo/$', getUserinfo),

    # 寻狗寻主人
    url(r'^dogloss/$', dogLoss, name='dog-loss'),
    url(r'^doglossadd/$', dogLossAdd, name='dog-loss-add'),
    url(r'^doglossdetail/(?P<pk>\d+)/$', DogLossDetailView.as_view(), name='dog-loss-detail'),
    url(r'^dogowneradd/$', dogOwnerAdd, name='dog-owner-add'),
    url(r'^dogownerdetail/(?P<pk>\d+)/$', DogOwnerDetailView.as_view(), name='dog-owner-detail'),
    url(r'^doglossnav/$', dogLossNav, name='dog-loss-nav'),

    # 宠物领养和送养
    url(r'^dogadopt/$', dogAdopt, name='dog-adoption'),
    url(r'^dogadoptadd/$', dogadoptAdd, name='dog-adopt-add'),
    url(r'^dogadoptdetail/(?P<pk>\d+)/$', DogAdoptDetailView.as_view(), name='dog-adopt-detail'),
    url(r'^dogadoptnav/$', dogAdoptNav, name='dog-adopt-nav'),

    url(r'^dogdeliveryadd/$', DogdeliveryAdd, name='dog-delivery-add'),
    url(r'^dogdeliverydetail/(?P<pk>\d+)/$', DogdeliveryDetailView.as_view(), name='dog-delivery-detail'),

    # 配种
    url(r'^dogbreed/$', dogBreed, name='dog-breed'),
    url(r'^dogbreedadd/$', dogBreedAdd, name='dog-breed-add'),
    url(r'^dogbreeddetail/(?P<pk>\d+)/$', DogBreedDetailView.as_view(), name='dog-breed-detail'),
    url(r'^dogfemaledetail/(?P<pk>\d+)/$', DogFemaleDetailView.as_view(), name='dog-female-detail'),


    #狗粮订单
    url(r'^dogorder/$', dogOrder, name='dog-order'),
    # url(r'^pay/dogcreateorder$', CreateOrder.as_view(), name='dog-create-order'), #创建订单
    url(r'^pay/dogpayorder$', DogPayOrderView.as_view(), name='dog-pay-order'), #支付订单
    url(r'^pay/dogwxnotify/$', DogpayNotify, name='dog-pay-notify'), #订单回调
    url(r'^pay/ordersuccess/$', orderSuccess, name='order-success'),
    url(r'^pay/orderlist$', orderList, name='order-list'),
    url(r'^pay/refund/$', orderRefund, name='order-Refund'),
    url(r'^dogbreednav/$', dogBreedNav, name='dog-breed-nav'),

    # 新手学堂
    url(r'^freshman/$', freshman, name='fresh-man'),
    url(r'^freshmandetail/(?P<pk>\d+)/$', FreshmanDetailView.as_view(), name='dog-freshman-detail'),

    # 加盟宠物医疗机构
    url(r'^doginstitution/$', doginstitution, name='dog-institution'),
    url(r'^doginstitutionadd/$', DoginstitutionAdd, name='dog-institution-add'),
    url(r'^doginstitutiondetail/(?P<pk>\d+)/$', DogInstitutionDetailView.as_view(), name='dog-inst-detail'),

    # 宠物求购
    url(r'^dogtrade/$', dogTrade, name='dog-trade'),
    url(r'^dogbuyadd/$', dogBuyAdd, name='dog-buy-add'),
    url(r'^dogbuydetail/(?P<pk>\d+)/$', DogBuyDetailView.as_view(), name='dog-buy-detail'),
    # 宠物销售
    url(r'^dogsaleadd/$', dogSaleAdd, name='dog-sale-add'),
    url(r'^dogsaledetail/(?P<pk>\d+)/$', DogSaleDetailView.as_view(), name='dog-sale-detail'),
    url(r'^dogsaledel/(?P<pk>\d+)/$', DogSaleDelView.as_view(), name='dog-sale-del'),
    url(r'^dogtradnav/$', dogTradeNav, name='dog-trade-nav'),
    # 宠物出售

    #宠物乐园
    url(r'^petworld/$', petWorld,name='pets-world'),
    url(r'^petworlddetail/$', PetWorldView.as_view(), name='pet-world-detail'),

     #首页
    url(r'^dogindex/$', dogIndex,name='dog-index'),

    #我的
    url(r'^myinfo/$', myInfo,name='my-info'),
    url(r'^contactus/$', ContactUsView.as_view(), name='contact-us'),

    #微信支付
    url(r'^pay/paylist$', payList,name='pay-list'),
    url(r'^pay/payinfo/$', getPayInfo,name='pay-info'),


    #显示我的二维码
    url(r'^showmyqr/(?P<is_member>\d+)/(?P<img_url>.+)/$', showMyQRCode, name='my-qrcode-image'),
    url(r'^myqrcode/$', showQRCode, name='my-qrcode'),
    url(r'^myscore/$', myScore, name='my-score'),
    url(r'^longqrcode/$', createLongQRCode, name='long-qrcode'),

    # 网页授权测试
    url(r'^auth2/$', auth2),
    url(r'^authlist/$', authlist),

    url(r'^updateuserinfo/$', updateUserinfo),
    url(r'^password/$', PasswordView.as_view(), name='password-change'),
    url(r'^wxerror/$', TemplateView.as_view(template_name='wxchat/wxerror.html'), name='wx-error'),

]
