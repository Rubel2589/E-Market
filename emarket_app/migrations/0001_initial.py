# Generated by Django 2.2.1 on 2020-06-08 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('brand_type', models.CharField(max_length=250)),
                ('subject', models.CharField(max_length=250)),
                ('contact', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]
