# Generated by Django 3.2.4 on 2021-06-20 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210621_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='/static/img/blog/slider1.jpg', upload_to=''),
        ),
    ]