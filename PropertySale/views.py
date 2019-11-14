from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Admin,PlotModel,ApartmentModel,EmployeeModel,UserModel
from django.contrib import messages
import csv
# Create your views here.
def showHome(request):
    return render(request,"showHome.html")

def login(request):
    usertype=request.POST.get("type")
    username=request.POST.get("u")
    password=request.POST.get("p")
    if usertype=="Admin":
        try:
            dat=Admin.objects.get(Username=username,Password=password)
            if dat:
                request.session["uid"]=dat.id
                return render(request,"adminHome.html",{"data":"Welcome Admin"})
        except:
            return render(request,"showHome.html",{"data":"Invalid details"})
    if usertype=="User":
        try:
            dat=UserModel.objects.get(name=username,password=password)
            if dat:
                request.session["uname"]=dat.name
                return render(request,"userHome.html",{"data":"Welcome User"})
        except:
            return render(request,"showHome.html",{"data":"Invalid details"})
def home(request):
    return render(request,"adminHome.html",{"data":"Welcome Admin"})
def logout(request):
    try:
        del request.session["uid"]
        return render(request, "showHome.html", {"data": " Successfully Logged Out"})
    except:
        return redirect('main')
def plot(request):
    return render(request,"plot.html")
def back(request):
    return render(request,"adminHome.html",{"data":"Welcome Admin"})
def apart(request):
    return render(request,"Apartment.html")
def employee(request):
    return render(request,"employee.html")
def reports(request):
    return render(request, "report.html")
def about(request):
    return render(request, "about.html")
def sales(request):
    return render(request, "sales.html")
def addPlot(request):
     return render(request, "AddPlot.html")
def cost(request):
    pn=request.POST.get("pn")
    rn=request.POST.get("rn")
    sn=request.POST.get("sn")
    sy=request.POST.get("sy")
    csy=request.POST.get("csy")
    oe=request.POST.get("oe")
    facing=request.POST.get("facing")
    status=request.POST.get("status")
    total_cost=(float(sy)*float(csy))+float(oe)
    return render(request,"AddPlot.html",{"total_cost":total_cost,"pn":pn,
                                          "rn":rn,"sn":sn,"csy":csy,"oe":oe,"facing":facing,"status":status,"sy":sy})

def plotsave(request):
    pn=request.POST.get("pn")
    rn=request.POST.get("rn")
    sn=request.POST.get("sn")
    sy=request.POST.get("sy")
    csy=request.POST.get("csy")
    oe=request.POST.get("oe")
    facing=request.POST.get("facing")
    status=request.POST.get("status")
    cost=request.POST.get("cost")
    image=request.FILES["image"]
    p=PlotModel(Plot_number=pn,Road_number=rn,Survey_number=sn,Square_yards=sy,
              Cost_per_saqare_yard=csy,Other_expences=oe,Facing=facing,Status=status,Total_cost=cost,Plot_image=image)
    p.save()
    messages.success(request,"data saved sucessfully")
    return redirect('AddPlot')

def viewplot(request):
    data=PlotModel.objects.all()
    return render(request,"viewplot.html",{"data":data})
def editPlot(request):
    data=PlotModel.objects.all()
    return render(request,"edit.html",{"data1":data})
def editone(request):
    id=request.GET.get("id")
    data=PlotModel.objects.filter(Survey_number=id)
    return render(request,"edit1.html",{"data1":data})
def delete(request):
    id = request.GET.get("id")
    PlotModel.objects.get(Survey_number=id).delete()
    return render(request,"edit.html")
def newapart(request):
    return render(request,"newapart.html")

def flatsave(request):
    fn = request.POST.get("fn")
    fp = request.POST.get("fp")
    rn = request.POST.get("rn")
    hn = request.POST.get("hn")
    sy = request.POST.get("sy")
    facing = request.POST.get("facing")
    status = request.POST.get("status")
    cost = request.POST.get("cost")
    image = request.FILES["image"]
    ApartmentModel(Flat_number=fn,Place=fp,Road_number=rn,House_number=hn,Square_yards=sy,
                   Facing=facing,Status=status,Cost=cost,Flat_image=image).save()
    messages.success(request,"data saved sucessfully")
    return redirect('newapart')

