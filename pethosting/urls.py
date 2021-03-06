#-*-coding:utf-8-*-
__author__ = 'malxin'


from django.conf.urls import url
from django.views.generic import TemplateView
from pethosting.views import PetInfoListView, HostingOrderView, HostingCalcPrice, HostingDepositSearchView, \
   HostingOrderListView, \
   HostingContractView, HostContractPageView, HostingOrderDetailView, HostContractDetailView, HostQrCodeView, \
   HostQrCodeShowView, HostQrCodeAckView, HostingRoomUpdateView

urlpatterns = [

   url(r'^petinfolist/$', PetInfoListView.as_view(), name='hosting-pet-list'),   # 宠物列表
   url(r'^hostingorder/$', HostingOrderView.as_view(), name='hosting-order'),   # 宠物托管订单
   url(r'^hostpricecalc/$', HostingCalcPrice.as_view(), name='hosting-calc-price'),   # 宠物托管价格计算
   url(r'^hostdepositsearch/$', HostingDepositSearchView.as_view(), name='hosting-deposit-search'),   # 托管备用金查询
   url(r'^hostingorderlist/$', HostingOrderListView.as_view(), name='hosting-order-list'),   # 托管订单列表
   url(r'^hostingcontract/$', HostingContractView.as_view(), name='hosting-contract'),
   url(r'^hostcontractpage/(?P<id>\d+)/$', HostContractPageView.as_view(), name='hosting-contract-page'),
   url(r'^hostingorderdetail/(?P<id>\d+)/$', HostingOrderDetailView.as_view(), name='hosting-order-detail'),
   url(r'^hostcontractdetail/$', HostContractDetailView.as_view(), name='hosting-contract-detail'),
   url(r'^qrcode/$', HostQrCodeView.as_view(), name='hosting-qrcode'), # 确认二维码
   url(r'^qrcodeshow/$', HostQrCodeShowView.as_view(), name='hosting-qrcode-show'), # 确认二维码
   url(r'^qrcodeack/$', HostQrCodeAckView.as_view(), name='hosting-qrcode-ack'), # 确认二维码
   url(r'^hostrupdateroom/$', HostingRoomUpdateView.as_view(), name='hosting-room-update'),
   url(r'^hostingknow/$', TemplateView.as_view(template_name="pethosting/hosting_know.html"), name='hosting-know'),  # 托管须知
]
