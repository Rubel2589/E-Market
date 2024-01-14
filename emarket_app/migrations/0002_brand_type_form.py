# Generated by Django 2.2.1 on 2020-06-10 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emarket_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='brand_type_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brand_location', models.CharField(max_length=200)),
                ('brand_description', models.TextField()),
                ('brand_image', models.ImageField(upload_to='brand_image')),
            ],
        ),
    ]
