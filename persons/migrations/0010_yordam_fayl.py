# Generated by Django 4.0.5 on 2022-07-30 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0009_person_tuman'),
    ]

    operations = [
        migrations.AddField(
            model_name='yordam',
            name='fayl',
            field=models.FileField(default=1, upload_to='yordam_fayli/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
