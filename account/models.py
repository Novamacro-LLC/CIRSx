from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccoutManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, address, city, state, post_code, country,
                    password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must provide a user name')
        if not first_name:
            raise ValueError('Users must provide a first name')
        if not last_name:
            raise ValueError('Users must provide a last_name')
        if not address:
            raise ValueError('Users must provide an address')
        if not city:
            raise ValueError('Users must provide a city')
        if not state:
            raise ValueError('Users must provide a state/province/region')
        if not post_code:
            raise ValueError('User must provide a postal code')
        if not country:
            raise ValueError('User must provide a country')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            address=address,
            city=city,
            state=state,
            post_code=post_code,
            country=country)

        user.set_password(using=self._db)
        user.save(user=self._db)
        return user


    def create_superuser(self, email, username, first_name, last_name, address, city, state, post_code, country,
                    password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            address=address,
            city=city,
            state=state,
            post_code=post_code,
            country=country,
            password=password)

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=150, unique=True)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    post_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=25)
    country = models.CharField(max_length=50, default='USA')
    #Do you want country to be in a drop down?  Are there countries that you do not operate in?
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',
                       'first_name',
                       'last_name',
                       'address',
                       'city',
                       'state',
                       'post_code',
                       'country']

    objects = MyAccoutManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


