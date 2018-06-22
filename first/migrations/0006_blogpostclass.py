# Generated by Django 2.0.6 on 2018-06-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_auto_20180615_0557'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPostClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogId', models.IntegerField()),
                ('blogTitle', models.CharField(max_length=300)),
                ('blogDescription', models.CharField(max_length=100000)),
                ('blogPostDateTime', models.CharField(max_length=50)),
                ('blogCoverImage', models.CharField(max_length=1000000)),
                ('blogImage', models.CharField(max_length=1000000)),
            ],
        ),
    ]