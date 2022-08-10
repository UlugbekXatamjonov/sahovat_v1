from rest_framework import serializers
from .models import *


class ViloyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viloyat
        fields = ('__all__')


class TumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuman
        fields = ('__all__')


class MFYSerializer(serializers.ModelSerializer):
    class Meta:
        model = MFY
        fields = ('__all__')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('__all__')


class FaylSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fayl
        fields = ('__all__')


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ('__all__')



class TashkilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tashkilot
        fields = ('__all__')



class TashkilotSeeSerializer(serializers.ModelSerializer):
    tuman_id = serializers.CharField(source='mfy.tuman.id')
    tuman_viloyat = serializers.CharField(source='mfy.tuman.viloyat')
    tuman_sektor = serializers.CharField(source='mfy.tuman.sektor')
    tuman_shaxs = serializers.CharField(source='mfy.tuman.shaxs')
    tuman_name = serializers.CharField(source='mfy.tuman.name')
    tuman_slug = serializers.CharField(source='mfy.tuman.slug')
    tuman_status = serializers.CharField(source='mfy.tuman.status')

    mfy_id = serializers.CharField(source='mfy.id')
    mfy_tuman = serializers.CharField(source='mfy.tuman')
    mfy_sektor = serializers.CharField(source='mfy.sektor')
    mfy_shaxs = serializers.CharField(source='mfy.shaxs')
    mfy_name = serializers.CharField(source='mfy.name')
    mfy_slug = serializers.CharField(source='mfy.slug')
    mfy_status = serializers.CharField(source='mfy.status')

    class Meta:
        model = Tashkilot
        fields = ('mfy_id','mfy_tuman','mfy_sektor','mfy_shaxs','mfy_name','mfy_slug','mfy_status',\
            'tuman_id','tuman_viloyat','tuman_sektor','tuman_shaxs','tuman_name','tuman_slug','tuman_status',\
            'name','slug','faoliyat_turi','loyiha','ish_orni','created_at','created_by','status'
        )


class IshliSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ishli
        fields = ('__all__')


class IshsizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ishsiz
        fields = ('__all__')


class QarorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qaror
        fields = ('__all__')


class YordamSerializer(serializers.ModelSerializer):
    yordam_turi = serializers.StringRelatedField()

    class Meta:
        model = Yordam
        fields = ('id','person','slug','yordam_sanasi','korxona','vakil_fio','yuridik','phone',
            'summa','izoh','fayl','created_at','created_by','tekshirildi','status',
            'yordam_turi')



class KompleksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kompleks
        fields = ('__all__')


class AllSerializer(serializers.ModelSerializer):
    viloyat_id = serializers.CharField(source='mfy.tuman.viloyat.id')
    viloyat_name = serializers.CharField(source='mfy.tuman.viloyat.name')
    viloyat_slug = serializers.CharField(source='mfy.tuman.viloyat.slug')
    viloyat_status = serializers.CharField(source='mfy.tuman.viloyat.status')
    
    tuman_id = serializers.CharField(source='mfy.tuman.id')
    tuman_viloyat = serializers.CharField(source='mfy.tuman.viloyat')
    tuman_sektor = serializers.CharField(source='mfy.tuman.sektor')
    tuman_shaxs = serializers.CharField(source='mfy.tuman.shaxs')
    tuman_name = serializers.CharField(source='mfy.tuman.name')
    tuman_slug = serializers.CharField(source='mfy.tuman.slug')
    tuman_status = serializers.CharField(source='mfy.tuman.status')

    mfy_id = serializers.CharField(source='mfy.id')
    mfy_tuman = serializers.CharField(source='mfy.tuman')
    mfy_sektor = serializers.CharField(source='mfy.sektor')
    mfy_shaxs = serializers.CharField(source='mfy.shaxs')
    mfy_name = serializers.CharField(source='mfy.name')
    mfy_slug = serializers.CharField(source='mfy.slug')
    mfy_status = serializers.CharField(source='mfy.status')

    family_info = FamilySerializer(many=True, read_only=True)
    ishli_person = IshliSerializer(many=True, read_only=True)
    ishsiz_person = IshsizSerializer(many=True, read_only=True)
    person_qaror = QarorSerializer(many=True, read_only=True)
    person_yordam = YordamSerializer(many=True, read_only=True)
    person_photo = PhotoSerializer(many=True, read_only=True)
    person_fayl = FaylSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = ('id','parent','mfy','ism','familya','sharif','slug','tsana','jins','passport','jshir','phone1',\
            'phone2','vafot_etgan','manzil','created_by','created_at','status','objects','active', \

            'mfy_id','mfy_tuman','mfy_sektor','mfy_shaxs','mfy_name','mfy_slug','mfy_status',\
            'tuman_id','tuman_viloyat','tuman_sektor','tuman_shaxs','tuman_name','tuman_slug','tuman_status',\
            'viloyat_id','viloyat_name','viloyat_slug','viloyat_status',\

            'family_info','ishli_person','ishsiz_person','person_qaror','person_yordam',\
            'person_photo','person_fayl',\
            )




