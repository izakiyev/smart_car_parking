# Generated by Django 3.2.9 on 2022-03-29 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('places', models.IntegerField()),
                ('free_places', models.IntegerField()),
                ('order_a', models.TextField(blank=True, null=True)),
                ('order_b', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
