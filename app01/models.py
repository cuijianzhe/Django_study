from django.db import models

# Create your models here.
#  ORM相关的稚嫩个写到这个文件夹中，写的别的文件夹中Django找不到

class UserInfo(models.Model):
    id = models.AutoField(primary_key=) #创建一个自增的主键字段
    name = models.CharField(null=False,max_length=20)  #创建一个varchar(20)的类型的不为空的字段

