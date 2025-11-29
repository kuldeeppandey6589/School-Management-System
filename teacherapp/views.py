from django.shortcuts import render,redirect
from adminapp.models import Teacher
from django.views.decorators.cache import cache_control
from django.core.files.storage import FileSystemStorage

# Create your views here.
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def teacherhome(req):
    try:
        if req.session['teacherid']!=None:
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            return render(req,'teacherhome.html',{'teacher':teacher})
    except KeyError:
        return redirect('login')
    
@cache_control(no_store=True,no_cache=True,must_revalidate=True)    
def teacherprofile(req):
    try:    
        if req.session['teacherid']!=None:
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            if req.method=="POST":
                name=req.POST['name']
                fname=req.POST['fname']
                mname=req.POST['mname']
                gender=req.POST['gender']
                dob=req.POST['dob']
                contactno=req.POST['contactno']
                address=req.POST['address']
                qualification=req.POST['qualification']
                Teacher.objects.filter(emailaddress=teacherid).update(name=name,fname=fname,mname=mname,gender=gender,dob=dob,contactno=contactno,address=address,qualification=qualification)
                return redirect('teacherapp:teacherprofile')
            return render(req,'teacherprofile.html',{'teacherid':teacherid,'teacher':teacher})
    except KeyError:
        return redirect('login')
    
@cache_control(no_store=True,no_cache=True,must_revalidate=True)    
def teacherlogout(req):
    try:
        if req.session['teacherid']!=None:
            del req.session['teacherid']
            return redirect('login')
    except KeyError:
        return redirect('login')       
    
def uploadpic(req):
    if req.method=="POST":
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            pic=req.FILES['pic']
            fs=FileSystemStorage()
            filename=fs.save(pic.name,pic)
            teacher.pic=filename
            teacher.save()
            return redirect('teacherapp:teacherprofile')
        
def tchangepass(req):
        try:
            if req.session['teacherid']!=None:
                teacherid=req.session['teacherid']
                teacher=Teacher.objects.get(emailaddress=teacherid)
                if req.method=="POST":
                    oldpassword=req.POST['oldpassword']
                    newpassword=req.POST['newpassword']
                    cnfpassword=req.POST['cnfpassword']
                    if newpassword!=cnfpassword:
                        msg="Please enter same password"
                        return render(req,'tchangepass.html',{'msg':msg})
                    elif teacher.password!=oldpassword:
                        msg="Wrong Password"
                        return render(req,'tchangepass.html',{'msg':msg})
                    elif teacher.password==oldpassword:
                        Teacher.objects.filter(emailaddress=teacherid).update(password=newpassword)
                        return redirect('teacherapp:teacherlogout')
                return render(req,'tchangepass.html',{'teacher':teacher})
        except KeyError:
            return redirect('login')
        
        