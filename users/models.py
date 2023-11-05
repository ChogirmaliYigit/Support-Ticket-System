import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from users.querysets.user import UserManager
from users.utils.langs import SUPPORTED_LANGUAGES


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=2000)
    last_name = models.CharField(max_length=2000, null=True, blank=True)
    username = None
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to="profile_images/", null=True, blank=True)
    language = models.CharField(max_length=5, choices=SUPPORTED_LANGUAGES, null=True, blank=True)
    confirmation_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    referral_code = models.CharField(max_length=20, null=True, blank=True)
    invited_code = models.CharField(max_length=20, null=True, blank=True)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    @property
    def has_company(self):
        return self.companies.count() > 0

    class Meta:
        db_table = "users"


class Company(models.Model):
    name = models.CharField(max_length=500)
    logo = models.ImageField(upload_to="company_logos/", null=True, blank=True)
    description = models.TextField()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def make_verify_account(self):
        if not self.is_verified:
            self.is_verified = True
            self.save()

    class Meta:
        db_table = "companies"


class Member(models.Model):
    ADMIN = 'admin'
    MANAGER = "manager"

    ROLES = (
        (ADMIN, "Admin"),
        (MANAGER, "Manager"),
    )

    company = models.ForeignKey(Company, models.CASCADE, "members")
    user = models.ForeignKey(User, models.CASCADE, "companies")
    role = models.CharField(max_length=20, choices=ROLES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