def viewapart(request):
    data=ApartmentModel.objects.all()
    return render(request,"viewApartment.html",{"data":data})

def editflat(request):
    id=request.GET.get("id")
    data1=ApartmentModel.objects.filter(House_number=id)
    return render(request,"editflat.html",{"data1":data1})


def deleteflat(request):
    hno=request.GET.get("id")
    ApartmentModel.objects.get(House_number=hno).delete()
    return redirect('viewapart')
def viewsoldplots(request):
    data=PlotModel.objects.filter(Status="sold")
    return render(request,"purchasedplots.html",{"data":data})

def viewsoldApartments(request):
    data=ApartmentModel.objects.filter(Status="sold")
    return render(request,'viewsoldApartments.html',{"data":data})
def addemp(request):
    return render(request,"AddEmployee.html")

def empsave(request):
    eid=request.POST.get("eid")
    ename=request.POST.get("ename")
    edesig=request.POST.get("edesig")
    email=request.POST.get("email")
    EmployeeModel(id=eid,Name=ename,Designation=edesig,Employee_mail=email).save()
    messages.success(request, "data saved sucessfully")
    return redirect('Addemp')

def viewemp(request):
    data=EmployeeModel.objects.all()
    return render(request,"viewmp.html",{"data":data})

def deleteemp(request):
    id=request.GET.get("id")
    EmployeeModel.objects.get(id=id).delete()
    return viewemp(request)

def dspr(request):
    response = HttpResponse(content_type='text/csv', )
    response['content-disposition'] = 'attachment;filename="dspr.csv"'

    writer = csv.writer(response)
    fd = PlotModel.objects.filter(Status="sold")
    writer.writerow(['Plot_number', 'Road_number', 'Survey_number', 'Square_yards', 'cost_per_sqareyard',
                     'other_Expences','Facing','Status','Total_cost'])
    for x in fd:
        writer.writerow([x.Plot_number,x.Road_number,x.Survey_number,x.Square_yards,x.Cost_per_saqare_yard,
                         x.Other_expences,x.Facing,x.Status,x.Total_cost])
    return response

def drpr(request):
    response = HttpResponse(content_type='text/csv', )
    response['content-disposition'] = 'attachment;filename="drpr.csv"'

    writer = csv.writer(response)
    fd = PlotModel.objects.filter(Status="Reserved")
    writer.writerow(['Plot_number', 'Road_number', 'Survey_number', 'Square_yards', 'cost_per_sqareyard',
                     'other_Expences','Facing','Status','Total_cost'])
    for x in fd:
        writer.writerow([x.Plot_number,x.Road_number,x.Survey_number,x.Square_yards,x.Cost_per_saqare_yard,
                         x.Other_expences,x.Facing,x.Status,x.Total_cost])
    return response

def dvpr(request):
    response = HttpResponse(content_type='text/csv', )
    response['content-disposition'] = 'attachment;filename="dvpr.csv"'

    writer = csv.writer(response)
    fd = PlotModel.objects.filter(Status="Vacant")
    writer.writerow(['Plot_number', 'Road_number', 'Survey_number', 'Square_yards', 'cost_per_sqareyard',
                     'other_Expences','Facing','Status','Total_cost'])
    for x in fd:
        writer.writerow([x.Plot_number,x.Road_number,x.Survey_number,x.Square_yards,x.Cost_per_saqare_yard,
                         x.Other_expences,x.Facing,x.Status,x.Total_cost])
    return response

