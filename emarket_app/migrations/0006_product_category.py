# Generated by Django 2.2.1 on 2020-06-11 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emarket_app', '0005_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
