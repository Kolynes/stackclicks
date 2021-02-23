# Generated by Django 2.0.6 on 2021-02-20 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StackClicksApp', '0010_auto_20210218_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='withdrawalrequestmodel',
            name='processed',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='withdrawalrequestmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdrawals', to=settings.AUTH_USER_MODEL),
        ),
    ]