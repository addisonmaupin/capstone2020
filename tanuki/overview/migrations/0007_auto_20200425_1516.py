# Generated by Django 3.0.3 on 2020-04-25 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0006_auto_20200425_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additem',
            name='dateDisplayed',
            field=models.DateField(auto_now_add=True),
        ),
    ]