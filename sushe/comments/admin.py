from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    # 列表可显示的字段
    list_display = ['name', 'post', 'created_time']
    fields = ['name', 'text', 'post']


admin.site.register(Comment, CommentAdmin)