from django.shortcuts import render,redirect
from . models import Enquiry,Adminlogin
import datetime
from django.core.exceptions import ObjectDoesNotExist
from adminapp.models import Teacher
# Create your views here.
def index(req):
    return render(req,"index.html")
def about(req):
    return render(req,'about.html')
def contact(req):
    if req.method=="POST":
        name=req.POST['name']
        gender=req.POST['gender']
        address=req.POST['address']
        contactno=req.POST['contactno']
        emailaddress=req.POST['emailaddress']
        enquirytext=req.POST['enquirytext']
        enquirydate=datetime.datetime.today()
        enq=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext,enquirydate=enquirydate)
        enq.save()
        msg="Your Enquiry is submitted successfully"
        return render(req,'contact.html',{'msg':msg})
    return render(req,'contact.html')

def login(req):
    return render(req,'login.html')

def logcode(req):
    if req.method=="POST":
        usertype=req.POST['usertype']
        userid=req.POST['userid']
        password=req.POST['password']
        if usertype=="admin":
            try:
                user=Adminlogin.objects.get(userid=userid,password=password)
                if user is not None:
                    req.session['adminid']=userid
                    return redirect('adminapp:adminhome')
            except ObjectDoesNotExist:
                return render(req,'login.html',{'msg':"Invalid User"})
        elif usertype=="teacher":
            try:
                teacher=Teacher.objects.get(emailaddress=userid,password=password)
                if teacher is not None:
                    req.session['teacherid']=userid
                    return redirect('teacherapp:teacherhome')
            except ObjectDoesNotExist:
                return render(req,'login.html',{'msg':'invalid user'})    
        else:
            return render(req,'login.html',{'msg':"Abhi student add nhi hai"})    
            
def academic(req):
    return render(req,'academic.html')            

def media(req):
    return render(req,'media.html')