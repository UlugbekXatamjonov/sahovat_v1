# Generated by Django 4.0.5 on 2022-07-30 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0008_tashkilot_mfy_tashkilot_tuman'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='tuman',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='person_tuman', to='persons.tuman', verbose_name='Tuman'),
            preserve_default=False,
        ),
    ]
