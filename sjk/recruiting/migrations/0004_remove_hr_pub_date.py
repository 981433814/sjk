# Generated by Django 2.1 on 2019-09-30 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruiting', '0003_hr_h_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hr',
            name='pub_date',
        ),
    ]