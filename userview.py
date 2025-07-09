from django.db.models  import Count from django.db.models   import Q from django.shortcu    import render, redirect, get_object_or_404       
import pandas as pd  from sklearn.feature_extraction.text  import CountVectorizerfromsklearn.metrics   import accuracy_score, confusion_matrix,    
classification_report    
from sklearn.metrics   import accuracy_score   from sklearn.model_selection  
 importtrain_test_split    from sklearn.preprocessing      import LabelEncoder    from sklearn.svm import SVC 
             from sklearn.linear_model                import LogisticRegression              from  sklearn.ensemble import      
GradientBoostingClassifier,   VotingClassifier from sklearn.metrics  import accuracy_score  # Create your views here.    from Remote_User.models  imporClientRegister_Model,Behavior_Based_Intranet_Attacks,detection_ratio   
,detection_accuracy  def login(request): if request.method == "POST" and 'submit1' in request.POST:    
    
username = request.POST.get('username')        
  password = request.POST.get('password')          try:  enter =    
ClientRegister_Model.objects.get(username=username,password=password    
)    
request.session["userid"] = enter.id    
    
return redirect('ViewYourProfile')     except: pass      return render(request,'RUser/login.html')  def index(request):   
 return render(request, 'RUser/index.html')  def Add_DataSet_Details(request):   
return render(request, 'RUser/Add_DataSet_Details.html',    
{"excel_data":   	''}) def Register1(request):  if request.method == "POST":  
 username = request.POST.get('username')          email =  request.POST.get('email')          password = request.POST.get('password')          phoneno = request.POST.get('phoneno')          country = request.POST.get('country')          state =  request.POST.get('state')        city = request.POST.get('city')           address = request.POST.get('address')          gender =   request.POST.get('gender')    
ClientRegister_Model.objects.create(username=username, email=email,   
password=password,   phoneno=phoneno,                                             country=country,  
state=state , city=city, address=address, gender=gender)   
obj = "Registered Successfully"      return render(request,    
'RUser/Register1.html',{'object':obj})  else:    
  return render(request,'RUser/Register1.html')   def  
ViewYourProfile(request):  userid  = request.session['userid']    obj  =  ClientRegister_Model.objects.get(id= userid)      return  
render(request,'RUser/ViewYourProfile.html',{ 
'obj ect':obj})   def  
Predict_Behavior_Based_Intranet_Attacks(requ  est):     if request.method == "POST":  if request.method == "POST":    
    
Login_Frequency= request.POST.get('Login_Frequency')                
Failed_Login_Attempts= request.POST.get('Failed_Login_Attempts')              
 Data_Transferred_MB= request.POST.get('Data_Transferred_MB')                
Session_Duration_Minutes= request.POST.get('Session_Duration_Minutes')    
Accessed_Files= request.POST.get('Accessed_Files')    
Password_Changes= request.POST.get('Password_Changes')                
IP_Location_Changes= request.POST.get('IP_Location_Changes')                
Malware_Detections= request.POST.get('Malware_Detections')                
Suspicious_URL_Clicks= request.POST.get('Suspicious_URL_Clicks')                
Time_Since_Last_Login_Hours= request.POST.get('Time_Since_Last_Login_Hours')    
    
    
models = []  dataset = pd.read_csv('behavior_based_intranet_attack_data.csv')    
# Preprocessing    
X = dataset.drop('Attack_Type', axis=1)          y = dataset['Attack_Type']    
    
# Encode the target variable (Attack_Type) as it is categorical  label_encoder  
= LabelEncoder() y_encoded  = label_encoder.fit_transform(y)    # Split the data into training and testing sets          X_train, X_test, 
 y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42)    
    
# SVM Model          print("SVM")  from sklearn import svm    
    
