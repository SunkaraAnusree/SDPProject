from django.urls import path
from . import views


# Create your views here.
urlpatterns = [
    path("",views.indexpage,name="index"),
    path("index1",views.indexpage1,name="index1"),
    path("index2",views.indexpage2,name="index2"),
    path("index3", views.indexpage3, name="index3"),
    path("home",views.homepage,name="home"),
    path("home1",views.homepage1,name="home1"),
    path("home2",views.homepage2,name="home2"),
    path("home3", views.homepage3, name="home3"),
    path("aboutus",views.aboutuspage,name="aboutus"),
    path("Resume",views.resumepage,name="Resume"),
    path("subcategory1",views.subcategory1,name="subcategory1"),
    path("contactus",views.addcontactusfunction,name="contactus"),
    #path("savecontactus",views.savecontactusfunction,name="saveccontactus"),
    path("userlogin", views.userlogin, name="userlogin"),
    path("checkuserlogin", views.checkuserlogin, name="checkuserlogin"),
    path("workfromhome", views.workfromhome, name="workfromhome"),
    path("jobsindelhi", views.jobsindelhi, name="jobsindelhi"),
    path("jobsinmumbai", views.jobsinmumbai, name="jobsinmumbai"),
    path("jobsinvizag", views.jobsinvizag, name="jobsinvizag"),
    path("jobsinkolkata", views.jobsinkolkata, name="jobsinkolkata"),
    path("jobsinchennai", views.jobsinchennai, name="jobsinchennai"),
    path("userhome", views.userhome, name="userhome"),
    path("userlogout", views.userlogout, name="userlogout"),

    path("parttime",views.parttime,name="parttime"),
    path("fulltime",views.fulltime,name="fulltime"),

    path("registration",views.registration,name="registration"),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('adminhome',views.adminhome,name="adminhome"),
    path('checkadminlogin', views.checkadminlogin, name="checkadminlogin"),
    path('adminlogout', views.adminlogout, name='adminlogout'),

    path("recruiterregistration",views.recruiterregistration,name="recruiterregistration"),
    path('recruiterlogin', views.recruiterlogin, name='recruiterlogin'),
    path('checkrecruiterlogin', views.checkrecruiterlogin, name="checkrecruiterlogin"),
    path('recruiterhome', views.recruiterhome, name='recruiterhome'),
    path('recruiterlogout', views.adminlogout, name='recruiterlogout'),

    path('viewemployees', views.viewemployees, name="viewemployees"),
    path('viewemployees1', views.viewemployees1, name="viewemployees1"),
    #path("deleteemployees/<int:eid>",views.deleteemployees,name="deleteemployees"),
    path('viewrecruiters', views.viewrecruiters, name="viewrecruiters"),
    path('cards', views.cards ,name="cards"),
    path('viewdetails', views.viewdetails ,name="viewdetails"),
    path('viewdetails1', views.viewdetails1 ,name="viewdetails1"),
    path('viewdetails2', views.viewdetails2 ,name="viewdetails2"),

     path('courses', views.courses ,name="courses"),
     path('enroll',views.enroll,name='enroll'),
     path('enrolled',views.enrolled,name='enrolled'),
    ]