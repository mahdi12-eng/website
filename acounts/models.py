from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class Address(models.Model):
    adr_id = models.AutoField(primary_key=True, blank=True)
    city = models.CharField()
    state = models.CharField()

    class Meta:
        db_table = "address"

    def __str__(self) -> str:
        return f"{self.city}-{self.state}"


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("email must be set!")
        if kwargs["address"]:
            kwargs["address"] = Address.objects.get(
                adr_id=int(kwargs["address"]))
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)
        if kwargs.get("is_staff") is not True:
            raise ValueError("invalid operation")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("invalid operation")
        return self.create_user(email, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    """
    custom customer user model
    """
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField(unique=True)
    address = models.ForeignKey(
        Address, models.DO_NOTHING, db_column="address")
    created_date = models.DateField(auto_now_add=True)
    points = models.IntegerField(default=0)
    ####
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "last_name", "birth_date", "address"]
    is_active = models.BooleanField(default=True)
    is_verivied = models.BooleanField(default=False)

    objects = UserManager()

    def __str__(self):
        return self.email
