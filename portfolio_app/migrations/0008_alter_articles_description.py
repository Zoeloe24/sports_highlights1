# Generated by Django 4.1.7 on 2023-04-05 06:49

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0007_articles_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='description',
            field=django_quill.fields.QuillField(default=''),
            preserve_default=False,
        ),
    ]
