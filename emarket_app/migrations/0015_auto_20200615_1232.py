# Generated by Django 2.2.1 on 2020-06-15 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emarket_app', '0014_cart_details_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_info',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
