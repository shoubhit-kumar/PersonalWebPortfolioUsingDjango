# Generated by Django 3.2.4 on 2021-06-20 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='/static/img/blog/slider1.jpg', upload_to='img/'),
        ),
    ]
