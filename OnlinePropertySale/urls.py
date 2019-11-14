"""OnlinePropertySale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from OnlinePropertySale import settings
from PropertySale import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showHome,name="main"),
    path('login/',views.login,name='login'),
    path('Home/',views.home,name="Home"),
    path('logout/',views.logout,name='logout'),
    path('plot/',views.plot,name='plot'),
    path('back/',views.back,name='back'),
    path('apart/',views.apart,name='apart'),
    path('emp/',views.employee,name='emp'),
    path('reports/',views.reports,name='reports'),
    path('about/',views.about,name='about'),
    path('sales/',views.sales,name='sales'),
    path('AddPlot/',views.addPlot,name='AddPlot'),
    path('cost/',views.cost,name='cost'),
    path('plotsave/',views.plotsave,name='plotsave'),
    path('viewplot/',views.viewplot,name='viewplot'),
    path('editplot/',views.editPlot,name="editplot"),
    path('edit1',views.editone,name='edit1'),
    path('delete/',views.delete,name='delete'),
    path('newapart/',views.newapart,name='newapart'),
    path('flatsave/',views.flatsave,name='flatsave'),
    path('viewapart/',views.viewapart,name='viewapart'),
    path('editflat/',views.editflat,name='editflat'),
    path('deleteflat/',views.deleteflat,name='deleteflat'),
    path('viewsoldplots/',views.viewsoldplots,name='viewsoldplots'),
    path('viewsoldApartments/',views.viewsoldApartments,name='viewsoldApartments'),
    path('Addemp/',views.addemp,name='Addemp'),
    path('empsave/',views.empsave,name='empsave'),
    path('viewemp/',views.viewemp,name='viewemp'),
    path('deleteemp/',views.deleteemp,name='deleteemp'),
    path('dspr/',views.dspr,name='dspr'),
    path('drpr/',views.drpr,name='drpr'),
    path('dvpr/',views.dvpr,name='dvpr'),
    path('dsar/',views.dsar,name='dsar'),
    path('drar/',views.drar,name='drar'),
    path('dvar/',views.dvar,name='dvar'),
    path('addUser/',views.addUser,name='addUser'),
    path('usersave/',views.usersave,name='usersave'),
    path('viewuser/',views.viewuser,name='viewuser'),
    path('deleteuser/',views.deleteuser,name='deleteuser'),
    path('changepass/',views.changepass,name='changepass'),
    path('logout1/',views.logout1,name='logout1'),
    path('viewvacantplot/',views.viewvacantplot,name='viewvacantplot'),
    path('viewvacantapartments/',views.viewvacantapartments,name='viewvacantapartments'),
    path('dvpreports/',views.dvpreports,name='dvpreports'),
    path('dvareports/',views.dvareports,name='dvareports')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
