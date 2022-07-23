from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from accounts.models import MyUser
from autoslug import AutoSlugField
# django-autoslug==1.9.8

# Create your models here.



STATUS = (
	('active','Active'),
	('arxiv','Arxiv'),
	('delete','Delete'),
)


TOIFA = (
	('muhtoj_oila','Muhtoj oila'),
	('band_oila', 'Bandligi taminlangan oila'),
	('muhtoj_emas_oila', "Muhtojlar ro'yhatidan chiqarilgan")
)

SEKTOR=(
	('1','1'),
	('2','2'),
	('3','3'),
	('4','4'),
)


JINS = (
	('erkak','Erkak'),
	('ayol','Ayol'),
)

IJTIMOIY_HOLAT = (
	('ogir_kasal',"Og'ir kasal"),
	('farzandi_bor_oila','5 va undan ortiq farzandi bor oila'),
	('boquvchisini_yoqotgan',"Boquvchisini yo'qotgan(beva ayollar)"),
	('boshqalar','Boshqalar'),
	('cheteldagi_daromadlari','Chet eldagi daromadlari'),
	('uzdagi_daromadlari',"O'zbekistondagi daromadlari"),
	('kam_taminlangan','Kam taminlangan(VMQ-44)'),
	('nogiron','Nogiron'),
	('yakka_yolgiz',"Yakka yolg'iz(Keksalar)"),
)


FAOLIYAT_TURI = (
	('oilaviy_tadbirkorlik',"Oilaviy tadbirkorlik"),
	('xunarmandchilik',"Xunarmandchilik"),
	('jamoat_ishlari',"Jamoat ishlari"),
	('sanoat_loyhalari',"Sanoat loyihalari"),
	('agrosanoat_loyihalari',"Agrosanoat loyihalari"),
	('kooperatsiya_asosida','Kooperatsiya asosida yer ajratish'),
	('takroriy_ekin','Takroriy ekin'),
	('qurilishda_ishlash','Qurilish obyektlarid ishlash'),
	('rasmiy_ozi_band_qilish',"Rasmiy o'zini o'zi band qilish(PQ-4742)"),
	('norasmiy_bandlik','Norasmiy bandlik(odam va yuk tashish xizmati, shaxsiy qurilishda quruvchi va h.k)'),
	('ishiga_qaytish',"O'zining ishiga qaytish(karantin yumshatilishi)"),
	('boshqa_ft',"Boshqa faoliyat turlari"),
)


EHTIYOJMAND_OILA = (
	('juda_muhtoj',"O'ta muhtoj oila"),
	('muhtoj',"Muhtoj oila"),
	('vaqtincha_muhtoj',"Vaqtincha muhtoj oila"),
)

YORDAM_TURI = (
	('oziq_ovqat',"Oziq-ovqat mahsulotlari etkazib berish"),
	('naqt_pul',"Naqt (yoki plastik kartochka) pul ko'rinishida"),
	('komunal_tolandi',"Komunal qarzi to'lab berildi(gaz, suv svet"),
	('dori_darmon',"Dori darmon yetkazib berildi"),
	('boshqa_yordam',"Ko'rsatilgan boshqa yordam"),
	('qoramol',"Chorva: qoramol"),
	('qoy',"Chorva: qo'y"),
	('echki',"Chorva: echki"),
	('parranda',"Chorva: parranda"),
	('quyon',"Chorva: quyon"),
	('asalari',"Chorva: asalari"),
	('pf_6038',"PF-6038 (30.07.2020)"),
	('vmf_346',"VMF-346 (29.07.2020)"),
	('pq_5204',"PQ-5204 (30.07.2021)"),
	('pq_4815',"PQ-4817 (26.08.2021)")
)

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='active')


class Viloyat(models.Model):
	name = models.CharField(max_length=50, verbose_name="Viloyat nomi")
	slug = AutoSlugField(populate_from='name')

	status = models.CharField(max_length=20, choices=STATUS, default='active')
	objects = models.Manager()
	active = ActiveManager()

	def __str__(self):
		return self.name
 

class Tuman(models.Model):
	viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE, related_name="tuman_viloyat", verbose_name="Viloyat nomi")
	sektor = models.CharField(max_length=50, choices=SEKTOR, verbose_name="Viloyat sektori")
	shaxs = models.CharField(max_length=150, verbose_name=('Sektorga bog\'langan shaxs'))
	name = models.CharField(max_length=50, verbose_name="Tuman nomi")
	slug = AutoSlugField(populate_from='name')

	status = models.CharField(max_length=20, choices=STATUS, default='active')
	objects = models.Manager()
	active = ActiveManager()

	def __str__(self):
		return self.name


class MFY(models.Model):
	tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE, related_name="mfy_tuman", verbose_name="Tuman nomi")
	sektor = models.CharField(max_length=50, choices=SEKTOR, verbose_name="Sektor raqami")
	shaxs = models.CharField(max_length=150, verbose_name=('Sektorga bog\'langan shaxs'))
	name = models.CharField(max_length=100, verbose_name="MFY nomi")
	slug = AutoSlugField(populate_from='name')

	status = models.CharField(max_length=20, choices=STATUS, default='active')
	objects = models.Manager()
	active = ActiveManager()

	def __str__(self):
		return self.name


