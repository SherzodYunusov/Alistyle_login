# Generated by Django 4.2.1 on 2023-06-13 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0004_alter_media_rasm'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahsulot',
            name='yetkazish',
            field=models.CharField(default=0, max_length=60),
        ),
    ]
