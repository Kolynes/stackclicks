from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from utils.code_generator import generate_code

class UserManager(BaseUserManager):
	def create_user(self, email, first_name, last_name, password=None):
		if not email:
			raise ValueError('Email must be set!')
		user = self.model(email=email, first_name=first_name, last_name=last_name)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, first_name, last_name, password):
		user = self.create_user(email, first_name, last_name, password)
		user.is_superuser = True
		user.is_staff = True
		user.save()
		return user

class UserModel(AbstractBaseUser, PermissionsMixin):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	date_joined = models.DateTimeField(auto_now_add=True)
	last_login = models.DateTimeField(auto_now=True)
	referral_code = models.CharField(max_length=6, unique=True)
	referee = models.ForeignKey("UserModel", on_delete=models.CASCADE, related_name="referrals", null=True, blank=True, editable=False)
	bank_name = models.CharField(max_length=50, null=True)
	account_number = models.CharField(max_length=10, null=True)
	account_name = models.CharField(max_length=30, null=True)
	balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	referral_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

	REQUIRED_FIELDS = ["first_name", "last_name"]
	USERNAME_FIELD = "email"
	EMAIL_FIELD = "email"

	objects = UserManager()

	def __str__(self):
		return "%s %s" %(self.first_name, self.last_name)

	@property
	def fullname(self):
		return "%s %s" %(self.first_name, self.last_name)

	@property
	def dict(self):
		return {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
			"referralCode": self.referral_code,
			"referralCount": self.referrals.count(),
            "id": self.id,
			"bankName": self.bank_name,
			"accountNumber": self.account_number,
			"accountName": self.account_name,
			"balance": float(self.balance),
			"referralBalance": float(self.referral_balance),
        }
	
	def save(self, *args, **kwargs):
		if not self.referral_code:
			self.referral_code = generate_code(6)
		super().save(*args, **kwargs)

	class Meta:
		verbose_name = "User"