class Person(models.Model):
	# Shahs haqida malumot
	parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank = True, null=True,  verbose_name="Oila boshlig'i")
	mfy = models.ForeignKey(MFY, on_delete=models.CASCADE, related_name="person_mfy", verbose_name="MFY")

	ism = models.CharField(max_length=100, verbose_name="Ism")
	familya = models.CharField(max_length=100,  verbose_name="Familya")
	sharif = models.CharField(max_length=100,  verbose_name="Sharif")
	slug = AutoSlugField(populate_from='ism')
	tsana = models.DateField(auto_now_add=False,  verbose_name="Tug'ilgan sana")
	jins = models.CharField(max_length=20, choices=JINS, verbose_name="Jinsi")
	passport = models.CharField(max_length=15, verbose_name="Passport raqami")
	jshir  = models.PositiveIntegerField(blank=True, null=True, verbose_name="JSHIR")
	phone1 = PhoneNumberField(blank=True, null=True, verbose_name="Telefon raqam 2")
	phone2 = PhoneNumberField(blank=True, null=True, verbose_name="Telefon raqam 1")
	manzil = models.CharField(max_length=200, blank=True, null=True, verbose_name="Manzil")
	kochib_ketgan = models.BooleanField(default=False, blank=True, null=True, verbose_name="Boshqa hududga ko'chib ketgan")
	vafot_etgan = models.BooleanField(default=False, blank=True, null=True, verbose_name="Vafot etgan")
	
	created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="person_cr", blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	tekshirildi = models.BooleanField(default=False, verbose_name="Tekshirilganlik holati")
	status = models.CharField(max_length=20, choices=STATUS, default='active')
	objects = models.Manager()
	active = ActiveManager()

	def __str__(self):
		return self.ism


	def str(self):
	    full_path = [self.ism]
	    k = self.parent
	    while k is not None:
	      full_path.append(k.ism)
	      k = k.parent
	    return ' -> '.join(full_path[::-1])

	
class Photo(models.Model):
	person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="person_photo")
	slug = AutoSlugField(populate_from='person')
	photo = models.ImageField(upload_to='yordam_rasmi/%Y/%m/%d/')
	created_at = models.DateTimeField(auto_now_add=True)

	status = models.CharField(max_length=20, choices=STATUS, default='active')
	objects = models.Manager()
	active = ActiveManager()


class Fayl(models.Model):
	person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="person_fayl")
	slug = AutoSlugField(populate_from='person')
	fayl = models.FileField(upload_to='yordam_fayli/%Y/%m/%d/')
	created_at = models.DateTimeField(auto_now_add=True)

	status = models.CharField(max_length=20, choices=STATUS, default='active')
	objects = models.Manager()
	active = ActiveManager()


class Family(models.Model):
	# Oila haqida malumot
	parent = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="family_info")
	slug = AutoSlugField(populate_from='parent')
	toifa = models.CharField(max_length=20, choices=TOIFA , verbose_name="Toifa")

	oila_azolari_soni = models.PositiveIntegerField(verbose_name="Oila azolari soni")
	ishsizlar_soni = models.PositiveIntegerField(verbose_name='Mehnatga layoqatli ishsizlar', blank=True, null=True)
	bandlar_soni = models.PositiveIntegerField(verbose_name='bandligi taminlangan oila azolari', blank=True, null=True)
	ijtimoiy_holat = models.CharField(max_length=100, choices=IJTIMOIY_HOLAT ,verbose_name="Ijtimoi holati")

	oila_guruhi = models.CharField(max_length=100, choices=EHTIYOJMAND_OILA, verbose_name="Ehtiyojmant oila guruhi")
	guruh = models.CharField(max_length=100, blank=True, null=True, verbose_name="Guruh")
	phone = PhoneNumberField(blank=True, null=True, verbose_name="Oila telefon raqami ")
	vafot_etgan_soni = models.PositiveIntegerField(verbose_name='Vafot etkanlar soni', blank=True, null=True)

	created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="famly_cr", blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	status = models.CharField(max_length=20, choices=STATUS, default='active')
	objects = models.Manager()
	active = ActiveManager()

	def __str__(self):
		return self.parent.ism


class Tashkilot(models.Model):
	name = models.CharField(max_length=250,blank=True, null=True,  verbose_name="Ish beruvchi tashkilot")
	slug = AutoSlugField(populate_from='name')
	stir  = models.PositiveIntegerField(blank=True, null=True, verbose_name="Tashkilot STIR raqami")
	faoliyat_turi = models.CharField(max_length=200, choices=FAOLIYAT_TURI ,verbose_name="korxona faoliyat turi")
	loyiha = models.PositiveIntegerField(verbose_name="Tashkilot loyihalari soni", blank=True, null=True)
	ish_orni = models.PositiveIntegerField(verbose_name="Tashkilot yaratgan ish o'rni", blank=True, null=True)

	created_at = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="tashkilot_cr", verbose_name="Malumot kirituvchi")
	
	status = models.CharField(max_length=20, choices=STATUS, default='active', verbose_name="Holati")
	objects = models.Manager()
	active = ActiveManager()




	def __str__(self):
		return f"{self.name}"


