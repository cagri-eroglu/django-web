# Generated by Django 3.1.5 on 2022-11-03 14:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_yazilarmodel_resim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yazilarmodel',
            name='icerik',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
