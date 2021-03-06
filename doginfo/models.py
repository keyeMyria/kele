#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.urls import reverse
from easy_thumbnails.fields import ThumbnailerImageField

__author__ = 'yy'

from django.db import models
import datetime
from django.contrib.auth.models import User
import random
from ckeditor_uploader.fields import RichTextUploadingField
from dogtype.models import Dogtype
from easy_thumbnails.files import get_thumbnailer
from shopping.models import  TYPE_MAIL_STYLE, TYPE_SHOPPING_STATUS
now = datetime.datetime.now()
order_id = now.strftime("%Y%m%d%H%M%S") + 'B'

PAGE_TYPE_CHOICE = (
    (0, u'公'),
    (1, u'母'),
)

Vaccine_TYPE_CHOICE = (
    (0, u'否'),
    (1, u'是'),
)

PET_TYPE_CHOICE = (
    (0, u'狗狗'),
    (1, u'猫咪'),
)

bodytype_TYPE_CHOICE = (
    (0, u'大'),
    (1, u'中'),
    (2, u'小'),
)

TYPE_SEX_CHOICE = (
    (u'公', u'公'),
    (u'母', u'母'),
)

TYPE_RESULT_CHOICE = (
    (0, u'没找到'),
    (1, u'已找到'),
)


TYPE_FUNC_CHOICE = (
    (0,'增重'),
    (1,'减肥'),
)

ORDER_STATUS_CHOICE = (
    (0,'正常'),
    (1,'定制'),
)

PAY_STATUS_CHOICE = (
    (0,'已支付'),
    (1,'支付失败'),
)

TYPE_LEVEL_CHOICE = (
    (0,'低档'),
    (1,'中档'),
    (2,'高档'),
)

def defulfs():
    now = datetime.datetime.now()
    order_id = now.strftime("%Y%m%d%H%M%S") + 'B'
    return order_id


# 宠物简介
class Doginfo(models.Model):
    dog_code = models.CharField(verbose_name=u'宠物编号', max_length=20, default=defulfs)
    dog_name = models.CharField(verbose_name=u'宠物名称', max_length=50, )
    dog_birthday = models.DateField(verbose_name=u'出生日期', null=True, blank=True)
    dog_typeid = models.ForeignKey(Dogtype, verbose_name=u'品种', on_delete=models.CASCADE)
    dog_bodytype = models.IntegerField(verbose_name=u'宠物体型', default=0, choices=bodytype_TYPE_CHOICE)
    dog_picture = models.ImageField(verbose_name=u'宠物图片', upload_to='imgs', blank=True)
    dog_color = models.CharField(verbose_name=u'宠物颜色', max_length=10, blank=True)
    owner_name = models.CharField(verbose_name=u'主人姓名', max_length=20, blank=True)
    owner_address = models.CharField(verbose_name=u'主人地址', max_length=200, blank=True)
    owner_telephone = models.CharField(verbose_name=u'主人电话', max_length=50)
    owner_weixin = models.CharField(verbose_name=u'主人微信', max_length=50, blank=True)
    sterilization = models.IntegerField(verbose_name=u'是否绝育', default=0, choices=Vaccine_TYPE_CHOICE)
    dog_sex = models.IntegerField(verbose_name=u'性别', default=0, choices=PAGE_TYPE_CHOICE)
    Insect = models.DateField(verbose_name=u'驱虫日期', blank=True, null=True)
    vaccine = models.DateField(verbose_name=u'注射疫苗日期', blank=True, null=True)
    remarks = models.TextField(verbose_name=u'备注', max_length=1000, blank=True)
    click = models.IntegerField(verbose_name=u'阅读量', blank=True, null=True, default=0)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    class Meta:
        verbose_name = u"宠物简介"
        verbose_name_plural = u'宠物简介'

    def __str__(self):
        return self.dog_name