def dsar(request):
    response = HttpResponse(content_type='text/csv', )
    response['content-disposition'] = 'attachment;filename="dsar.csv"'
    writer = csv.writer(response)
    fd = ApartmentModel.objects.filter(Status="sold")
    writer.writerow(['Flat_number', 'Flat_place','Road_number', 'House_number', 'Square_yards',
                     'Facing','Status','Total_cost'])
    for x in fd:
        writer.writerow([x.Flat_number,x.Place,x.Road_number,x.House_number,x.Square_yards,x.Facing,x.Status,x.Cost])
    return response
def drar(request):
    response = HttpResponse(content_type='text/csv', )
    response['content-disposition'] = 'attachment;filename="drar.csv"'
    writer = csv.writer(response)
    fd = ApartmentModel.objects.filter(Status="Reserved")
    writer.writerow(['Flat_number', 'Flat_place','Road_number', 'House_number', 'Square_yards',
                     'Facing','Status','Total_cost'])
    for x in fd:
        writer.writerow([x.Flat_number,x.Place,x.Road_number,x.House_number,x.Square_yards,x.Facing,x.Status,x.Cost])
    return response

def dvar(request):
    response = HttpResponse(content_type='text/csv', )
    response['content-disposition'] = 'attachment;filename="dvar.csv"'
    writer = csv.writer(response)
    fd = ApartmentModel.objects.filter(Status="Vacant")
    writer.writerow(['Flat_number', 'Flat_place','Road_number', 'House_number', 'Square_yards',
                     'Facing','Status','Total_cost'])
    for x in fd:
        writer.writerow([x.Flat_number,x.Place,x.Road_number,x.House_number,x.Square_yards,x.Facing,x.Status,x.Cost])
    return response

def addUser(request):
    return render(request,"adduser.html")

def usersave(request):
    uid=request.POST.get("uid")
    uname=request.POST.get("uname")
    email=request.POST.get("email")
    pword=request.POST.get('pword')
    cno=request.POST.get('cno')
    UserModel(uid=uid,name=uname,email=email,password=pword,contact_number=cno).save()
    messages.success(request, "data saved sucessfully")
    return redirect('addUser')
def viewuser(request):
    data=UserModel.objects.all()
    return render(request,'viewuser.html',{"data":data})
def deleteuser(request):
    id=request.GET.get("id")
    UserModel.objects.get(uid=id).delete()
    return viewuser(request)

def changepass(request):
    data=UserModel.objects.all()
    return render(request,"changepass.html",{"data":data})

def logout1(request):
    try:
        del request.session["uname"]
        return render(request, "showHome.html", {"data": " Successfully Logged Out"})
    except:
        return redirect('main')
def viewvacantplot(request):
    data=PlotModel.objects.filter(Status="Vacant")
    return render(request,"viewvacantplot.html",{"data":data})

def viewvacantapartments(request):
    data = ApartmentModel.objects.filter(Status="Vacant")
    return render(request, "viewvacantaprtment.html", {"data": data})
def dvpreports(request):
    response = HttpResponse(content_type='text/csv', )
    response['content-disposition'] = 'attachment;filename="dvpr.csv"'

    writer = csv.writer(response)
    fd = PlotModel.objects.filter(Status="Vacant")
    writer.writerow(['Plot_number', 'Road_number', 'Survey_number', 'Square_yards', 'cost_per_sqareyard',
                     'other_Expences','Facing','Status','Total_cost'])
    for x in fd:
        writer.writerow([x.Plot_number,x.Road_number,x.Survey_number,x.Square_yards,x.Cost_per_saqare_yard,
                         x.Other_expences,x.Facing,x.Status,x.Total_cost])
    return response

def dvareports(request):
    response = HttpResponse(content_type='text/csv', )
    response['content-disposition'] = 'attachment;filename="dvar.csv"'
    writer = csv.writer(response)
    fd = ApartmentModel.objects.filter(Status="Vacant")
    writer.writerow(['Flat_number', 'Flat_place','Road_number', 'House_number', 'Square_yards',
                     'Facing','Status','Total_cost'])
    for x in fd:
        writer.writerow([x.Flat_number,x.Place,x.Road_number,x.House_number,x.Square_yards,x.Facing,x.Status,x.Cost])
    return response