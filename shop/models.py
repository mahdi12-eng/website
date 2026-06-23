from django.db import models
from django.contrib.auth import get_user_model


###
User = get_user_model()


class Categories(models.Model):
    ct_id = models.AutoField(primary_key=True)
    name = models.CharField()
    description = models.TextField(blank=True)

    class Meta:
        db_table = "categories"

    def __str__(self) -> str:
        return f"{self.name}"


class Feedbacks(models.Model):
    fb_id = models.AutoField(primary_key=True, blank=True)
    user = models.ForeignKey(
        User, models.DO_NOTHING, db_column="user")
    fb_date = models.DateField(auto_now=False, auto_now_add=True)
    feedback = models.TextField()

    class Meta:
        db_table = "feedbacks"


class Invoices(models.Model):
    inv_id = models.AutoField(primary_key=True, blank=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    invoic_total = models.IntegerField()
    payment_total = models.IntegerField()

    class Meta:
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
        db_table = "order_detail"

    def __str__(self) -> str:
        return f"{self.product}-{self.unit_price}"


class Orders(models.Model):
    or_id = models.AutoField(primary_key=True, blank=True)
    user = models.ForeignKey(
        User, models.DO_NOTHING, db_column="customer")
    or_data = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.ForeignKey("Status", models.DO_NOTHING, db_column="status")

    class Meta:
        db_table = "orders"


class PaymentMethod(models.Model):
    pym_id = models.AutoField(primary_key=True, blank=True)
    method = models.CharField()

    class Meta:
        db_table = "payment_method"


class Payments(models.Model):
    py_id = models.AutoField(primary_key=True, blank=True)
    invoices_inv = models.ForeignKey(Invoices, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    py_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    amount = models.IntegerField()
    method = models.ForeignKey(
        PaymentMethod, models.DO_NOTHING, db_column="method")

    class Meta:
        db_table = "payments"

    def __str__(self) -> str:
        return f"{self.amount}-{self.method}"
# only for test


class Products(models.Model):
    pr_id = models.AutoField(primary_key=True)
    name = models.CharField()
    category = models.ForeignKey(
        Categories, models.DO_NOTHING, db_column="category")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    description = models.TextField(blank=True, null=True)
    image = models.CharField(null=True)
    amount_in_stock = models.IntegerField(blank=True, null=True)
    hot = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f"{self.pr_id}-{self.name}-{self.price}"

    class Meta:
        db_table = "products"


class Status(models.Model):
    st_id = models.AutoField(primary_key=True, blank=True)
    state = models.CharField()
    just_for_test = models.BooleanField(blank=True, null=True)
    test = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "status"
