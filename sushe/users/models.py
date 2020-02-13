from django.db import models
from django.contrib.auth.models import AbstractUser
# AbstractUser 自带属性：username,first_name, last_name, password, email, last_login,
#                           is_superuser,is_staff, is_active, date_joined
from phonenumber_field.modelfields import PhoneNumberField


class School(models.Model):
    # id = models.IntegerField(primary_key=True, null=True)
    school = models.CharField('学校名称', max_length=64, null=True)

    class Meta:
        verbose_name = "添加学校"
        verbose_name_plural = verbose_name

    def __str__(self):
            return self.school


class Building(models.Model):
    # id = models.IntegerField(primary_key=True, null=True)
    unit = models.CharField('楼号', max_length=16, null=True)

    class Meta:
        verbose_name = "添加楼号"
        verbose_name_plural = verbose_name

    def __str__(self):
            return self.unit


class Floor(models.Model):
    # id = models.IntegerField(primary_key=True, null=True)
    floor = models.CharField('楼层', max_length=16, null=True)

    class Meta:
        verbose_name = "添加楼层"
        verbose_name_plural = verbose_name

    def __str__(self):
            return self.floor


class RoomNum(models.Model):
    # id = models.IntegerField(primary_key=True, null=True)
    room = models.CharField('房间号', max_length=16, null=True)

    class Meta:
        verbose_name = "添加宿舍"
        verbose_name_plural = verbose_name

    def __str__(self):
            return self.room


# 用户的数据库
class User(AbstractUser):
    # 用户密码
    password = models.CharField('密码', max_length=128)

    # 信息最近存储时间
    last_login = models.DateTimeField('最近登录时间', auto_now_add=True)

    class Meta:
        verbose_name = "用户注册信息"
        verbose_name_plural = verbose_name  # 指定模型的复数形式是什么,如果不指定Django会自动在模型名称后加一个’s’

    def __str__(self):
        return self.username


class UserInfo(models.Model):
    # 用户信
    # 息与注册信息一对一
    username = models.OneToOneField("User", on_delete=models.CASCADE, blank=True, null=True)

    # 用户电话
    phone = PhoneNumberField('手机号', blank=True, null=True)

    # 用户身份证号
    gonghao = models.CharField('工号', max_length=31, blank=True, null=True)

    # 绑定上面的学校
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)

    # 绑定宿舍单元,models.CASCADE是指当删除宿舍这个数据库时，用户中关于这个数据库的信息也一并删除。
    # black=True表示该数据允许为空
    unit = models.ForeignKey(Building, on_delete=models.CASCADE, blank=True, null=True)

    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, blank=True, null=True)

    room = models.ForeignKey(RoomNum, on_delete=models.CASCADE, blank=True, null=True)

    # 判断用户是否已完善信息
    is_perfect = models.IntegerField("信息是否完善", default=0)

    class Meta:
        verbose_name = "用户完善信息"
        verbose_name_plural = verbose_name

    def __str__(self):
            return self.gonghao