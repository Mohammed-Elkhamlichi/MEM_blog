# Generated by Django 3.1 on 2020-11-16 07:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20201116_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
