# Generated by Django 2.2.1 on 2019-06-05 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_auto_20190605_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainpage',
            name='el_one',
        ),
        migrations.DeleteModel(
            name='MainSlider',
        ),
        migrations.DeleteModel(
            name='MainPage',
        ),
    ]