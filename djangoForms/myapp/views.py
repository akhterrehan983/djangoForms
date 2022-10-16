from django.forms import JSONField
from django.http import JsonResponse
from django.shortcuts import HttpResponse, redirect, render
from myapp.models import userForm,incidentReport
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"index.html")

def login(request):
    if request.method == "POST":
        uname = request.POST.get("uname",None)
        pwd = request.POST.get("pwd",None)
        obj = userForm.objects.filter(username=uname,password=pwd)
        if obj:
            request.session["username"] = uname
            messages.success(request,"Success: You are now logged in.")
            return redirect("/")
        else:
            messages.error(request,"Invalid Credentials!!!")
            return render(request,"login.html")
    return render(request,"login.html")

def logout(request):
    if "username" in request.session:
        del request.session["username"] 
    return redirect("/login")

def register(request):
    if request.method == "POST":
        uname = request.POST.get("uname",None)
        pwd = request.POST.get("pwd",None)
        obj = userForm.objects.filter(username=uname)
        if obj:
            messages.error(request,"Username already exists!!!")
            # return redirect("register")
        else:
            obj = userForm(username=uname, password=pwd)
            obj.save()
            messages.success(request,"User added successfully!!!")
            # return redirect("register")
    return render(request,"register.html")

def reportIncident(request):
    if request.method == "POST":
        # pass
        try:
            location = request.POST.get("location",None)
            incidentDepartment = request.POST.get("incidentDepartment",None)
            date = request.POST.get("date",None)
            time = request.POST.get("time",None)
            incidentLocation = request.POST.get("incidentLocation",None)
            initialSeverity = request.POST.get("initialSeverity",None)
            suspectedCause = request.POST.get("suspectedCause",None)
            immediateAction = request.POST.get("immediateAction",None)
            subIncidentTypes =  request.POST.getlist("subIncidentTypes[]")
            print(location,incidentDepartment,date,time,incidentLocation,initialSeverity,suspectedCause,immediateAction,subIncidentTypes)
            
            uobj = userForm.objects.get(username=request.session["username"])
            print(uobj)
            # try:
            obj = incidentReport(location=location, incidentDepartment=incidentDepartment, date=date, time=time, incidentLocation=incidentLocation, initialSeverity=initialSeverity, suspectedCause=suspectedCause, immediateAction=immediateAction, subIncidentTypes=subIncidentTypes,user=uobj)
            obj.save()
            messages.success(request,"Report added successfully!!!")
        except:
            messages.errro(request,"Something went wrong!!!")
    return render(request,"reportIncident.html")

def savedReports(request):
    objects = incidentReport.objects.all()
    print(objects)

    return render(request,"savedReports.html",{"objects":objects})

def savedReportSummary(request):
    id = int(request.POST.get("id"))
    obj = incidentReport.objects.filter(id=id)[0]
    print(obj)
    obj.date = str(obj.date)
    obj.time = str(obj.time)
    print(obj.subIncidentTypes,type(obj.subIncidentTypes))
    obj.subIncidentTypes = str(obj.subIncidentTypes)
    print(obj.subIncidentTypes)
    return render(request,"savedReportSummary.html",{"obj":obj})
    # return JsonResponse({"id":obj.location})