# Generated by Django 3.2.4 on 2021-06-25 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_blog_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.CharField(default='Jun 25, 2021', max_length=30),
        ),
    ]