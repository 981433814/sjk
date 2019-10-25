# Generated by Django 2.2.6 on 2019-10-21 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiting', '0010_detail_hr'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='city',
            field=models.CharField(default='广州市', max_length=3, verbose_name='城市'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='province',
            field=models.CharField(default='广东省', max_length=10, verbose_name='省份'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='salary',
            field=models.IntegerField(choices=[(0, '1000-3000'), (1, '3000-5000'), (2, '5000-7000'), (3, '7000-以上')], default=0, verbose_name='工资等级'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='school',
            field=models.CharField(default='北京理工大学珠海学院', max_length=20, verbose_name='学校'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='specialty',
            field=models.CharField(default='信息系统与信息管理', max_length=20, verbose_name='专业'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='station',
            field=models.CharField(default='无', max_length=10, verbose_name='岗位'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='hr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiting.Hr', verbose_name='发布人'),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('statue', models.PositiveIntegerField(choices=[(1, '投递成功'), (2, '简历被查看'), (3, '待沟通'), (4, '邀请面试'), (5, '已录用'), (6, '不合适')], default=1, verbose_name='状态')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiting.Applicant', verbose_name='应聘者')),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiting.Detail', verbose_name='文章')),
                ('hr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiting.Hr', verbose_name='招聘者')),
            ],
        ),
    ]