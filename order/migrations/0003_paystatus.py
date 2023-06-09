# Generated by Django 4.1.7 on 2023-04-30 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0002_payhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='paystatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30, verbose_name='Email')),
                ('ORDERID', models.CharField(max_length=30, verbose_name='ORDER ID')),
                ('amount', models.CharField(max_length=30, verbose_name='AMOUNT')),
                ('STATUS', models.CharField(default='process', max_length=12, verbose_name='STATUS')),
                ('TXNDATE', models.DateTimeField(default=django.utils.timezone.now, verbose_name='TXN DATE')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_paytm', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
