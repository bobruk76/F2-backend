# Generated by Django 3.1.3 on 2020-11-24 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]