from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Viloyat)
admin.site.register(Kompleks)

@admin.register(Tuman)
class TumanAdmin(admin.ModelAdmin):
	list_display = ('name','viloyat','sektor')
	list_filter = ('viloyat','sektor')

@admin.register(MFY)
class MFYAdmin(admin.ModelAdmin):
	list_display = ('name','tuman','sektor')
	list_filter = ('tuman','sektor')

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	list_display = ('ism','parent','mfy','familya','passport','jshir',\
	'created_at','created_by')
	list_filter = ('mfy','created_at','created_by')
	search_fields = ('ism','familya','manzil')

# @admin.register(Photo)
# class PhotoAdmin(admin.ModelAdmin):
# 	list_display = ('person','photo','created_at')
# 	list_filter = ('created_at',)

# @admin.register(Fayl)
# class FaylAdmin(admin.ModelAdmin):
# 	list_display = ('person','fayl','created_at')
# 	list_filter = ('fayl','created_at')

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
	list_display = ('parent','toifa','created_by','created_at')
	list_filter = ('toifa','created_by','created_at')

@admin.register(Tashkilot)
class TashkilotAdmin(admin.ModelAdmin):
	list_display = ('name','faoliyat_turi','stir',)
	list_filter = ('created_at','status')

@admin.register(Ishli)
class IshliAdmin(admin.ModelAdmin):
	list_display = ('person','tashkilot','created_at','created_by')
	list_filter = ('created_at','created_by')

@admin.register(Ishsiz)
class IshsizAdmin(admin.ModelAdmin):
	list_display = ('person','created_at','created_by')
	list_filter = ('created_at','created_by')

@admin.register(Qaror)
class QarorAdmin(admin.ModelAdmin):
	list_display = ('person','qaror_raqami','created_at','created_by')
	list_filter = ('created_at','created_by')

@admin.register(Yordam)
class YordamAdmin(admin.ModelAdmin):
	list_display = ('person','korxona','created_at','created_by')
	list_filter = ('created_at','created_by')
