# Generated by Django 4.2.1 on 2023-06-13 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0005_mahsulot_yetkazish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahsulot',
            name='yetkazish',
            field=models.CharField(max_length=60),
        ),
    ]
