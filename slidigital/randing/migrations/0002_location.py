# Generated by Django 4.2 on 2023-04-09 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sido', models.CharField(max_length=200)),
                ('gugun', models.CharField(max_length=200)),
            ],
        ),
    ]
