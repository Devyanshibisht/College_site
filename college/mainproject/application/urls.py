from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home/', views.home),
    path('login/', views.login),
    path('register/', views.register),
    path('contact/', views.contact),
    path('about/', views.about),
    path('gallery/', views.gallery),
    path('regcode/', views.registercode),
    path('user/', views.user),
    path('logout/', views.logout),
    path('logincode/', views.logincode),
    path('showuser/', views.showuser),
    path('admin1/', views.admin1),
    path('addresult/', views.addresult),
    path('addevent/', views.addevent),
    path('addnotice/', views.addnotice),
    path('delete_stu/<int:pk>/', views.delete_stu, name="delete_stu"),
    path('myevent/', views.allevent),
    path('myevent2/', views.allevent2),
    path('allimages/', views.allimages),
    path('myresult/', views.myresult),
    path('myresult/', views.myresult),
    path('mynotice/', views.mynotice),
    path('myprofile/', views.myprofile),
    path('profile/', views.profile),
    path('sendfeedback/', views.sendfeedback),
    path('feedback/', views.feedback),
    path('showmessage/', views.showmessage),
    path('delete_feed/<int:pk>/', views.delete_feed, name="delete_feed"),
    path('edit_feed/<int:pk>/', views.edit_feed, name="edit_feed"),
    path('reply/', views.reply),
    path('mymsg/', views.mymsg),
    path('delete_feed2/<int:pk>/', views.delete_feed2, name="delete_feed2"),
    path('addgall/', views.addgall),
    path('showgall/', views.showgall),
    path('showresult/', views.showresult),
    path('gallery/', views.gallery),
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)