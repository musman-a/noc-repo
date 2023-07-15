from django.shortcuts import render,redirect, HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Icccomplaints, Ncdcomplaints,Seacomplaints,Cccomplaints,Acscomplaints,Sqcomplaints
from datetime import datetime





# Create your views here.


def index(request):
    return render(request,("departments.html"))

def loginuser(request):
     if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username= username, password= password)
        
        if user is not None:
    # A backend authenticated the credentials
            login(request,user)
            
            return redirect ("/userprofile")
        else:

           
            return redirect("/login") 
        
    
     return render(request,("login.html"))


def loginicc(request):
     if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username= username, password= password)
        
        if user is not None:
    # A backend authenticated the credentials
            login(request,user)
            
            return redirect("/employeesicc")
        else:

           
            return redirect("/logintoicc") 
        
    
     return render(request,("logintoicc.html"))     

def logoutuser(request):
    
        logout(request)
        messages.success(request,"Successfully Logout")
        return redirect("/login") 
      

def userregistration(request):
    if request.method =="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password!=password1:
         messages.error(request,"Your Password is not same")

        else:    

         my_user = User.objects.create_user(username,email,password)
         my_user.save()
         return redirect('login')
    return render (request,("user.html"))     

def ipcoreicc(request):
    if request.method =="POST":
        tokenid = request.POST.get('tokenid')
        clientname = request.POST.get('clientname')
        typeofcomplaint = request.POST.get('typeofcomplaint')
        complaintlevel = request.POST.get('complaintlevel')
        status = request.POST.get('status')

        icccomplaint = Icccomplaints(tokenid = tokenid,clientname = clientname, typeofcomplaint = typeofcomplaint, complaintlevel = complaintlevel, status = status, date = datetime.today() )
        icccomplaint.save()
        messages.success(request,"Your Complaints has been Successfully")

    allicc = Icccomplaints.objects.all()
    context = {'icc': allicc}
    return render(request,'ipcoreicc.html',context)      

    


def ipcorencd(request):
    if request.method =="POST":
        tokenid = request.POST.get('tokenid')
        clientname = request.POST.get('clientname')
        typeofcomplaint = request.POST.get('typeofcomplaint')
        complaintlevel = request.POST.get('complaintlevel')
        status = request.POST.get('status')

        ncdcomplaint = Ncdcomplaints(tokenid = tokenid,clientname = clientname, typeofcomplaint = typeofcomplaint, complaintlevel = complaintlevel, status = status, date = datetime.today() )
        ncdcomplaint.save()
        messages.success(request,"Your Complaints has been Successfully")

    allncd = Ncdcomplaints.objects.all()
    context = {'ncdrecord': allncd}
    return render(request,'ipcorencd.html',context)

       

def systememail(request):
    if request.method =="POST":
        tokenid = request.POST.get('tokenid')
        clientname = request.POST.get('clientname')
        typeofcomplaint = request.POST.get('typeofcomplaint')
        complaintlevel = request.POST.get('complaintlevel')
        status = request.POST.get('status')

        seacomplaint = Seacomplaints(tokenid = tokenid,clientname = clientname, typeofcomplaint = typeofcomplaint, complaintlevel = complaintlevel, status = status, date = datetime.today() )
        seacomplaint.save()
        messages.success(request,"Your Complaints has been Successfully")
    allsea = Seacomplaints.objects.all()
    context = {'seacomplaintrecord': allsea}
    return render(request,'systememail.html',context)


def solution(request):
    if request.method =="POST":
        tokenid = request.POST.get('tokenid')
        clientname = request.POST.get('clientname')
        typeofcomplaint = request.POST.get('typeofcomplaint')
        complaintlevel = request.POST.get('complaintlevel')
        status = request.POST.get('status')

        sqcomplaint = Sqcomplaints(tokenid = tokenid,clientname = clientname, typeofcomplaint = typeofcomplaint, complaintlevel = complaintlevel, status = status, date = datetime.today() )
        sqcomplaint.save()
        messages.success(request,"Your Complaints has been Successfully")
    allsq = Sqcomplaints.objects.all()
    context = {'sqrecord': allsq}
    return render(request,'solution.html',context)

   

def cloud(request):
    if request.method =="POST":
        tokenid = request.POST.get('tokenid')
        clientname = request.POST.get('clientname')
        typeofcomplaint = request.POST.get('typeofcomplaint')
        complaintlevel = request.POST.get('complaintlevel')
        status = request.POST.get('status')

        cccomplaint = Cccomplaints(tokenid = tokenid,clientname = clientname, typeofcomplaint = typeofcomplaint, complaintlevel = complaintlevel, status = status, date = datetime.today() )
        cccomplaint.save()
        messages.success(request,"Your Complaints has been Successfully")
    allcc = Cccomplaints.objects.all()
    context = {'ccrecord': allcc}
    return render(request,'cloud.html',context)

    

def activation(request):
    if request.method =="POST":
        tokenid = request.POST.get('tokenid')
        clientname = request.POST.get('clientname')
        typeofcomplaint = request.POST.get('typeofcomplaint')
        complaintlevel = request.POST.get('complaintlevel')
        status = request.POST.get('status')

        acscomplaint = Acscomplaints(tokenid=tokenid,clientname = clientname, typeofcomplaint = typeofcomplaint, complaintlevel = complaintlevel, status = status, date = datetime.today() )
        acscomplaint.save()
        messages.success(request,"Your Complaints has been Successfully")
    allacs = Acscomplaints.objects.all()
    context = {'acsrecord': allacs}
    return render(request,'activation.html',context)


               