lin_clf = svm.LinearSVC()          lin_clf.fit(X_train, y_train)           predict_svm = lin_clf.predict(X_test)      svm_acc =accuracy_score(y_test, predict_svm) * 100      print("ACCURACY")    print(svm_acc)  print("CLASSIFICATION REPORT")   print(classification_report(y_test, 
 
predict_svm))         print("CONFUSION MATRIX") print(confusion_matrix(y_test, 
predict_svm))         models.append(('svm', lin_clf))    
    
print("Logistic Regression")    
    
from sklearn.linear_model import LogisticRegression    
    
reg = LogisticRegression(random_state=0, solver='lbfgs').fit(X_train,   y_train)         y_pred = reg.predict(X_test)       print("ACCURACY")  
print(accuracy_score(y_test, y_pred) * 100)    
 print("CLASSIFICATION   REPORT")        
  print(classification_report(y_test, y_pred))            print("CONFUSION MATRIX")          print(confusion_matrix(y_test, y_pred))          models.append(('logistic', reg))    
    
print("Gradient Boosting Classifier")    gb_model = GradientBoostingClassifier()          gb_model.fit(X_train,  y_train)          dtcpredict = gb_model.predict(X_test)            print("ACCURACY")  
 print(accuracy_score(y_test,dtcpredict)*100)      
 print("CLASSIFICATION REPORT")  	  	 
print(classification_report(y_test,  dtcpredict))      print("CONFUSION MATRIX") 
 print(confusion_matrix(y_test, dtcpredict))    
models.append(('GradientBoostingClassifier', gb_model))    
    
classifier = VotingClassifier(models)          classifier.fit(X_train, y_train)       
   y_pred =  classifier.predict(X_test)    
    
# Input for prediction  input_data = [[Login_Frequency, Failed_Login_Attempts,  
Data_Transferred_MB,    
Session_Duration_Minutes, 
 Accessed_Files,    
Password_Changes 
, IP_Location_Changes, 
 Malware_Detections,    
Suspicious_URL_Clicks, Time_Since_Last_Login_Hours]]        predicted_class_index = classifier.predict(input_data)[0]    
  predicted_class = label_encoder.inverse_transform([predicted_class_index])[0]    
Behavior_Based_Intranet_Attacks.objects.create(  Login_Frequency=Login_Frequency,    
Failed_Login_Attempts=Failed_Login_Attempts,    
Data_Transferred_MB=Data_Transferred_MB,    
Session_Duration_Minutes=Session_Duration_Minutes,    
Accessed_Files=Accessed_Files,    
Password_Changes=Password_Changes,    
IP_Location_Changes=IP_Location_Changes,        
Malware_Detections=Malware_Detections,    
Suspicious_URL_Clicks=Suspicious_URL_Clicks,    
Time_Since_Last_Login_Hours=Time_Since_Last_Login_Hours,    
    
Prediction=predicted_class)    
    
return render(request,    
'RUser/Predict_Behavior_Based_Intranet_Attacks.html',{'objs':predicted_class})      return render(request,    
'RUser/Predict_Behavior_Based_Intranet_Attacks.html')  	 
Adminviews.py  	 
from django.db.models  import  Count, Avg  from django.shortcuts  import render, redirect  from django.db.models  import Count from django.db.models 
 import Q import datetime  import xlwt from django.http  import HttpResponse  import pandas as pd  
from sklearn.feature_extraction.text  import CountVectorizer  from sklearn.metrics   import  accuracy_score,   confusion_matrix, classification_report  
 from sklearn.metrics   import accuracy_score  
 from sklearn.feature_extraction.text  
import CountVectorizer  from sklearn.metrics 
 import accuracy_score,confusion_matrix,  classification_report    from sklearn.model_selection  import train_test_split  from sklearn.preprocessing  import LabelEncoder  from sklearn.svm  import SVC from sklearn.linear_model    
import LogisticRegression  fromsklearn.ensemble  
import GradientBoostingClassifier,VotingClassifie # Create your views here.    from Remote_User.models  import   ClientRegister_Model,Behavior_Based_Intranet_Attacks,detection_ratio,detection _acc uracy def serviceproviderlogin(request):      if request.method  == "POST":    admin = request.POST.get('username')        password = request.POST.get('password')          if admin == "Admin" and password =="Admin":    
detection_accuracy.objects.all().delete()             return  
redirect('View_Remote_Users')    
    
