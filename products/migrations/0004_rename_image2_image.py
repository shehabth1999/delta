# Generated by Django 5.1.4 on 2024-12-19 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_images_image2_delete_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image2',
            new_name='Image',
        ),
    ]