class Ishli(models.Model):
	person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="ishli_person", verbose_name="Ishga Joylashtirilgan shaxs")
	slug = AutoSlugField(populate_from='person')
	tashkilot = models.ForeignKey(Tashkilot, on_delete=models.CASCADE,related_name="ishli_tashkilot", blank=True, null=True ,verbose_name="Ish beruvchi tashkilot")
	faoliyat_turi = models.CharField(max_length=200, choices=FAOLIYAT_TURI ,verbose_name="korxona faoliyat turi")
	sana = models.DateField(verbose_name="Ishga joylashgan sana")
	band_qilish = models.CharField(max_length=200, verbose_name="O'zini o'zi band qilish turi", blank=True, null=True)

	created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="ishli_cr", verbose_name="Malumot kirituvchi")
	created_at = models.DateTimeField(auto_now_add=True)

	status = models.CharField(max_length=20, choices=STATUS, default='active', verbose_name="Holati")
	objects = models.Manager()
	active = ActiveManager()

	def __str__(self):
		return self.person.ism


class Ishsiz(models.Model):
	person = models.ForeignKey(Person, on_delete=models.CASCADE,related_name="ishsiz_person", verbose_name="mehnatga layoqatli ishsiz shaxs")
	slug = AutoSlugField(populate_from='person')
	faoliyat_turi = models.CharField(max_length=200, choices=FAOLIYAT_TURI ,verbose_name="Ishlash istagidagi faoliy turi")

	created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="ishsiz_cr",  verbose_name="Malumot kirituvchi")
	created_at = models.DateTimeField(auto_now_add=True)

	status = models.CharField(max_length=20, choices=STATUS, default='active', verbose_name="Holati")
	objects = models.Manager()
	active = ActiveManager()

	def __str__(self):
		return self.person.ism



class Qaror(models.Model):
	# Муҳтож оилалар рўйхатидан чиқариш тўғрисида қарор
	person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="person_qaror")
	slug = AutoSlugField(populate_from='person')
	
	qaror_raqami = models.CharField(max_length=30, verbose_name="Qaror raqami")
	qaror_sanasi = models.DateField(verbose_name="Qaror sanasi")
	qaror_fayli = models.FileField(upload_to='qaror_fayli/%Y/%m/%d/', verbose_name="Qaror fayli")

	created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="qaror_cr", verbose_name="Malumot kirituvchi")
	created_at = models.DateTimeField(auto_now_add=True)

	status = models.CharField(max_length=20, choices=STATUS, default='active', verbose_name="Holati")
	objects = models.Manager()
	active = ActiveManager()

	def __str__(self):
		return self.person.ism

	# def save_model(self, request, obj, form, change):
	# 	if getattr(obj, 'author',None) is None:    # <---- 1 ->
	# 		obj.author = request.user

		# if not obj.created_by:      # <---- 2 ->
		# 	obj.created_by = request.users
		
		# obj.save()


class Yordam(models.Model):
	# Oilaga ko'rsatilgan yordam  
	person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person_yordam')
	slug = AutoSlugField(populate_from='person')
	yordam_sanasi = models.DateTimeField(auto_now_add=True)
	korxona = models.ForeignKey(Tashkilot,on_delete=models.CASCADE, related_name="yordam_korxona", verbose_name="Korxona nomi")
	vakil_fio = models.CharField(max_length=100, blank=True, null=True)
	yuridik = models.BooleanField()
	phone = PhoneNumberField(verbose_name="Telefon raqam", blank=True, null=True)
	yordam_turi = models.CharField(max_length=250, choices=YORDAM_TURI, verbose_name="Yordam turi")
	summa = models.PositiveIntegerField(blank=True, null=True, verbose_name="Yordam summasi")
	izoh = models.TextField(blank=True, null=True, verbose_name="Izoh")

	created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="yordam_cr")
	created_at = models.DateTimeField(auto_now_add=True)
	
	tekshirildi = models.BooleanField(default=False, verbose_name="Tekshirilganlik holati")
	status = models.CharField(max_length=20, choices=STATUS, default='active', verbose_name="Holati")
	objects = models.Manager()
	active = ActiveManager()

	def __str__(self):
		return self.person.ism

class Kompleks(models.Model):
	name = models.CharField(max_length=100, verbose_name="Kompleksga bog'langan shaxs")

	status = models.CharField(max_length=20, choices=STATUS, default='active', verbose_name="Holati")
	objects = models.Manager()
	active = ActiveManager()


	def __str__(self):
		return self.name
