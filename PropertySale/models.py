from django.db import models

# Create your models here.
class Admin(models.Model):
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
class PlotModel(models.Model):
    Plot_number=models.IntegerField()
    Road_number=models.IntegerField()
    Survey_number=models.IntegerField(primary_key=True)
    Square_yards=models.DecimalField(max_digits=20,decimal_places=2)
    Cost_per_saqare_yard=models.DecimalField(max_digits=50,decimal_places=2)
    Other_expences=models.DecimalField(max_digits=20,decimal_places=2)
    Facing=models.CharField(max_length=50)
    Status=models.CharField(max_length=50)
    Total_cost=models.DecimalField(max_digits=50,decimal_places=2)
    Plot_image=models.FileField(upload_to="images/")
class ApartmentModel(models.Model):
    Flat_number=models.IntegerField()
    Place=models.CharField(max_length=100,default=False)
    Road_number=models.IntegerField()
    House_number=models.IntegerField(primary_key=True)
    Square_yards=models.DecimalField(max_digits=20,decimal_places=2)
    Cost=models.DecimalField(max_digits=50,decimal_places=2)
    Facing=models.CharField(max_length=50)
    Status=models.CharField(max_length=50)
    Flat_image=models.FileField(upload_to="flatimages/")
class EmployeeModel(models.Model):
    id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=70)
    Designation=models.CharField(max_length=70)
    Employee_mail=models.EmailField()
class UserModel(models.Model):
    uid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=70)
    email=models.EmailField()
    password=models.CharField(max_length=70)
    contact_number=models.IntegerField()