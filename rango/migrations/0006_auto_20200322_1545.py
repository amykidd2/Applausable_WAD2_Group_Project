# Generated by Django 2.2.3 on 2020-03-22 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20200321_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='artistImage',
            field=models.ImageField(default='artist.jpg', upload_to='C:\\Users\\euanw\\Workspace\\Applausable_WAD2_Group_Project\\media'),
        ),
    ]
