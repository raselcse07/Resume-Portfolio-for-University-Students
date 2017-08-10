import datetime
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.conf import settings
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from .utils import Key_Generator
from django.core.mail import send_mail
from Academic.models import Department
from Academic.utils import year_dropdown


USERNAME_REGEX="^[a-zA-Z0-9.+_-]*$"



class MyUserManager(BaseUserManager):

    def create_user(self, username,email, password=None):

        """
        Creates and saves a User with the given username, email and password.
        """

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(

            username    =username,
            email       =self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email, password):

        """
        Creates and saves a User with the given username, email and password.
        """

        user            = self.create_user(

                            username,
                            email,
                            password=password,
                        )

        user.is_admin   = True
        user.is_staff   =True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):

    username        =models.CharField(

                        max_length=250,
                        validators=[
                                RegexValidator(

                                    regex   =USERNAME_REGEX,
                                    message ='Username must be Alphanumeric or contain any of this ". + _ - "',
                                    code    ='Invalid Username '
                        )],
                        unique=True
                    )

    email              = models.EmailField(
                        verbose_name='email address',
                        max_length=255,
                        unique=True,
                        )

    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_admin        = models.BooleanField(default=False)

    objects         = MyUserManager()

    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):

        return self.email

    def get_short_name(self):

        return self.email

    def __str__(self):          # __unicode__ on Python 2

        return self.username

    def has_perm(self, perm, obj=None):


        return True

    def has_module_perms(self, app_label):

        return True



class ActivationProfile(models.Model):

    user        =models.ForeignKey(settings.AUTH_USER_MODEL)
    key         =models.CharField(max_length=120)
    expired     =models.BooleanField(default=False)

    def save(self,*args,**kwargs):
        self.key=Key_Generator()
        super(ActivationProfile,self).save(*args,**kwargs)

        subject = 'Activate Account'
        from_email = settings.DEFAULT_FROM_EMAIL
        message = "http://127.0.0.1:8000/students/activate/"+self.key
        recipient_list = [self.user.email]

        sent_mail=send_mail(
                            subject,
                            message,
                            from_email,
                            recipient_list,
                            fail_silently=False,
                            )
        return sent_mail

    def __str__(self):

        return str(self.user.username)

    class Meta:

        ordering=["user"]



class Profile(models.Model):

    user                =models.OneToOneField(settings.AUTH_USER_MODEL)
    first_name          =models.CharField(max_length=250,default="")
    last_name           =models.CharField(max_length=250,default="")
    fathers_name        =models.CharField(max_length=250,default="")
    mothers_name        =models.CharField(max_length=250,default="")
    dept_name           =models.ForeignKey(Department,on_delete=models.CASCADE,default="")
    reg_number          =models.CharField(max_length=120,default="")
    academic_year       =models.IntegerField(('Academic Year'),choices=year_dropdown,default=datetime.datetime.now().year)
    CGPA                =models.CharField(max_length=250,default="")

    class Meta:

        ordering=["reg_number"]

    def __str__(self):

        return str(self.user.username)

    def get_absolute_url(self):

        return reverse("Academic:detail",kwargs={"dept_name":self.dept_name,"dept_session":self.academic_year,"reg_number":self.reg_number})

def post_save_user_model_receiver(sender,instance,created,*args,**kwargs):

    if created:

        try:
            ActivationProfile.objects.create(user=instance)
        except:
            pass

post_save.connect(post_save_user_model_receiver,sender=settings.AUTH_USER_MODEL)
