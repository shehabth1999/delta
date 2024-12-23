# Generated by Django 5.1.4 on 2024-12-19 21:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.CreateModel(
            name='Image2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='products.product')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]