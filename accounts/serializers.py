from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MyUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'email')



class MyUserSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = MyUser
		fields = ('user', 'jins', 'tsana', 'user_photo',\
				'viloyat', 'tuman', 'address', 'phone1', 'passport', \
				'work_place', 'position', 'created_by')

# swagger update
