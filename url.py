graph_convolutional_networks URL Configuration    
    
The `urlpatterns` list routes URLs to views. For more information please see:  https://docs.djangoproject.com/en/3.0/topics/http/urls/ Examples:  Function views    
1.	Add an import:  from my_app import views    
2.	Add a URL to urlpatterns:  path('', views.home, name='home')    
Class-based views    
1. Add an import:  from other_app.views import Home      2. Add a URL to urlpatterns:    path('', Home.as_view(), name='home')    
Including another URLconf    
1.Import the include() function: from django.urls import include, path  2.    Add a URL to urlpatterns:  path('blog/', include('blog.urls')) """   from django.conf.urls import url from django.contrib import   
admin from Remote_User import views as remoteuser from  
Behavior_Based_Intranet_Attacks import settings from Service_Provider import views as serviceprovider from  django.conf.urls.static import static   urlpatterns = [ url('admin/', admin.site.urls),   
   url(r'^$', remoteuser.index, name="index"),      url(r'^login/$', remoteuser.login, name="login"),      url(r'^Register1/$',    
remoteuser.Register1, name="Register1"),      url(r'^Predict_Behavior_Based_Intranet_Attacks/$', remoteuser.Predict_Behavior_Based_Intranet_Attacks,   
name="Predict_Behavior_Based_Intranet_Attacks"),   
 url(r'^ViewYourProfile/$',    
remoteuser.ViewYourProfile, name="ViewYourProfile"),   url(r'^serviceproviderlogin/$', serviceprovider.serviceproviderlo   gin, name="serviceproviderlogin"),   url(r'View_Remote_Users/$', 
serviceprovider.View_Remote_Users,nam e="View_Remote_Users"),   url(r'^charts/(?P<chart_type>\w+)', serviceprovider.charts,name="charts"),  url(r'^charts1/(?P<chart_type>\w+)', serviceprovider.charts1, name="charts1"), url(r'^likeschart/(?P<like_chart>\w+)', serviceprovider.likeschart, name="likeschart"),  
url(r'^View_Predicted_Behavior_Based_Intranet_Attacks_Type_Ratio    
/$', serviceprovider.View_Predicted_Behavior_Based_Intranet_Attacks_Type_ Ratio, name="View_Predicted_Behavior_Based_Intranet_Attacks_Type_Ratio"),     url(r'^train_model/$', serviceprovider.train_model, name="train_model"), url(r'^View_Predicted_Behavior_Based_Intranet_Attacks_Type/$', serviceprovider.View_Predicted_Behavior_Based_Intranet_Attacks_Type, name="View_Predicted_Behavior_Based_Intranet_Attacks_Type"),       
url(r'^Download_Predicted_DataSets/$',  	serviceprovider.Download_Predicted_DataSets, name="Download_Predicted_DataSets"),    
    
 static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) Models.py  from django.db import models    
    
# Create your models here.  from django.db.models import CASCADE    
class ClientRegister_Model(models.Model):      username =  models.CharField(max_length=30)      email = models.EmailField(max_length=30)      password = models.CharField(max_length=10)     phoneno = models.CharField(max_length=10)    country = models.CharField(max_length=30)      state = models.CharField(max_length=30)      city = models.CharField(max_length=30) 
  gender= models.CharField(max_length=30)      address= models.CharField(max_length=30) class   Behavior_Based_Intranet_Attacks(models.Model):    
    
Login_Frequency= models.CharField(max_length=3000)    
Failed_Login_Attempts= models.CharField(max_length=3000)    
Data_Transferred_MB= models.CharField(max_length=3000)    
Session_Duration_Minutes= models.CharField(max_length=3000)    
Accessed_Files= models.CharField(max_length=3000)    
Password_Changes= models.CharField(max_length=300 
  IP_Location_Changes= models.CharField(max_length=3000)   
Malware_Detections= models.CharField(max_length=3000)    
Suspicious_URL_Clicks= models.CharField(max_length=3000)    
Time_Since_Last_Login_Hours= models.CharField(max_length=3000)  Prediction=  models.CharField(max_length=3000) class detection_accuracy(models.Model):    
    
names = models.CharField(max_length=300)      ratio =  models.CharField(max_length=300)   class detection_ratio(models.Model):    
    
names = models.CharField(max_length=300)    
 ratio =  models.CharField(max_length=300)    
    