# 狗场简介
class Company(models.Model):
    name = models.CharField(verbose_name=u'狗场名称', max_length=100)
    telephone = models.CharField(verbose_name=u'电话', max_length=50, blank=True)
    phone = models.CharField(verbose_name=u'手机', max_length=50)
    email = models.EmailField(verbose_name=u'邮箱')
    case = models.ImageField(verbose_name=u'成功案例', upload_to='imgs', blank=True)
    dynamic = models.CharField(verbose_name=u'最新动态', max_length=200, blank=True)
    address = models.CharField(verbose_name=u'狗场地址', max_length=200, blank=True)
    profile = models.CharField(verbose_name=u'简介', max_length=1000, blank=True)
    remarks = RichTextUploadingField(verbose_name=u'备注', max_length=10000, blank=True)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    class Meta:
        verbose_name = u"公司简介"
        verbose_name_plural = u'公司简介'
        ordering = ['create_time']

    def __str__(self):
        return self.name


# 寻宠登记表
class DogLoss(models.Model):
    dog_name = models.CharField(verbose_name=u'宠物昵称', max_length=50)
    typeid = models.CharField(verbose_name=u'宠物品种',max_length=32)
    desc = models.CharField(verbose_name=u'宠物说明', max_length=100, blank=True)
    picture = ThumbnailerImageField(verbose_name=u'宠物图片', upload_to='loss/%Y%m%d/', blank=True,null=True,max_length=200)
    # picture = models.ImageField(verbose_name=u'宠物图片', upload_to='loss/%Y%m%d/', blank=True,null=True)
    lostplace = models.CharField(verbose_name=u'丢失地点', max_length=100, )
    lostdate = models.DateTimeField(verbose_name=u'丢失时间')
    ownername = models.CharField(verbose_name=u'主人姓名', max_length=20, null=True, blank=True)
    telephone = models.CharField(verbose_name=u'主人手机', max_length=50)
    age = models.IntegerField(verbose_name=u'宠物年龄',null=True,  blank=True)
    sex = models.CharField(verbose_name=u'宠物性别',max_length=10, null=True,blank=True, choices=TYPE_SEX_CHOICE,default='公')
    click = models.IntegerField(verbose_name=u'阅读量',blank=True,null=True,default=0)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    is_show = models.BooleanField(verbose_name=u'是否显示', default=True)
    result = models.IntegerField(verbose_name='当前状态',default=0,choices=TYPE_RESULT_CHOICE,null=True,blank=True)
    openid = models.CharField(verbose_name='唯一标识', max_length=120, null=True, blank=True)
    nickname = models.CharField(verbose_name='昵称', max_length=64, null=True, blank=True)

    class Meta:
        verbose_name = u"寻宠登记"
        verbose_name_plural = u'寻宠登记表'
        ordering = ['-create_time']

    def __str__(self):
        return self.dog_name

    def _getTitle(self):
        return '【寻宠】昵称:%s(%s)\n丢失地点:%s' % (self.dog_name, self.typeid, self.lostplace)

    title = property(_getTitle)

    def get_absolute_url(self):
        return reverse('dog-loss-detail', kwargs={'pk': self.id})

    def get_picture(self):
        if self.picture:
            print(self.picture.width,self.picture.height)
            # exif = self.picture._getexif()
            # print(exif)
            options = {'size': (1600, 1200), 'crop': True}
            thumburl = get_thumbnailer(self.picture).get_thumbnail(options).url
            return thumburl
        else:
            return  self.picture.url


# 寻宠主
class DogOwner(models.Model):
    typeid = models.CharField(verbose_name=u'宠物品种',max_length=32)
    desc = models.CharField(verbose_name=u'宠物说明', max_length=100, blank=True)
    picture = ThumbnailerImageField(verbose_name=u'宠物图片', upload_to='loss/%Y%m%d/', blank=True)
    # picture = models.ImageField(verbose_name=u'宠物图片', upload_to='loss/%Y%m%d/', blank=True)
    findplace = models.CharField(verbose_name=u'发现地点', max_length=100, )
    finddate = models.DateTimeField(verbose_name=u'发现时间')
    findname = models.CharField(verbose_name=u'联系人姓名', max_length=20, null=True, blank=True)
    telephone = models.CharField(verbose_name=u'联系电话', max_length=50)
    click = models.IntegerField(verbose_name=u'阅读量', blank=True, null=True, default=0)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    is_show = models.BooleanField(verbose_name=u'是否显示', default=True)
    result = models.IntegerField(verbose_name='当前状态',default=0,choices=TYPE_RESULT_CHOICE,null=True,blank=True)
    openid = models.CharField(verbose_name='唯一标识', max_length=120, null=True, blank=True)
    nickname = models.CharField(verbose_name='昵称', max_length=64, null=True, blank=True)

    class Meta:
        verbose_name = u"寻宠物主人"
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.typeid

    def _getTitle(self):
        return '【寻主人】品种:%s\n发现地点:%s' % (self.typeid, self.findplace)

    title = property(_getTitle)

    def get_absolute_url(self):
        return reverse('dog-owner-detail', kwargs={'pk': self.id})


