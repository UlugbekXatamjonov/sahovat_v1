from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


JINS = (
    ('erkak','Erkak'),
    ('ayol','Ayol'),
)


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="myuser")
    jins = models.CharField(max_length=100, choices=JINS, verbose_name='Jins')
    tsana = models.DateField(auto_now_add=False)
    user_photo = models.ImageField(upload_to='admin_rasmi/%Y/%m/%d/', verbose_name='Admin rasmi', null=True, blank=True)
    viloyat = models.CharField(max_length=50, verbose_name='Viloyat')
    tuman = models.CharField(max_length=50, verbose_name='Tuman')
    address = models.CharField(max_length=250, verbose_name='Manzil')
    phone1 = PhoneNumberField(verbose_name='Telefon raqam')
    # phone2 = PhoneNumberField(verbose_name='Telefon raqam 2', blank=True, null=True)
    passport = models.CharField(max_length=15, verbose_name='Passport seria raqami')
    # iib = models.CharField(max_length=250, verbose_name='Passport bergan IIB')
    work_place = models.CharField(max_length=200, verbose_name="Ish joyi", blank=True, null=True)
    position = models.CharField(max_length=100, verbose_name="Lavozim", blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="createdby")
    created_at = models.DateField(auto_now_add=False)


    def __str__(self):
        return self.user.first_name






