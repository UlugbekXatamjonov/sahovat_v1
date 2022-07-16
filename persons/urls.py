from django.urls import path
from .views import *

urlpatterns = [
	path('viloyat/<slug:slug>/<int:pk>/', ViloyatDetail.as_view()),
	path('viloyat/', ViloyatList.as_view()),

	path('tuman/<slug:slug>/<int:pk>/', TumanDetail.as_view()),
	path('tuman/', TumanList.as_view()),

	path('mfy/<slug:slug>/<int:pk>/', MFYDetail.as_view()),
	path('mfy/', MFYList.as_view()),

	path('person/<slug:slug>/<int:pk>/', PersonDetail.as_view(), name='person_detail'),
	path('person/', PersonList.as_view()),

	path('photo/<slug:slug>/<int:pk>/', PhotoDetail.as_view()),
	path('photo/', PhotoList.as_view()),

	path('fayl/<slug:slug>/<int:pk>/', FaylDetail.as_view()),
	path('fayl/', FaylList.as_view()),

	path('family/<slug:slug>/<int:pk>/', FamilyDetail.as_view()),
	path('family/', FamilyList.as_view()),	

	path('tashkilot/<slug:slug>/<int:pk>/', TashkilotDetail.as_view()),
	path('tashkilot/', TashkilotList.as_view()),

	path('tash-faoliyat/<slug:slug>/<int:pk>/', Tash_FaoliyatDetail.as_view()),
	path('tash-faoliyat/', Tash_FaoliyatList.as_view()),

	path('ishli/<slug:slug>/<int:pk>/', IshliDetail.as_view()),
	path('ishli/', IshliList.as_view()),

	path('ishsiz/<slug:slug>/<int:pk>/', IshsizDetail.as_view()),
	path('ishsiz/', IshsizList.as_view()),

	path('qaror/<slug:slug>/<int:pk>/', QarorDetail.as_view()),
	path('qaror/', QarorList.as_view()),

	path('yordam/<slug:slug>/<int:pk>/', YordamDetail.as_view()),
	path('yordam/', YordamList.as_view()),
	

	path('all/<int:pk>/', AllSerializerDetailView.as_view()),
	path('all/', AllSerializerListView.as_view()),
	
	
	path('temir/', TemirdaftarList.as_view()),
	
	 
	

]