#
# 宠物状况表
class DogStatus(models.Model):
    name = models.CharField(verbose_name=u'名称', max_length=64, db_index=True)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    sort = models.IntegerField(verbose_name='顺序', default=0, blank=True, null=True)
    suffix_name = models.CharField(verbose_name='后缀名',max_length=20, blank=True, default='')
    short_name = models.CharField(verbose_name='简称', max_length=20,blank=True, null=True)
    is_checkbox = models.BooleanField(verbose_name='是否多选', default=False, blank=True)

    class Meta:
        verbose_name = u"定制食品选项"
        verbose_name_plural = verbose_name
        ordering = ['sort']

    def __str__(self):
        return self.name

#
# 宠物状况分类表
class DogStatusType(models.Model):
    name = models.CharField(verbose_name=u'名称', max_length=64, )
    dogtype = models.ForeignKey(DogStatus, verbose_name=u'宠物基本情况', related_name='dogstatustype', on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    class Meta:
        verbose_name = u"定制食品分项"
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.name

#定制食品价格表
class FoodPrice(models.Model):
    name = models.CharField(verbose_name='价格名称', max_length=32, blank=True, null=True)
    price = models.DecimalField(verbose_name="价格(元)", max_digits=6, decimal_places=2, null=True, blank=True, default=0)
    create_time  = models.DateTimeField(verbose_name='创建时间', auto_now=True)

    class Meta:
        verbose_name = '定制食品价格表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 宠粮订单表
class DogOrder(models.Model):
    out_trade_no = models.CharField(verbose_name='订单号', max_length=32, default='')
    user_id = models.CharField(verbose_name='用户ID', max_length=64, null=True, blank=True)
    username = models.CharField(verbose_name='收货人姓名', max_length=64, null=True, blank=True)
    telnumber = models.CharField(verbose_name='联系电话', max_length=32, null=True, blank=True)
    postalcode = models.CharField(verbose_name='邮编', max_length=16, null=True, blank=True)
    detailinfo = models.CharField(verbose_name='详细收货地址', max_length=200, null=True, blank=True)
    total_fee = models.DecimalField(verbose_name='应收款',  max_digits=10, decimal_places=2,blank=True,null=True)
    cash_fee = models.DecimalField(verbose_name='实收款',  max_digits=10, decimal_places=2,blank=True,null=True)
    price = models.DecimalField(verbose_name='价格',  max_digits=6, decimal_places=2,blank=True,null=True)
    goods_nums = models.IntegerField(verbose_name='定制数量', blank=True , default=0)
    product_detail = models.CharField(verbose_name=u'商品定制内容', max_length=2000, blank=True)
    mailstyle = models.IntegerField(verbose_name='发货方式', blank=True , null=True, choices=TYPE_MAIL_STYLE)
    mail_cost = models.IntegerField(verbose_name='邮寄费用', blank=True, null=True, default=0)
    is_mail = models.BooleanField(verbose_name="是否发货", blank=True,  default=0)
    status = models.IntegerField(verbose_name='支付状态',default=0,choices=TYPE_SHOPPING_STATUS)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True,auto_now=False)
    pay_time = models.DateTimeField(verbose_name='支付时间', blank=True, null=True)
    transaction_id = models.CharField(verbose_name='微信支付订单号', max_length=32,null=True,blank=True)
    message = models.CharField(verbose_name='留言', max_length=400,null=True, blank=True)

    class Meta:
        verbose_name = u"定制食品订单"
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
         return '订单号 {}'.format(self.out_trade_no)

    def update_status_transaction_id(self,status,transaction_id, cash_fee,pay_time):
        self.status = status
        self.transaction_id = transaction_id
        self.cash_fee = cash_fee
        self.pay_time = pay_time
        self.save(update_fields=['status','transaction_id','cash_fee','pay_time'])

