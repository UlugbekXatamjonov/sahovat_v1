# Generated by Django 4.0.5 on 2022-07-23 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0006_tashkilot_created_by_tashkilot_faoliyat_turi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tashkilot',
            name='ish_orni',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name="Tashkilot yaratgan ish o'rni"),
        ),
        migrations.AlterField(
            model_name='tashkilot',
            name='loyiha',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Tashkilot loyihalari soni'),
        ),
    ]
