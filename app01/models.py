from django.db import models

# Create your models here.
#  ORM相关的只能写到这个文件夹中，写的别的文件夹中Django找不到

class UserInfo(models.Model):   #对应数据库中的数据表
    id = models.AutoField(primary_key=True) #创建一个自增的主键字段
    name = models.CharField(null=False,max_length=32)  #创建一个varchar(32)的类型的不为空的字段

