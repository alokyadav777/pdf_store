# Generated by Django 2.0.6 on 2018-06-15 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_sessionclass_login_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionclass',
            name='login_status',
            field=models.CharField(max_length=5),
        ),
    ]
