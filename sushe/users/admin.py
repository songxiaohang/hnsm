from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import User, School, Floor, Building, RoomNum, UserInfo


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'last_login')


admin.site.register([School, Floor, Building, RoomNum])


@admin.register(UserInfo)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'gonghao', 'phone', 'school', 'unit', 'floor', 'room')