# Generated by Django 2.2.1 on 2019-05-23 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_delete_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('slug', models.SlugField(blank=True)),
                ('prev_img', models.ImageField(blank=True, upload_to='')),
                ('prev_text', models.TextField(blank=True)),
                ('detail_img', models.ImageField(blank=True, upload_to='')),
                ('detail_text', models.TextField(blank=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Category')),
            ],
        ),
    ]
