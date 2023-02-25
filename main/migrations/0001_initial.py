# Generated by Django 4.1.7 on 2023-02-25 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dis', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('uniqueID', models.CharField(blank=True, max_length=10)),
                ('img', models.TextField()),
            ],
        ),
    ]