# Generated by Django 2.2.6 on 2019-10-28 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PropertySale', '0004_apartmentmodel_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartmentmodel',
            name='Other_expences',
        ),
    ]