#狗粮订单选项
class DogOrderItem(models.Model):
    dogorder = models.ForeignKey(DogOrder, verbose_name='订单', on_delete=models.CASCADE)
    dog_status = models.ForeignKey(DogStatus, verbose_name='定制项目')
    dog_status_type = models.CharField(verbose_name='选项内容', max_length=64, blank=True, null=True)

    class Meta:
        verbose_name = u"宠粮定制选项"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.dog_status_type


# # 宠粮录入表
# class Dogfood(models.Model):
#     productname = models.CharField(verbose_name=u'产品名称', max_length=50, )
#     dog_brandid = models.ForeignKey(Dogbrand, verbose_name=u'品牌', on_delete=models.CASCADE)
#     prod_picture = models.ImageField(verbose_name=u'品牌图片', upload_to='imgs', blank=True)
#     dog_age = models.CharField(verbose_name=u'适用犬龄', max_length=20, blank=True)
#     sale_url = models.CharField(verbose_name=u'交易网址', max_length=50, blank=True)
#     food_models = models.CharField(verbose_name=u'规格', max_length=50, blank=True)
#     period = models.CharField(verbose_name=u'保质期', max_length=50, blank=True)
#     netweight = models.CharField(verbose_name=u'净含量', max_length=50, blank=True)
#     dog_desc = RichTextUploadingField(verbose_name=u'简介', max_length=2000)
#     prod_desc = RichTextUploadingField(verbose_name=u'产品介绍', max_length=2000)
#     click = models.IntegerField(verbose_name=u'阅读量', blank=True, null=True, default=0)
#     create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
#
#     class Meta:
#         verbose_name = u"宠粮录入"
#         verbose_name_plural = u'宠粮录入表'
#         ordering = ['-create_time']
#
#     def __str__(self):
#         return self.productname


# 宠物配种
class DogBreed(models.Model):
    name = models.CharField(verbose_name=u'宠物昵称', max_length=50)
    pet_class = models.IntegerField(verbose_name=u'宠物种类', choices=PET_TYPE_CHOICE, default=0)
    sex = models.CharField(verbose_name=u'宠物性别', max_length=10,choices=TYPE_SEX_CHOICE, null=True, blank=True)
    ages = models.CharField(verbose_name=u'狗龄', max_length=50 ,blank=True)
    birth =  models.DateField(verbose_name=u'出生日期',blank=True,null=True)
    typeid = models.CharField(verbose_name=u'宠物品种',max_length=32)
    desc = models.CharField(verbose_name=u'宠物说明', max_length=50,blank=True)
    picture = ThumbnailerImageField(verbose_name=u'宠物图片',  upload_to='breed', blank=True)
    price  = models.CharField(verbose_name=u'价格区间', max_length=100,blank=True)
    ownername = models.CharField(verbose_name=u'主人姓名', max_length=100,blank=True,null=True)
    telephone = models.CharField(verbose_name=u'主人电话', max_length=50 )
    click = models.IntegerField(verbose_name=u'阅读量',blank=True,null=True,default=0)
    showtime = models.DateTimeField(verbose_name=u'显示时间',blank=True,null=True)
    create_time = models.DateTimeField(verbose_name=u'添加时间', auto_now_add=True)
    is_show = models.BooleanField(verbose_name=u'是否显示', default=True)
    openid = models.CharField(verbose_name='唯一标识', max_length=120, null=True, blank=True)
    nickname = models.CharField(verbose_name='昵称', max_length=64, null=True, blank=True)

    class Meta:
        verbose_name = u"宠物相亲"
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.name


