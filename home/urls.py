from django.urls import path
from home import views
urlpatterns = [
    path('',views.index, name = "home" ),
    path('login',views.loginuser, name = "login" ),
    path('logout',views.logoutuser, name = "logout" ),
    path('user',views.userregistration, name = "user" ),
    path('ipcoreicc',views.ipcoreicc, name = "ipcoreicc" ),
    path('ipcorencd',views.ipcorencd, name = "ipcorencd" ),
    path('logintoicc',views.loginicc, name = "logintoicc" ),
    path('boss',views.boss, name = "boss" ),
    path('registeredcomplaint',views.registrationcomplaint, name = "registeredcomplaint" ),
    path('ipregistrationcomplaint',views.ipregistrationcomplaint, name = "ipregistrationcomplaint" ),

    path('activation',views.activation, name = "activation" ),
    path('solution',views.solution, name = "solution" ),
    path('cloud',views.cloud, name = "cloud" ),
    path('systememail',views.systememail, name = "systememail" ),
    path('userprofile',views.userprofile, name = "userprofile" ),
    path('boss',views.boss, name = "boss" ),
    path('bossportal',views.bossportal, name = "bossportal" ),
  
    path('logoutboss',views.logoutboss, name = "logoutboss" ),
    path('employees',views.employees, name = "employees" ),
    path('ipemployees',views.ipemployees, name = "ipemployees" ),
    path('icc',views.icc, name = "icc" ),
    path('ncd',views.ncd, name = "ncd" ),
    path('sea',views.sea, name = "sea" ),
    path('cc',views.cc, name = "cc" ),
    path('acs',views.acs, name = "acs" ),
    path('sq',views.sq, name = "sq" ),
    path('departments',views.departments, name = "departments" ),
    path('empregistration',views.empregistration, name = "empregistration" ),
    path('useripcore',views.useripcore, name = "useripcore" ),
    path('iccregistration',views.iccregistration, name = "iccregistration" ),
    path('ncdregistration',views.ncdregistration, name = "ncdregistration" ),
    path('searegistration',views.searegistration, name = "searegistration" ),
    path('ccregistration',views.ccregistration, name = "ccregistration" ),
    path('acsregistration',views.acsregistration, name = "acsregistration" ),
    path('sqregistration',views.sqregistration, name = "sqregistration" ),
    path('engregistration',views.engregistration, name = "engregistration" ),
    path('base',views.base, name = "base" ),
    path('employeesicc',views.employeesicc, name = "employeesicc" ),
    path('employeesncd',views.employeesncd, name = "employeesncd" ),
    path('employeescc',views.employeescc, name = "employeescc" ),
    path('employeessea',views.employeessea, name = "employeessea" ),
    path('employeesacs',views.employeesacs, name = "employeesacs" ),
    path('employeessq',views.employeessq, name = "employeessq" ),
    path ('employeesacs/<int:tokenid>',views.deleteacs, name = 'employeesacs'),
    path ('employeesicc/<int:tokenid>',views.deleteicc, name = 'employeesicc'),
    path ('employeesncd/<int:tokenid>',views.deletencd, name = 'employeesncd'),
    path ('employeessea/<int:tokenid>',views.deletesea, name = 'employeessea'),
    path ('employeessq/<int:tokenid>',views.deletesq, name = 'employeessq'),
    path ('employeescc/<int:tokenid>',views.deletecc, name = 'employeescc'),

]