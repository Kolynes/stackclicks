# Generated by Django 2.0.6 on 2021-02-06 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StackClicksApp', '0003_auto_20210206_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
