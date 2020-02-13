from django.contrib.auth.forms import UserCreationForm
from .models import User,UserInfo
from django import forms


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # 注册默认提供的信息只有用户名、密码、密码确认，要增加在fields里加入
        fields = ("username", "email")


class PerfectForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        # 指定表单需要显示的字段
        fields = ['username', 'phone', 'gonghao', 'school', 'is_perfect']
