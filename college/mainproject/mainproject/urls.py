from django.contrib import admin
from django.urls import path, include
from application import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('application.urls')),
    path('home/', include('application.urls')),
    path('login/', include('application.urls')),
    path('register/', include('application.urls')),
    path('contact/', include('application.urls')),
    path('about/', include('application.urls')),
    path('gallery/', include('application.urls')),
    path('regcode/', include('application.urls')),
    path('user/', include('application.urls')),
    path('logout/', include('application.urls')),
    path('logincode/', include('application.urls')),
    path('showuser/', include('application.urls')),
    path('admin1/', include('application.urls')),
    path('addresult/', include('application.urls')),
    path('addevent/', include('application.urls')),
    path('addnotice/', include('application.urls')),
    path('delete_stu/', include('application.urls')),
    path('myevent/', include('application.urls')),
    path('myevent2/', include('application.urls')),
    path('allimages/', include('application.urls')),
    path('myresult/', include('application.urls')),
    path('mynotice/', include('application.urls')),
    path('myprofile/', include('application.urls')),
    path('profile/', include('application.urls')),
    path('sendfeedback/', include('application.urls')),    
    path('feedback/', include('application.urls')),
    path('showmessage/', include('application.urls')),
    path('delete_feed/', include('application.urls')),
    path('edit_feed/', include('application.urls')),
    path('reply/', include('application.urls')),
    path('mymsg/', include('application.urls')),
    path('delete_feed2/', include('application.urls')),
    path('addgall/', include('application.urls')),
    path('showgall/', include('application.urls')),
    path('showresult/', include('application.urls')),
    path('gallery/', include('application.urls')),
]