# 宠物领养Pet adoption
class DogAdoption(models.Model):
    name = models.CharField(verbose_name=u'领养人', max_length=50)
    telephone = models.CharField(verbose_name=u'电话', max_length=20)
    record = models.CharField(verbose_name='饲养记录', max_length=100, blank=True, null=True)
    requirement = models.CharField(verbose_name='对宠物要求', max_length=200)
    click = models.IntegerField(verbose_name=u'阅读量', blank=True, null=True, default=0)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    is_show = models.BooleanField(verbose_name=u'是否显示', default=True)
    openid = models.CharField(verbose_name='唯一标识', max_length=120, null=True, blank=True)
    nickname = models.CharField(verbose_name='昵称', max_length=64, null=True, blank=True)

    class Meta:
        verbose_name = u'宠物领养'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.name


# 宠物送养pet delivery

class DogDelivery(models.Model):
    name = models.CharField(verbose_name='宠物昵称',max_length=50)
    typeid = models.CharField(verbose_name=u'宠物品种',max_length=32)
    ages = models.CharField(verbose_name=u'宠物年龄', max_length=50 ,blank=True,null=True)
    sex = models.CharField(verbose_name=u'宠物性别', max_length=10,choices=TYPE_SEX_CHOICE,blank=True,null=True)
    desc = models.CharField(verbose_name=u'宠物说明', max_length=50,blank=True,null=True)
    picture = ThumbnailerImageField(verbose_name=u'宠物照片',  upload_to='delivery/%Y%m%d/', blank=True,null=True)
    ownername = models.CharField(verbose_name=u'宠物姓名', max_length=20,null=True,blank=True)
    telephone = models.CharField(verbose_name=u'联系方式', max_length=50 )
    click = models.IntegerField(verbose_name=u'阅读量',blank=True,null=True,default=0)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    is_show = models.BooleanField(verbose_name=u'是否显示', default=True)
    openid = models.CharField(verbose_name='唯一标识', max_length=120, null=True, blank=True)
    nickname = models.CharField(verbose_name='昵称', max_length=64, null=True, blank=True)

    class Meta:
        verbose_name = u'宠物送养'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.name


# 宠物求购
class DogBuy(models.Model):
    typeid = models.CharField(verbose_name=u'宠物品种',max_length=32)
    pet_class = models.IntegerField(verbose_name=u'宠物种类', choices=PET_TYPE_CHOICE, default=0)
    ages = models.CharField(verbose_name=u'年龄', max_length=50 ,blank=True,null=True)
    sex = models.CharField(verbose_name=u'性别', max_length=10,choices=TYPE_SEX_CHOICE,blank=True,null=True)
    price = models.CharField(verbose_name=u'价格区间', max_length=50,blank=True,null=True)
    buyname = models.CharField(verbose_name=u'姓名', max_length=20,null=True,blank=True)
    telephone = models.CharField(verbose_name=u'联系方式', max_length=50 )
    click = models.IntegerField(verbose_name=u'阅读量',blank=True,null=True,default=0)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    is_show = models.BooleanField(verbose_name=u'是否显示', default=True)
    openid = models.CharField(verbose_name='唯一标识', max_length=120, null=True, blank=True)
    nickname = models.CharField(verbose_name='昵称', max_length=64, null=True, blank=True)

    class Meta:
        verbose_name = u'宠物求购'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.typeid



# 宠物出售
class DogSale(models.Model):
    typeid = models.CharField(verbose_name=u'宠物品种',max_length=32)
    pet_class = models.IntegerField(verbose_name=u'宠物种类', choices=PET_TYPE_CHOICE, default=0)
    ages = models.CharField(verbose_name=u'年龄', max_length=50 ,blank=True,null=True,default='')
    sex = models.CharField(verbose_name=u'性别', max_length=10,choices=TYPE_SEX_CHOICE,blank=True,null=True)
    desc = models.CharField(verbose_name=u'特点', max_length=200,blank=True,null=True)
    picture = ThumbnailerImageField(verbose_name=u'照片',  upload_to='sale/%Y%m%d/', blank=True,null=True)
    price = models.CharField(verbose_name=u'价格区间', max_length=50,blank=True,null=True)
    ownername = models.CharField(verbose_name=u'主人姓名', max_length=20,null=True,blank=True)
    telephone = models.CharField(verbose_name=u'联系方式', max_length=50 )
    click = models.IntegerField(verbose_name=u'阅读量',blank=True,null=True,default=0)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    is_show = models.BooleanField(verbose_name=u'是否显示', default=True)
    openid = models.CharField(verbose_name='唯一标识', max_length=120, null=True, blank=True)
    nickname = models.CharField(verbose_name='昵称', max_length=64, null=True, blank=True)

    class Meta:
        verbose_name = u'宠物出售'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.typeid


