# Generated by Django 4.2.4 on 2023-11-18 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_alter_order_price_alter_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
