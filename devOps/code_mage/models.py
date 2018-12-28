from django.db import models

# Create your models here.

class code_user(models.Model):
    userID = models.AutoField(primary_key=True, verbose_name='用户ID')
    userName = models.CharField(max_length=50, verbose_name='Git用户名')
    userEmail = models.EmailField(verbose_name='用户邮箱')
    userPassword = models.CharField(max_length=50, verbose_name='用户Git密码')

class code_info(models.Model):
    userID = models.AutoField(primary_key=True, verbose_name='用户ID')
    userName = models.CharField(max_length=50, verbose_name='Git用户名')
    verNO = models.CharField(max_length=20, db_index=True, verbose_name="版本号")
    fileList = models.TextField(max_length=500, verbose_name='发布文件列表')
    TSDate = models.DateTimeField(verbose_name='测试环境发布时间')
    OSDate = models.DateTimeField(verbose_name='正式环境发布时间')
    TSStatus = models.IntegerField(verbose_name='测试环境发布状态')
    OSStatus = models.IntegerField(verbose_name='正式环境发布状态')
    RBStatus = models.IntegerField(verbose_name='回滚状态')

