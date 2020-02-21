from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    # 在admin中汉化名称
    verbose_name = '用户管理'
