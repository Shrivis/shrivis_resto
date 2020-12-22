from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_category = models.CharField(max_length=20, default="")
    p_subcategory = models.CharField(max_length=20, default="")
    p_name = models.CharField(max_length=50, default="")
    p_image = models.ImageField(upload_to="images", default="")
    p_type = models.CharField(max_length=10, default="veg")
    p_desc = models.CharField(max_length=300, default="")
    p_price = models.IntegerField(default=0)

    def __str__(self):
        return '{}, {}'.format(self.p_category, self.p_name)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_status = models.CharField(max_length=100, default="Failed")
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, default="")


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


class Reservation(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default="")
    email = models.CharField(max_length=20, default="")
    phone = models.CharField(max_length=15,)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    person = models.IntegerField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=300,)

    def __str__(self):
        return self.name