# 训犬 行为纠正
class DogBehavior(models.Model):
    name = models.CharField(verbose_name=u'项目名称', max_length=50)
    price = models.CharField(verbose_name=u'价格', max_length=50)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    is_show = models.BooleanField(verbose_name=u'是否显示', default=True)
    openid = models.CharField(verbose_name='唯一标识', max_length=120, null=True, blank=True)

    class Meta:
        verbose_name = u'宠物行为纠正'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']


# 训犬 技能培训
class DogSkill(models.Model):
    name = models.CharField(verbose_name=u'项目名称', max_length=50)
    price = models.CharField(verbose_name=u'价格', max_length=50)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    is_show = models.BooleanField(verbose_name=u'是否显示', default=True)
    openid = models.CharField(verbose_name='唯一标识', max_length=120, null=True, blank=True)

    class Meta:
        verbose_name = u'宠物技能培训'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

# 新手课堂
class Freshman(models.Model):
    title = models.CharField(verbose_name=u'标题', max_length=50,blank=True, null=True)
    picture = ThumbnailerImageField(verbose_name=u'标题图片', upload_to='new/%Y%m%d/', blank=True, null=True)
    desc = models.CharField(verbose_name=u'简介', max_length=200)
    prod_desc = RichTextUploadingField(verbose_name=u'内容', max_length=2000)
    click = models.IntegerField(verbose_name=u'阅读量', blank=True, null=True, default=0)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    is_show = models.BooleanField(verbose_name=u'是否显示', default=True)
    user = models.ForeignKey(User,verbose_name='作者',on_delete=models.CASCADE,blank=True, null=True)

    class Meta:
        verbose_name = u'新手课堂'
        verbose_name_plural = verbose_name
        #ordering = ['-create_time']


# 加盟宠物医疗机构
class Doginstitution(models.Model):
    name = models.CharField(verbose_name=u'机构名称', max_length=50, null=True, blank=True)
    tel = models.CharField(verbose_name=u'联系电话', max_length=50)
    address = models.CharField(verbose_name=u'详细地址', max_length=500)
    province = models.CharField(verbose_name=u'所属省市区', max_length=50,null=True,blank=True,default='')
    picture = ThumbnailerImageField(verbose_name=u'机构图片',upload_to='hospital/%Y%m%d/',null=True,blank=True,default='')
    brief = models.CharField(verbose_name='机构简介',max_length=500,null=True,blank=True,default='')
    # city = models.CharField(verbose_name=u'所属市', max_length=50)
    # area = models.CharField(verbose_name=u'所属县区', max_length=50)
    # click = models.IntegerField(verbose_name=u'阅读量',blank=True,null=True,default=0)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    is_show = models.BooleanField(verbose_name=u'是否显示', default=True)
    openid = models.CharField(verbose_name='唯一标识', max_length=120, null=True, blank=True)


    class Meta:
        verbose_name = u'加盟宠物医疗机构'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def get_absolute_url(self):
        return  reverse('dog-inst-detail',kwargs={'pk':self.id})

class PetWorldType(models.Model):
    name = models.CharField(verbose_name="乐园类型", max_length=64)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name = u'乐园分类'
        verbose_name_plural = verbose_name



class PetWorld(models.Model):
    title = models.CharField(verbose_name=u'标题', max_length=120)
    worldtype = models.ForeignKey(PetWorldType, verbose_name = u'乐园类别', on_delete=models.CASCADE)
    content = RichTextUploadingField(verbose_name=u'内容介绍',null=True,blank=True)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    is_show = models.BooleanField(verbose_name=u'是否显示', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'乐园介绍'
        verbose_name_plural = verbose_name
