# Generated by Django 2.1 on 2019-10-01 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiting', '0004_remove_hr_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hr',
            name='statue',
            field=models.PositiveIntegerField(choices=[(1, '未登陆'), (0, '已登录')], default=1, verbose_name='状态'),
        ),
    ]