def userprofile(request):
    return render(request,("userprofile.html"))    


def boss(request):
    if request.method =="POST":
        username = request.POST.get('boss')
        password = request.POST.get('boss123')
        if username != username:
            messages.error(request, "you are not boss")

        if password != password:
            messages.error(request,'you are not boss')    
        
       
        
        
       
    # A backend authenticated the credentials
        
         
        else:
            return redirect ("/bossportal")
          

           
    return render(request,("boss.html"))    


def bossportal(request):
    return render(request,("bossportal.html"))

  








def logoutboss(request):
    
        logout(request)
        messages.success(request,"Successfully Logout")
        return redirect("/boss")  

def employees(request):
    return render(request,("employees.html"))   

def ipemployees(request):
    return render(request,("ipemployees.html"))            

def icc(request):
    allicc = Icccomplaints.objects.all()
    context = {'icc': allicc}
    return render(request, 'icc.html',context)
    

def ncd(request):
    allncd = Ncdcomplaints.objects.all()
    context = {'ncdrecord': allncd}
    return render(request, 'ncd.html',context)
  


def sea(request):
    allsea = Seacomplaints.objects.all()
    context = {'seacomplaintrecord': allsea}
    return render(request, 'sea.html',context)
     

def cc(request):
    allcc = Cccomplaints.objects.all()
    context = {'ccrecord': allcc}
    return render(request, 'cc.html',context) 
  

def acs(request):
    allacs = Acscomplaints.objects.all()
    context = {'acsrecord': allacs}
    return render(request, 'acs.html',context) 
   

def sq(request):
    allsq = Sqcomplaints.objects.all()
    context = {'sqrecord': allsq}
    return render(request, 'sq.html',context)
 

def empregistration(request):
    return render(request,("empregistration.html"))                   

def departments(request):
    allicc = Icccomplaints.objects.all()
    context = {'icc': allicc}
    return render(request, 'departments.html',context)





              



def iccregistration(request):
     if request.method =="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password!=password1:
         messages.error(request,"Your Password is not same")

        else:    

         my_user = User.objects.create_user(username,email,password)
         my_user.set_password(password)
         my_user.save()
         return redirect('logintoicc')
     
     return render(request,("iccregistration.html"))  

def ncdregistration(request):
    return render(request,("ncdregistration.html"))          

def searegistration(request):
    return render(request,("searegistration.html")) 

def ccregistration(request):
    return render(request,("ccregistration.html")) 

def acsregistration(request):
    return render(request,("acsregistration.html"))   

def sqregistration(request):
    return render(request,("sqregistration.html"))    

def engregistration(request):
    return render(request,("engregistration.html"))                                      

def base(request):
    return render(request,("base.html"))   


def employeesicc(request):
    allicc = Icccomplaints.objects.all()
    context = {'icc': allicc}
    return render(request, 'employeesicc.html',context)
      

def employeesncd(request):
    allncd = Ncdcomplaints.objects.all()
    context = {'ncdrecord': allncd}
    return render(request, 'employeesncd.html',context)
     

def employeessea(request):
    allsea = Seacomplaints.objects.all()
    context = {'seacomplaintrecord': allsea}
    return render(request, 'employeessea.html',context)
    

def employeescc(request):
    allcc = Cccomplaints.objects.all()
    context = {'ccrecord': allcc}
    return render(request, 'employeescc.html',context) 
  

def employeesacs(request):
    allacs = Acscomplaints.objects.all()
    context = {'acsrecord': allacs}
    return render(request, 'employeesacs.html',context) 
    

def employeessq(request):
    allsq = Sqcomplaints.objects.all()
    context = {'sqrecord': allsq}
    return render(request, 'employeessq.html',context)
   
def useripcore(request):
    return render(request,("useripcore.html"))
   
def registrationcomplaint(request):
    return render(request,("registeredcomplaint.html"))

def ipregistrationcomplaint(request):
    return render(request,("ipregistrationcomplaint.html"))    

def deleteacs(request, tokenid):
    acs = Acscomplaints.objects.get(tokenid =tokenid)
    acs.delete()
    return redirect("/employeesacs")    

def deleteicc(request, tokenid):
    acs = Icccomplaints.objects.get(tokenid =tokenid)
    acs.delete()
    return redirect("/employeesicc")

def deletencd(request, tokenid):
    acs = Ncdcomplaints.objects.get(tokenid =tokenid)
    acs.delete()
    return redirect("/employeesncd")    

def deletesea(request, tokenid):
    acs = Seacomplaints.objects.get(tokenid =tokenid)
    acs.delete()
    return redirect("/employeessea") 

def deletesq(request, tokenid):
    acs = Sqcomplaints.objects.get(tokenid =tokenid)
    acs.delete()
    return redirect("/employeessq")  

def deletecc(request, tokenid):
    acs = Cccomplaints.objects.get(tokenid =tokenid)
    acs.delete()
    return redirect("/employeescc")                  

