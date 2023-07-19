from ast import If
from pyexpat.errors import messages
from urllib.robotparser import RequestRate
from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import student
from .models import Login

# Create your views here
def chooseproject(request):
    return render(request,'student/chooseproject.html',{})

def homepage1(request):
    return render(request,'student/homepage1.html',{})

def activestudent(request):
    return render(request,'student/activestudent.html',{})


def homepage(request): 
        return render(request, 'student/homepage.html',{})


def page1(request):
    student_info = student.objects.all()
    return render(request,'student/page1.html',{'student_info':student_info})

def delete(request, id):
    member = student.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('page1'))


def update(request, id):
    mystudent = student.objects.get(id=id)
    return render(request,'student/update.html',{'mystudent':mystudent})


def updaterecord(request, id):
    if request.method == 'POST':
        studentName = request.POST['studentname']
        studentId = request.POST['studentid']
        Birthday = request.POST['birthday']
        Gpa = request.POST['gpa']
        Level = request.POST['level']
        Gender = request.POST['gender']
        Email = request.POST['email']
        phoneNumber = request.POST['phonenumber']
        Department = request.POST['department']
        Status = request.POST['status']
        member = student.objects.get(id=id)
        member.studentname = studentName
        member.studentid = studentId
        member.birthday = Birthday
        member.gpa = Gpa
        member.level = Level
        member.gender = Gender
        member.email = Email
        member.phonenumber = phoneNumber
        member.department = Department
        member.status = Status
        member.save()
    return HttpResponseRedirect(reverse('page1'))


def page2(request):
    if request.method == 'POST':
        studentName = request.POST['studentname']
        studentId = request.POST['studentid']
        Birthday = request.POST['birthday']
        Gpa = request.POST['gpa']
        Level = request.POST['level']
        Gender = request.POST['gender']
        Email = request.POST['email']
        phoneNumber = request.POST['phonenumber']
        Department = request.POST['department']
        Status = request.POST['status']
        data = student(studentname=studentName,studentid=studentId,birthday=Birthday,gpa=Gpa,level=Level,gender=Gender,email=Email,phonenumber=phoneNumber,department=Department,status=Status)
        data.save()

    return render(request,'student/page2.html',{})


def page3(request):
    return render(request,'student/page3.html',{})


def page4(request):
    s=student.objects.all().values()
    x={'stu':s.filter()}
    return render(request,'student/page4.html',x)

def page5(request):
    return render(request,'student/page5.html',{})

def cs(request):
    return render(request,'student/cs.html',{})


def cscourse(request):
    return render(request,'student/cscourse.html',{})

def ds(request):
    return render(request,'student/ds.html',{})

def dscourse(request):
    return render(request,'student/dscourse.html',{})


def generalcourse(request):
    return render(request,'student/generalcourse.html',{})

def IS(request):
    return render(request,'student/IS.html',{})

def iscourse(request):
    return render(request,'student/iscourse.html',{})


def it(request):
    return render(request,'student/it.html',{})

def itcourse(request):
    return render(request,'student/itcourse.html',{})



