# Generated by Django 2.2.3 on 2020-03-18 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.CharField(default='Review', max_length=248),
        ),
    ]