return render(request,'SProvider/serviceproviderlogin.html')    
    
def View_Predicted_Behavior_Based_Intranet_Attacks_Type_Ratio(request):    
detection_ratio.objects.all().delete() ratio   
= "" kword = 'Phishing'      print(kword)      obj =   Behavior_Based_Intranet_Attacks.objects.all().filter(Q(Prediction=kword))      obj1 = Behavior_Based_Intranet_Attacks.objects.all()      count = obj.count(); count1 = obj1.count();   ratio = (count / count1) * 100 if ratio != 0:   detection_ratio.objects.create(names=kword, ratio=ratio ratio12 = ""   kword12 = 'Malware' print(kword12) obj12 
Behavior_Based_Intranet_Attacks. objects.all().filter(Q(Prediction=kwo rd12)) obj112 =  
Behavior_Based_Intranet_Attacks. 
objects.all() count12 = obj12.count();      count112 = obj112.count();     ratio12 = (count12 / count112) * 100  if ratio12 != 0:    
detection_ratio.objects.create(names=kword12, ratio=ratio ratio13   
 
kword13 = 'Brute_Force'      print(kword13)     
 obj13 =  Behavior_Based_Intranet_Attacks.objects.all().filter(Q(Prediction=kword13))      obj113 = Behavior_Based_Intranet_Attacks.objects.all()      count13 = obj13.count();      count113 = obj113.count();      ratio13 = (count13 / count113) * 100 if ratio13 != 0:    
detection_ratio.objects.create(names=kword13, ratio=ratio13)      obj = detection_ratio.objects.all() return render(request,    
'SProvider/View_Predicted_Behavior_Based_Intranet_Attacks_Type_Ratio.html',    
{'objs': obj})    
def View_Remote_Users(request):    
obj=ClientRegister_Model.objects.all()   	   	   	   	   	 return   
render(request,'SProvider/View_Remote_Users.html',{'objects':obj})    
    
def charts(request,chart_type):    
chart1 = detection_ratio.objects.values('names').annotate(dcount=Avg('ratio'))    
return render(request,"SProvider/charts.html", {'form':chart1, 'chart_type':chart_type})  
def   	charts1(request,chart_type):   chart1  =  
detection_accuracy.objects.values('names').annotate(dcount=Avg('ratio'))      
return render(request,"SProvider/charts1.html", {'form':chart1, 'chart_type':chart_type})    
    
def View_Predicted_Behavior_Based_Intranet_Attacks_Type(request):    
obj =Behavior_Based_Intranet_Attacks.objects.all()    
return render(request,    
'SProvider/View_Predicted_Behavior_Based_Intranet_Attacks_Type.html', {'list_objects':  obj})    
    
def likeschart(request,like_chart):    
charts =detection_accuracy.objects.values('names').annotate(dcount=Avg('ratio'))    return render(request,"SProvider/likeschart.html", {'form':charts,   
'like_chart':like_chart})  	  	  	 def  Download_Predicted_DataSets(request):  	 respons= HttpResponse(content_type='application/ms-excel')    # decide file name     response['Content-Disposition'] = 'attachment; filename="Predicted_Datasets.xls"' 
 # creating workbook      wb = xlwt.Workbook(encoding='utf-8')    
# adding sheet     
 Ws wb.add_sheet("sheet1")     # Sheet header, first row     row_num = 0     font_style 
= xlwt.XFStyle()    
  # headers are bold     font_style.font.bold = True    
# writer = csv.writer(response)    
obj = Behavior_Based_Intranet_Attacks.objects.all() data = obj   
# dummy method to fetch data. for my_row in data: row_num = row_num + 1          ws.write(row_num, 0,  
  my_row.Login_Frequency, font_style)          ws.write(row_num, 
 1,my_row.Failed_Login_Attempts, font_style)              ws.write(row_num, 
     2, my_row.Failed_Login_Attempts, font_style)          ws.write(row_num, 
 3, my_row.Session_Duration_Minutes, font_style)        
  ws.write(row_num, 
 4, my_row.Accessed_Files, font_style)          ws.write(row_num, 
 5, my_row.Password_Changes, font_style)          ws.write(row_num,  
6, my_row.IP_Location_Changes, font_style)          ws.write(row_num,  
7, my_row.Malware_Detections, font_style)  
        ws.write(row_num,  
8, my_row.Suspicious_URL_Clicks, font_style)          ws.write(row_num,  
9, my_row.Time_Since_Last_Login_Hours, font_style)                  ws.write(row_num, 
 10, my_row.Prediction, font_style)       
   wb.save(response)          return respons         def train_model(request):    detection_accuracy.objects.all().delete()         models = []        dataset   pd.read_csv('behavior_based_intranet_attack_data.csv')  
# Preprocessing    
X = dataset.drop('Attack_Type',    
axis=1)     y = dataset['Attack_Type']    
    
# Encode the target variable (Attack_Type) as it is categorical       label_encoder   	=   	LabelEncoder()    y_encoded   	=   
label_encoder.fit_transform(y)    
# Split the data into training and testing sets    
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42)    
  # SVM Model     print("SVM")      
 
