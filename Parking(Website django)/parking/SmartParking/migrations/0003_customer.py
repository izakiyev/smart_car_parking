# Generated by Django 3.0.5 on 2022-05-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartParking', '0002_auto_20220516_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('time', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
