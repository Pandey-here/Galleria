# Generated by Django 4.0.4 on 2022-05-19 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_customer_desc_alter_customer_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='desc',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]