from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import MyUser
from .serializers import MyUserSerializer

class UserList(ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    
def login_view(request):
	
	if request.method == 'POST':
		pass
	else:
		pass
	return render(request,'login.html')
