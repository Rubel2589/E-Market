# Generated by Django 2.2.1 on 2020-06-17 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emarket_app', '0021_auto_20200615_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_details',
            name='order_id',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
