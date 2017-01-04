from django.shortcuts import render
from  django.http import HttpResponse
from  django.template import  loader,Context
import  datetime
from website.models import Student
# Create your views here.

class Person(object):
    def __init__(self,name,sex,age):
        self.name=name
        self.age=age
        self.sex=sex
    def say(self):
        return "my name is"+self.name
def index(request):
    t=loader.get_template("index.html")
    user={'name':'tom','age':22,'sex':'male'}
    person=Person("jack",25,"female")
    book_list=['python','ruby','java','c']
    c=Context({'title':'django','user':person,'book_list':book_list,'today':datetime.datetime.now()})
    return  HttpResponse(t.render(c))

def time(request):
    time=loader.get_template('time.html')
    id=request.GET.get("id")
    name=request.GET.get("name")
    c=Context({'today':datetime.datetime.now(),'id':id,'name':name})
    return HttpResponse(time.render(c))
def foo(request,p1):
    t=loader.get_template("time.html")
    c=Context({"today":datetime.datetime.now(),'id':p1})
    return  HttpResponse(t.render(c))

def bar(request,id,name):
    t=loader.get_template("time.html")
    c=Context({"today":datetime.datetime.now(),'id':id,'name':name})
    return  HttpResponse(t.render(c))

def student_list(request):
    t=loader.get_template("studentlist.html")
    studentlist=Student.objects.all().order_by("age")
    c=Context({"studentlist":studentlist})
    return  HttpResponse(t.render(c))

