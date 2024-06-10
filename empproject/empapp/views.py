
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import RegistrationForm, ContactusForm, RecruiterRegistrationForm, EnrollForm
from .models import Contactus, Admin


from .models import Registration,RecruiterRegistration
#from .forms import RegistrationForm
#from .models import  Contactus,Registration

def homepage(request):
    return render(request,"home.html")


def homepage1(request):
    return render(request,"home1.html")

def homepage2(request):
    return render(request,"home2.html")


def homepage3(request):
    return render(request,"home3.html")

def indexpage(request):
    return render(request,"index.html")

def indexpage1(request):
    return render(request,"index1.html")

def indexpage2(request):
    return render(request,"index2.html")


def indexpage3(request):
    return render(request,"index3.html")


def aboutuspage(request):
    return render(request,"aboutus.html")

def resumepage(request):
    return render(request,"createprofile.html")

def workfromhome(request):
    return render(request,"workfromhome.html")

def jobsindelhi(request):
    return render(request,"jobsindelhi.html")

def jobsinvizag(request):
    return render(request,"jobsinvizag.html")

def jobsinkolkata(request):
    return render(request,"jobsinkolkata.html")

def jobsinchennai(request):
    return render(request,"jobsinchennai.html")

def jobsinmumbai(request):
    return render(request,"jobsinmumbai.html")

def subcategory1(request):
    return render(request,"subcategory1.html")

def parttime(request):
    return render(request,"parttime.html")


def fulltime(request):
    return render(request,"fulltime.html")

def cards(request):
    return render(request ,"cards.html")
def viewdetails(request):
    return render(request ,"viewdetails.html")
def viewdetails1(request):
    return render(request ,"viewdetails1.html")
def viewdetails2(request):
    return render(request ,"viewdetails2.html")

def courses(request):
    return render(request ,"courses.html")

def viewemployees(request):
    auname = request.session["auname"]
    userdata = Registration.objects.all()
    usercount = Registration.objects.count()
    return render(request, "viewemployees.html", {"auname": auname, "userdata": userdata, "usercount": usercount})


def viewemployees1(request):
    auname = request.session["auname"]
    userdata = Registration.objects.all()
    usercount = Registration.objects.count()
    return render(request, "viewemployees1.html", {"auname": auname, "userdata": userdata, "usercount": usercount})



def viewrecruiters(request):
    auname = request.session["auname"]
    userdata = RecruiterRegistration.objects.all()
    usercount= RecruiterRegistration.objects.count()
    return render(request, "viewrecruiters.html", {"auname": auname, "userdata": userdata, "usercount": usercount})

"""
def deleteemployees(reequest,eid):
    RecruiterRegistration.objects.filter(id=eid).delete()
    return redirect("viewemployees")
"""
def addcontactusfunction(request):
    form = ContactusForm()

    if request.method == "POST":
        form = ContactusForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Added Successfully"
            return render(request, "addedsuccessfully.html", {"msg": msg})
        else:
            return HttpResponse("Query is not added")

    return render(request, "contactus.html", {"form": form})

def logindemofunction(request):
    return render(request,"logindemo.html")
"""
def checklogindemofunction(request):
    email=request.POST["emailid"]
    pwd=request.POST["password"]

    if email=="klu@gmail.com" and pwd=="klu":
        return HttpResponse("<b>Login Success</b>")
    else:
        return HttpResponse("<font color=red>Login Failed</font>")
"""

def userlogin(request):
    return render(request,"userlogin.html")

def checkuserlogin(request):
    emailid=request.POST["emailid"]
    pwd=request.POST["password"]

    flag=Registration.objects.filter( Q(email=emailid) & Q(password=pwd) )
    print(flag)

    if flag:
        user=Registration.objects.get(email=emailid)
        print(user)
        print(user.id,user.fullname)  #other fields
        request.session["uname"]=user.username
        return render(request,"home1.html",{"uname":user.username})
    else:
        msg="Login Failed"
        return render(request, "userlogin.html",{"msg":msg})

def userhome(request):
    username=request.session["uname"]
    return render(request,"userhome.html",{"uname":username})


def userlogout(request):
    return render(request,"userlogin.html")


def adminlogin(request):
    return render(request,"adminlogin.html")


def checkadminlogin(request):
    uname = request.POST["ausername"]
    pwd = request.POST["apassword"]

    flag = Admin.objects.filter(Q(username__exact=uname) & Q(password__exact=pwd))
    print(flag)

    if flag:
        admin = Admin.objects.get(username=uname)
        print(admin)
        request.session["auname"] = admin.username
        return render(request, "adminhome.html", {"auname": admin.username})
    else:
        msg = "Login Failed"
        return render(request, "adminlogin.html", {"msg": msg})


def adminhome(request):
    auname=request.session["auname"]
    return render(request,"adminhome.html",{"auname":auname})


def adminlogout(request):
    return render(request,"adminlogin.html")



def recruiterlogin(request):
    return render(request,"recruiterlogin.html")


def checkrecruiterlogin(request):
    uname = request.POST["rusername"]
    pwd = request.POST["rpassword"]

    flag1 = RecruiterRegistration.objects.filter(Q(username__exact=uname) & Q(password__exact=pwd))
    print(flag1)

    if flag1:
        recruiter = RecruiterRegistration.objects.get(username=uname)
        print(recruiter)
        request.session["auname"] = recruiter.username
        return render(request, "recruiterhome.html", {"auname": recruiter.username})
    else:
        msg = "Login Failed"
        return render(request, "recruiterlogin.html", {"msg": msg})


def recruiterhome(request):
    auname=request.session["auname"]
    return render(request,"recruiterhome.html",{"auname":auname})


def recruiterlogout(request):
    return render(request,"recruiterlogin.html")

"""def savecontactusfunction(request, ):

    name = request.POST["name"]
    email = request.POST["emailid"]
    subject = request.POST["subject"]
    comment = request.POST["comment"]
    contactobj = contactus(con_name=name, con_emailid=email,  con_subject=subject, con_comment=comment)
    contactus.save(contactobj)
    return HttpResponse("Contactus Added Successfully")"""

def registration(request):
    form = RegistrationForm()

    if request.method == "POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Successfully Registered"
            return render(request,"regsuccess.html",{"msg":msg})
        else:
            return HttpResponse("Registration Failed")

    return render(request,"registration.html",{"form":form})



def recruiterregistration(request):
    form1 = RecruiterRegistrationForm()

    if request.method == "POST":
        form1=RecruiterRegistrationForm(request.POST)
        if form1.is_valid():
            form1.save()
            msg = "Successfully Registered"
            return render(request,"recregsuccess.html",{"msg":msg})
        else:
            return HttpResponse("Registration Failed")

    return render(request,"recruiterregistration.html",{"form":form1})


def enroll(request):
    form2 = EnrollForm()

    if request.method == "POST":
        form2 = EnrollForm(request.POST)
        if form2.is_valid():
            form2.save()
            msg = "Added Successfully"
            return render(request, "courses.html", {"msg": msg})
        else:
            return HttpResponse("Query is not added")

    return render(request, "enroll.html", {"form": form2})

def enrolled(request):
    return render(request,"enrolled.html")