# Generated by Django 4.2.4 on 2023-11-17 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_product_category_product_sub_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField()),
            ],
        ),
    ]
