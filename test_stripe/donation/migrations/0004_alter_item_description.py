# Generated by Django 4.0.6 on 2022-11-29 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0003_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(),
        ),
    ]