# Generated by Django 3.0 on 2020-02-08 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Item'),
            preserve_default=False,
        ),
    ]