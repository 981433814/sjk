# Generated by Django 2.2.6 on 2019-10-16 11:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiting', '0007_auto_20191011_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='company',
            field=models.CharField(default=2, max_length=55, verbose_name='公司'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detail',
            name='company_address',
            field=models.CharField(default=2, max_length=55, verbose_name='公司地址'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detail',
            name='education',
            field=models.IntegerField(choices=[(0, '不限制'), (1, '本科生'), (2, '硕士'), (3, '博士')], default=0, verbose_name='学历'),
        ),
        migrations.AddField(
            model_name='detail',
            name='experience',
            field=models.IntegerField(choices=[(0, '无经验'), (1, '一年以上'), (2, '两年以上'), (3, '三年以上')], default=0, verbose_name='工作经验'),
        ),
        migrations.AddField(
            model_name='detail',
            name='post',
            field=models.CharField(default=2, max_length=20, verbose_name='岗位'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detail',
            name='salary',
            field=models.IntegerField(choices=[(0, '1000-3000'), (1, '3000-5000'), (2, '5000-7000'), (3, '7000-以上')], default=0, verbose_name='工资等级'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='context',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='detail',
            name='statue',
            field=models.PositiveIntegerField(choices=[(1, '未审核'), (0, '已审核')], default=1, verbose_name='状态'),
        ),
    ]