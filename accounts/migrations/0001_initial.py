# Generated by Django 4.0.5 on 2022-07-05 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jins', models.CharField(choices=[('erkak', 'Erkak'), ('ayol', 'Ayol')], max_length=100, verbose_name='Jins')),
                ('tsana', models.DateField()),
                ('user_photo', models.ImageField(blank=True, null=True, upload_to='admin_rasmi/%Y/%m/%d/', verbose_name='Admin rasmi')),
                ('viloyat', models.CharField(max_length=50, verbose_name='Viloyat')),
                ('tuman', models.CharField(max_length=50, verbose_name='Tuman')),
                ('address', models.CharField(max_length=250, verbose_name='Manzil')),
                ('phone1', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Telefon raqam')),
                ('passport', models.CharField(max_length=15, verbose_name='Passport seria raqami')),
                ('work_place', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ish joyi')),
                ('position', models.CharField(blank=True, max_length=100, null=True, verbose_name='Lavozim')),
                ('created_at', models.DateField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createdby', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='myuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
