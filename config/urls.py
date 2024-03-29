"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions  
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi
from accounts.views import login_view 

schema_view = get_schema_view( 
    openapi.Info(
        title='Blog API',
        description='oddiy API loyixasi', 
        default_version='v1',
        terms_of_service='https://google.com.policies.terms',
        contact=openapi.Contact(email="xatamjonovulugbek17@gmail.com"),
        license=openapi.License('Blog API litsenziasi'),
        ),
        public=True,
        permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin2/', login_view),

    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    
     
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-radoc'),

    # path('account/', include('accounts.urls')),
    path('person/', include('persons.urls'), name='person'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
