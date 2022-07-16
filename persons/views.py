from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from .models import *
from .serializers import *
from django.shortcuts import  get_object_or_404

# ---------------------- Product -----------------------
# class ToifaList(ListCreateAPIView):
#     queryset = Toifa.objects.all()
#     serializer_class = ToifaSerializer
    
# class ToifaDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Toifa.objects.all()
#     serializer_class = ToifaSerializer


class AllSerializerListView(ListCreateAPIView):
    queryset = Person.active.all()
    serializer_class = AllSerializer

class AllSerializerDetailView( RetrieveAPIView):
    queryset = Person.active.all()
    serializer_class = AllSerializer
    # lookup_fields = ['slug','pk']


# <------------  Detail ga slug orqali kirish uchun ------------------------->
class MultipleFieldLookupMixin:
    def get_object(self):
        queryset = self.get_queryset()           
        filter = {}
        for slug in self.lookup_fields:
            if self.kwargs[slug]: 
                filter[slug] = self.kwargs[slug]
        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj
# <------------  Detail ga slug orqali kirish uchun ------------------------->


class ViloyatList(ListCreateAPIView):
    queryset = Viloyat.active.all()
    serializer_class = ViloyatSerializer

class ViloyatDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Viloyat.active.all()
    serializer_class = ViloyatSerializer

# <------------  Detail ga slug orqali kirish uchun ------------------------->
    lookup_fields = ['slug','pk']
# <------------  Detail ga slug orqali kirish uchun ------------------------->



class TumanList(ListCreateAPIView):
    queryset = Tuman.active.all()
    serializer_class = TumanSerializer

class TumanDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Tuman.active.all()
    serializer_class = TumanSerializer
    lookup_fields = ['slug','pk']


class MFYList(ListCreateAPIView):
    queryset = MFY.active.all()
    serializer_class = MFYSerializer

class MFYDetail(RetrieveUpdateDestroyAPIView):
    queryset = MFY.active.all()
    serializer_class = MFYSerializer
    lookup_fields = ['slug','pk']


class PersonList(ListCreateAPIView):
    queryset = Person.active.all()
    serializer_class = PersonSerializer

class PersonDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Person.active.all()
    serializer_class = PersonSerializer
    lookup_fields = ['slug','pk']


class PhotoList(ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    lookup_fields = ['slug','pk']


class FaylList(ListCreateAPIView):
    queryset = Fayl.active.all()
    serializer_class = FaylSerializer

class FaylDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Fayl.active.all()
    serializer_class = FaylSerializer
    lookup_fields = ['slug','pk']


class FamilyList(ListCreateAPIView):
    queryset = Family.active.all()
    serializer_class = FamilySerializer

class FamilyDetail( RetrieveUpdateDestroyAPIView):
    queryset = Family.active.all()
    serializer_class = FamilySerializer
    lookup_fields = ['slug','pk']


class TashkilotList(ListCreateAPIView):
    queryset = Tashkilot.objects.all()
    serializer_class = TashkilotSerializer

class TashkilotDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Tashkilot.objects.all()
    serializer_class = TashkilotSerializer
    lookup_fields = ['slug','pk']


class Tash_FaoliyatList(ListCreateAPIView):
    queryset = Tash_Faoliyat.active.all()
    serializer_class = Tash_FaoliyatSerializer

class Tash_FaoliyatDetail(RetrieveUpdateDestroyAPIView):
    queryset = Tash_Faoliyat.active.all()
    serializer_class = Tash_FaoliyatSerializer


class IshliList(ListCreateAPIView):
    queryset = Ishli.active.all()
    serializer_class = IshliSerializer

class IshliDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Ishli.active.all()
    serializer_class = IshliSerializer
    lookup_fields = ['slug','pk']


class IshsizList(ListCreateAPIView):
    queryset = Ishsiz.active.all()
    serializer_class = IshsizSerializer

class IshsizDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Ishsiz.active.all()
    serializer_class = IshsizSerializer
    lookup_fields = ['slug','pk']


class QarorList(ListCreateAPIView):
    queryset = Qaror.active.all()
    serializer_class = QarorSerializer

class QarorDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Qaror.active.all()
    serializer_class = QarorSerializer
    lookup_fields = ['slug','pk']


class YordamList(ListCreateAPIView):
    queryset = Yordam.active.all()
    serializer_class =YordamSerializer 

class YordamDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Yordam.active.all()
    serializer_class =YordamSerializer 
    lookup_fields = ['slug','pk']


# class List(ListCreateAPIView):
#     queryset = .active.all()
#     serializer_class = 

# class Detail(RetrieveUpdateDestroyAPIView):
#     queryset = .active.all()
#     serializer_class = 



class TemirdaftarList(ListCreateAPIView):
    queryset = Person.active.all()
    serializer_class = Temirdaftar

class TemirdaftarDetail(RetrieveUpdateDestroyAPIView):
    queryset = Person.active.all()
    serializer_class = Temirdaftar


