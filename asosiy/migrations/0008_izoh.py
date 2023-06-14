# Generated by Django 4.2.1 on 2023-06-13 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
        ('asosiy', '0007_mahsulot_mavjud'),
    ]

    operations = [
        migrations.CreateModel(
            name='Izoh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matn', models.TextField()),
                ('sana', models.DateField()),
                ('baho', models.CharField(choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')], max_length=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.account')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
            ],
        ),
    ]
