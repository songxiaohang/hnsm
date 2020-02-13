# Generated by Django 3.0.1 on 2020-02-12 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200211_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='unit',
            field=models.CharField(max_length=16, null=True, verbose_name='楼号'),
        ),
        migrations.AlterField(
            model_name='floor',
            name='floor',
            field=models.CharField(max_length=16, null=True, verbose_name='楼层'),
        ),
        migrations.AlterField(
            model_name='roomnum',
            name='room',
            field=models.CharField(max_length=16, null=True, verbose_name='房间号'),
        ),
        migrations.AlterField(
            model_name='school',
            name='school',
            field=models.CharField(max_length=64, null=True, verbose_name='学校名称'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='floor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Floor'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gonghao',
            field=models.CharField(blank=True, max_length=31, null=True, verbose_name='工号'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.RoomNum'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.School'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Building'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]