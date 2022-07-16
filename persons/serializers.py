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



class Tash_FaoliyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tash_Faoliyat
        fields = ('__all__')

class TashkilotSerializer(serializers.ModelSerializer):
    tashkilot_faoliyat = Tash_FaoliyatSerializer(many=True)
    class Meta:
        model = Tashkilot
        fields = ('__all__')





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
    class Meta:
        model = Yordam
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

    # tashkilot = YordamSerializer(many=True, read_only=True)
    # tashkilot = YordamSerializer(write_only=True)
    # tashkilot = YordamSerializer(many=True, read_only=True)
    # name = serializers.SerializerMethodField()


    class Meta:
        model = Person
        fields = ('parent','mfy','ism','familya','sharif','slug','tsana','jins','passport','jshir','phone1',\
            'phone2','vafot_etgan','manzil','created_by','created_at','status','objects','active', \

            # viloyat, tuman, mfy infos
            'mfy_id','mfy_tuman','mfy_sektor','mfy_shaxs','mfy_name','mfy_slug','mfy_status',\
            'tuman_id','tuman_viloyat','tuman_sektor','tuman_shaxs','tuman_name','tuman_slug','tuman_status',\
            'viloyat_id','viloyat_name','viloyat_slug','viloyat_status',\

            'family_info','ishli_person','ishsiz_person','person_qaror','person_yordam',\
            'person_photo','person_fayl',\
            )

    # def create(self, validated_data):
    #     tashkilot_data = validated_data.pop('tashkilot')
    #     Tashkilot.objects.create(**tashkilot_data)
    #     return super().create(validated_data)
            
    # def get_name(self, Tashkilot):
    #     name = Tashkilot.objects.all()
    #     return TashkilotSerializer(name, many=True).data




class Temirdaftar(serializers.ModelSerializer):
    parent = FamilySerializer()

    class Meta:
        model = Person
        fields = ('parent','mfy','ism','familya','sharif','slug','tsana','jins','passport','jshir','phone1',\
            'phone2','manzil','created_by','created_at','status','objects','active','parent')



# class LikeSerializer(serializers.ModelSerializer):
#     book = BookSerializer(write_only=True)

#     class Meta:
#         model = Like 
#         fields = '__all__'

#     def create(self, validated_data):
#         book_data = validated_data.pop('book')
#         Book.objects.create(**book_data)
#         return super().create(validated_data)


    # class AccountSerializer (serializers.ModelSerializer):
        
    #         class Meta:
    #             fields = ('id', 'amount', 'name', 'account_type', 'customer_id', 'bank_id')
    #             model = Account
        
        
    # class CustomerSerializer (serializers.ModelSerializer):
    #     accounts_items = serializers.SerializerMethodField()

    #     class Meta:
    #         fields = ('id', 'user', 'first_name', 'last_name', 'phone', 'email', 'rank', 'bank_id', 'accounts_items')
    #         model = Customer

    #     def get_accounts_items(self, obj):
    #         customer_account_query = models.Account.objects.filter(
    #             customer_id=obj.id)
    #         serializer = AccountSerializer(customer_account_query, many=True)

    #         return serializer.data



class TestSerializer(serializers.ModelSerializer):
    tashkilot = YordamSerializer(read_only=True)

    class Meta:
        model = Person
        fields = ('parent','mfy','ism','familya','sharif','slug','tsana','jins','passport','jshir','phone1',\
            'phone2','vafot_etgan','manzil','created_by','created_at','status',

            'tashkilot')


    # def create(self, validated_data):
    #     tashkilot_data = validated_data.pop('tashkilot')
    #     Tashkilot.objects.create(**tashkilot_data)
    #     return super().create(validated_data)