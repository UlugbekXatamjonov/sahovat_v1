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

    def get_queryset(self):
        return Viloyat.active.filter()


class ViloyatDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Viloyat.active.all()
    serializer_class = ViloyatSerializer

    def get_queryset(self):
        return Viloyat.active.filter()

# <------------  Detail ga slug orqali kirish uchun ------------------------->
    lookup_fields = ['slug','pk']
# <------------  Detail ga slug orqali kirish uchun ------------------------->



class TumanList(ListCreateAPIView):
    queryset = Tuman.active.all()
    serializer_class = TumanSerializer

    def get_queryset(self):
        return Tuman.active.filter()

class TumanDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Tuman.active.all()
    serializer_class = TumanSerializer
    lookup_fields = ['slug','pk']

    def get_queryset(self):
        return Tuman.active.filter()


class MFYList(ListCreateAPIView):
    queryset = MFY.active.all()
    serializer_class = MFYSerializer

    def get_queryset(self):
        return MFY.active.filter()

class MFYDetail(RetrieveUpdateDestroyAPIView):
    queryset = MFY.active.all()
    serializer_class = MFYSerializer
    lookup_fields = ['slug','pk']

    def get_queryset(self):
        return MFY.active.filter()




class PersonList(ListCreateAPIView):
    queryset = Person.active.all()
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.active.filter()

    

class PersonDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Person.active.all()
    serializer_class = PersonSerializer
    lookup_fields = ['slug','pk']

    def get_queryset(self):
        return Person.active.filter()


class PhotoList(ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get_queryset(self):
        return Photo.active.filter()

class PhotoDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    lookup_fields = ['slug','pk']

    def get_queryset(self):
        return Photo.active.filter()


class FaylList(ListCreateAPIView):
    queryset = Fayl.active.all()
    serializer_class = FaylSerializer

    def get_queryset(self):
        return Fayl.active.filter()

class FaylDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Fayl.active.all()
    serializer_class = FaylSerializer
    lookup_fields = ['slug','pk']

    def get_queryset(self):
        return Fayl.active.filter()


class FamilyList(ListCreateAPIView):
    queryset = Family.active.all()
    serializer_class = FamilySerializer

    def get_queryset(self):
        return Family.active.filter()

    
class FamilyDetail( RetrieveUpdateDestroyAPIView):
    queryset = Family.active.all()
    serializer_class = FamilySerializer
    lookup_fields = ['slug','pk']

    def get_queryset(self):
        return Family.active.filter()

    

class TashkilotList(ListCreateAPIView):
    queryset = Tashkilot.objects.all()
    serializer_class = TashkilotSerializer

    def get_queryset(self):
        return Tashkilot.active.filter()

    
class TashkilotDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Tashkilot.objects.all()
    serializer_class = TashkilotSerializer
    lookup_fields = ['slug','pk']

    def get_queryset(self):
        return Tashkilot.active.filter()


class TashkilotSeeList(ListCreateAPIView):
    queryset = Tashkilot.objects.all()
    serializer_class = TashkilotSeeSerializer

    def get_queryset(self):
        return Tashkilot.active.filter()

    
class TashkilotSeeDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Tashkilot.objects.all()
    serializer_class = TashkilotSeeSerializer
    lookup_fields = ['slug','pk']

    def get_queryset(self):
        return Tashkilot.active.filter()

    

class IshliList(ListCreateAPIView):
    queryset = Ishli.active.all()
    serializer_class = IshliSerializer

    def get_queryset(self):
        return Ishli.active.filter()

    

class IshliDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Ishli.active.all()
    serializer_class = IshliSerializer
    lookup_fields = ['slug','pk']

    def get_queryset(self):
        return Ishli.active.filter()

    


class IshsizList(ListCreateAPIView):
    queryset = Ishsiz.active.all()
    serializer_class = IshsizSerializer

    def get_queryset(self):
        return Ishsiz.active.filter()

    

class IshsizDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Ishsiz.active.all()
    serializer_class = IshsizSerializer
    lookup_fields = ['slug','pk']

    def get_queryset(self):
        return Ishsiz.active.filter()

    


class QarorList(ListCreateAPIView):
    queryset = Qaror.active.all()
    serializer_class = QarorSerializer

    def get_queryset(self):
        return Qaror.active.filter()

    

class QarorDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Qaror.active.all()
    serializer_class = QarorSerializer
    lookup_fields = ['slug','pk']

    def get_queryset(self):
        return Qaror.active.filter()

    
class YordamList(ListCreateAPIView):
    queryset = Yordam.active.all()
    serializer_class =YordamSerializer

    def get_queryset(self):
        return Yordam.active.filter()

    

class YordamDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Yordam.active.all()
    serializer_class =YordamSerializer 
    lookup_fields = ['slug','pk']

    def get_queryset(self):
        return Yordam.active.filter()

    


class KompleksList(ListCreateAPIView):
    queryset = Kompleks.active.all()
    serializer_class =KompleksSerializer

    def get_queryset(self):
        return Kompleks.active.filter() 

class KompleksDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Kompleks.active.all()
    serializer_class =KompleksSerializer 
    lookup_fields = ['pk']

    def get_queryset(self):
        return Kompleks.active.filter()


