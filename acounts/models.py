from django.db import models

# Create your models here.


class Address(models.Model):
    adr_id = models.AutoField(primary_key=True, blank=True)
    city = models.CharField()
    state = models.CharField()

    class Meta:
        managed = False
        db_table = "address"

    def __str__(self) -> str:
        return f"{self.city}-{self.state}"


class Customers(models.Model):
    cs_id = models.AutoField(primary_key=True, blank=True)
    cs_name = models.CharField(max_length=50)
    cs_lastname = models.CharField()
    email = models.EmailField(max_length=254)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    phone = models.CharField(blank=True, null=True)
    address = models.ForeignKey(
        Address, models.DO_NOTHING, db_column="address")
    create_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    points = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "customers"

    def __str__(self) -> str:
        return f"{self.cs_name} {self.cs_lastname}-{self.email}-{self.points}"


class PaymentMethod(models.Model):
    pym_id = models.AutoField(primary_key=True, blank=True)
    method = models.CharField()

    class Meta:
        managed = False
        db_table = "payment_method"


class Payments(models.Model):
    py_id = models.AutoField(primary_key=True, blank=True)
    invoices_inv = models.ForeignKey(Invoices, models.DO_NOTHING)
    customers_cs = models.ForeignKey(Customers, models.DO_NOTHING)
    py_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    amount = models.IntegerField()
    method = models.ForeignKey(
        PaymentMethod, models.DO_NOTHING, db_column="method")
