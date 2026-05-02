from django.db import models


class Address(models.Model):
    adr_id = models.AutoField(primary_key=True, blank=True)
    city = models.TextField()
    state = models.TextField()

    class Meta:
        managed = False
        db_table = "address"


class Categories(models.Model):
    ct_id = models.AutoField(primary_key=True, blank=True)
    slug = models.TextField()
    name = models.TextField()
    description = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = "categories"


class Customers(models.Model):
    cs_id = models.AutoField(primary_key=True, blank=True)
    cs_name = models.TextField()
    cs_lastname = models.TextField()
    birth_date = models.TextField(blank=True)
    email = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    address = models.ForeignKey(Address, models.DO_NOTHING, db_column="address")
    create_time = models.TextField()
    points = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "customers"


class Feedbacks(models.Model):
    fb_id = models.AutoField(primary_key=True, blank=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, db_column="customer")
    fb_date = models.TextField()
    feedback = models.TextField()

    class Meta:
        managed = False
        db_table = "feedbacks"


class Invoices(models.Model):
    inv_id = models.AutoField(primary_key=True, blank=True)
    cs = models.ForeignKey(Customers, models.DO_NOTHING)
    invoic_total = models.IntegerField()
    payment_total = models.IntegerField()

    class Meta:
        managed = False
        db_table = "invoices"


class OrderDetail(models.Model):
    od_id = models.AutoField(primary_key=True, blank=True)
    or_field = models.ForeignKey(
        "Orders", models.DO_NOTHING, db_column="or_id"
    )  # Field renamed because it was a Python reserved word.
    product = models.ForeignKey("Products", models.DO_NOTHING, db_column="product")
    unit_price = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = "order_detail"


class Orders(models.Model):
    or_id = models.AutoField(primary_key=True, blank=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, db_column="customer")
    or_data = models.TextField()
    status = models.ForeignKey("Status", models.DO_NOTHING, db_column="status")

    class Meta:
        managed = False
        db_table = "orders"


class PaymentMethod(models.Model):
    pym_id = models.AutoField(primary_key=True, blank=True)
    method = models.TextField()

    class Meta:
        managed = False
        db_table = "payment_method"


class Payments(models.Model):
    py_id = models.AutoField(primary_key=True, blank=True)
    invoices_inv = models.ForeignKey(Invoices, models.DO_NOTHING)
    customers_cs = models.ForeignKey(Customers, models.DO_NOTHING)
    py_date = models.TextField()
    amount = models.IntegerField()
    method = models.ForeignKey(PaymentMethod, models.DO_NOTHING, db_column="method")

    class Meta:
        managed = False
        db_table = "payments"


class Products(models.Model):
    pr_id = models.AutoField(primary_key=True)
    name = models.TextField()
    category = models.ForeignKey(Categories, models.DO_NOTHING, db_column="category")
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    amount_in_stock = models.IntegerField(blank=True, null=True)
    hot = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "products"


class Status(models.Model):
    st_id = models.AutoField(primary_key=True, blank=True)
    state = models.TextField()

    class Meta:
        managed = False
        db_table = "status"
