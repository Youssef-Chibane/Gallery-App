# Generated by Django 5.1.4 on 2024-12-09 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_image_description_alter_image_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='Others', max_length=100),
        ),
    ]