# Generated by Django 4.1.5 on 2023-01-18 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0009_whtomasfisicasdetails_acepted_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="productvariant",
            name="ean",
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name="productvariant",
            name="upc",
            field=models.CharField(
                blank=True,
                help_text="The UPC code of the Product variant",
                max_length=13,
                null=True,
            ),
        ),
    ]
