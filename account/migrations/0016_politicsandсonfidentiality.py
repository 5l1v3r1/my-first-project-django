# Generated by Django 2.2.1 on 2019-05-27 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoliticsAndСonfidentiality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
    ]
