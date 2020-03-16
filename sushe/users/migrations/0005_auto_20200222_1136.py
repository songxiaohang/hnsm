# Generated by Django 3.0.1 on 2020-02-22 03:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200212_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='floor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Floor', verbose_name='楼层'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.RoomNum', verbose_name='房间号'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.School', verbose_name='学校'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Building', verbose_name='楼号'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
    ]
