# Generated by Django 4.0.5 on 2022-07-16 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_family_bandlar_soni_alter_family_ishsizlar_soni'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='vafot_etgan_soni',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Vafot etgan soni'),
        ),
        migrations.AlterField(
            model_name='family',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_info', to='persons.person'),
        ),
        migrations.AlterField(
            model_name='fayl',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_fayl', to='persons.person'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_photo', to='persons.person'),
        ),
        migrations.AlterField(
            model_name='qaror',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_qaror', to='persons.person'),
        ),
        migrations.AlterField(
            model_name='yordam',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_yordam', to='persons.person'),
        ),
    ]
