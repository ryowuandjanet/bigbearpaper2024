# Generated by Django 4.2.5 on 2023-09-12 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_remove_orderitem_remark_cart_remark'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='remark',
            field=models.TextField(blank=True, null=True),
        ),
    ]
