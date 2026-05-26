from django.db import models


class Categories(models.Model):
    ct_id = models.AutoField(primary_key=True, blank=True)
    name = models.CharField()
    description = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = "categories"

    def __str__(self) -> str:
        return f"{self.name}"


class Feedbacks(models.Model):
    fb_id = models.AutoField(primary_key=True, blank=True)
    customer = models.ForeignKey(
        Customers, models.DO_NOTHING, db_column="customer")
    fb_date = models.DateField(auto_now=False, auto_now_add=True)
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

    def __str__(self) -> str:
        return f"{self.invoic_total}/{self.payment_total}"


class OrderDetail(models.Model):
    od_id = models.AutoField(primary_key=True, blank=True)
    or_field = models.ForeignKey(
        "Orders", models.DO_NOTHING, db_column="or_id"
    )  # Field renamed because it was a Python reserved word.
    product = models.ForeignKey(
        "Products", models.DO_NOTHING, db_column="product")
    unit_price = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = "order_detail"

    def __str__(self) -> str:
        return f"{self.product}-{self.unit_price}"


class Orders(models.Model):
    or_id = models.AutoField(primary_key=True, blank=True)
    customer = models.ForeignKey(
        Customers, models.DO_NOTHING, db_column="customer")
    or_data = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.ForeignKey("Status", models.DO_NOTHING, db_column="status")

    class Meta:
        managed = False
        db_table = "orders"

    class Meta:
        managed = False
        db_table = "payments"

    def __str__(self) -> str:
        return f"{self.amount}-{self.method}"


class Products(models.Model):
    pr_id = models.AutoField(primary_key=True)
    name = models.CharField()
    category = models.ForeignKey(
        Categories, models.DO_NOTHING, db_column="category")
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.CharField(null=True)
    amount_in_stock = models.IntegerField(blank=True, null=True)
    hot = models.BooleanField(blank=True, null=True)
    saved_time = models.TimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f"{self.pr_id}-{self.name}-{self.price}"

    class Meta:
        managed = False
        db_table = "products"


class Status(models.Model):
    st_id = models.AutoField(primary_key=True, blank=True)
    state = models.CharField()

    class Meta:
        managed = False
        db_table = "status"