from sklearn  import svm    
  lin_clf = svm.LinearSVC() 
 lin_clf.fit(X_train, y_train)      predict_svm = lin_clf.predict(X_test)      svm_acc = accuracy_score(y_test, predict_svm) * 100      print(svm_acc)  print("CLASSIFICATION REPORT")    
print(classification_report(y_test, predict_svm))    
print("CONFUSION MATRIX")    
print(confusion_matrix(y_test, predict_svm))      models.append(('svmlin_clf))     detection_accuracy.objects.create(names="SVM",  ratio=svm_acc)     print("Logistic Regression")      from sklearn.linear_model import LogisticRegression      reg =LogisticRegression(random_state=0,  solver='lbfgs').fit(X_train, y_train)      
y_pred = reg.predict(X_test)  print("ACCURACY")   
print(accuracy_score(y_test, y_pred) * 100)   print("CLASSIFICATION REPORT")    
print(classification_report(y_test, y_pred))    print("CONFUSION MATRIX")    print(confusion_matrix(y_test,y_pred))  models.append(('logistic', reg))    detection_accuracy.objects.create(names="Logistic Regression",    
ratio=accuracy_score(y_test, y_pred) * 100)    
    
print("GradientBoostingClassifier")     dtc =  
GradientBoostingClassifier() dtc.fit(X_train, y_train)      dtcpredict = dtc.predict(X_test) print("ACCURACY")  print(accuracy_score(y_test, 	dtcpredict) 	* 	100)  print("CLASSIFICATION REPORT")    
print(classification_report(y_test, dtcpredict))    
print("CONFUSION MATRIX")    
print(confusion_matrix(y_test,dtcpredict))     models.append(('GradientBoostingClassifier',dtc)) detection_accuracy.objects.create(names="Gradient  Boosting Classifier",  
 ratio=accuracy_score(y_test,  dtcpredict)  *  100)      
print("VotingClassifier")      classifier = VotingClassifier(models)      classifier.fit(X_train, y_train)      knpredict = classifier.predict(X_test)  
  print("ACCURACY")    print(accuracy_score(y_test,knpredict) *100)   print("CLASSIFICATION REPORT")    
print(classification_report(y_test, knpredict))    
print("CONFUSION MATRIX")    
print(confusion_matrix(y_test, knpredict))    
detection_accuracy.objects.create(names="VotingClassifier",    
ratio=accuracy_score(y_test, knpredict) * 100)  
    csv_format = 'Results.csv'     dataset.to_csv(csv_format, index=False)       dataset.to_markdown     obj = detection_accuracy.objects.all()       return render(request,'SProvider/train_model.html', {'objs': obj})  
