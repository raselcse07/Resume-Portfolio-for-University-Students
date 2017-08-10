from django.db import models
from django.conf import settings



def UploadLocation(instance,filename):

    return "CV/%s/%s" % (instance.user,filename)

def upoload_location_for_image(instance,filename):

    return "Student Image/%s/%s/%s" %(instance.user,instance.full_name,filename)

def upoload_location_for_portfolio(instance,filename):

    return "Student Image/%s/%s" %(instance.user,filename)

def upoload_location_for_client(instance,filename):

    return "Client Image/%s/%s" %(instance.user,filename)


class UploadCV(models.Model):


    user        =models.OneToOneField(settings.AUTH_USER_MODEL)
    cv          =models.FileField(upload_to=UploadLocation,default="",verbose_name="Resume",help_text="File must be pdf.")
    is_publish  =models.BooleanField(default=False,help_text="If you want to display this Resume then check it.Otherwise don't check")

    def __str__(self):

        return str(self.user.username)


    class Meta:

        ordering=["user"]
        verbose_name="Resume"
        verbose_name_plural="Resume"


class AdditionalInfo(models.Model):


    user                        =models.OneToOneField(settings.AUTH_USER_MODEL)


    student_image               =models.ImageField(upload_to=upoload_location_for_image,
                                       height_field="height_field",
                                       width_field="width_field",
                                )

    height_field                =models.IntegerField(default=100)
    width_field                 =models.IntegerField(default=100)
    full_name                   =models.CharField(max_length=200)
    fathers_name                =models.CharField(max_length=200)
    mothers_name                =models.CharField(max_length=200)
    present_address             =models.TextField()
    birthday                    =models.CharField(max_length=50,help_text="Example : 05 September,1995")
    cell_number                 =models.CharField(max_length=200)
    email                       =models.EmailField(
                                              verbose_name='Email Address',
                                              max_length=255,
                                              unique=True                                              )

    about                       =models.TextField()
    professional_certification  =models.TextField(blank=True)
    work_position               =models.CharField(max_length=200,help_text="Example : Web Developer")




    def __str__(self):

        return str(self.user.username)

    class Meta:

        ordering=["user"]
        verbose_name="Additional Information"
        verbose_name_plural="Additional Informations"

class TechnicalSkills(models.Model):

    user                        =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    skills                      =models.CharField(max_length=200)
    skill_level                 =models.CharField(max_length=200,help_text="Example: 90%")

    class Meta:

        ordering=["user"]
        verbose_name="Technical Skill"
        verbose_name_plural="Technical Skills"

    def __str__(self):

        return str(self.user.username)

class Education(models.Model):

    user                        =models.ForeignKey(settings.AUTH_USER_MODEL)
    institute_name              =models.CharField(max_length=200)
    degree                      =models.CharField(max_length=200)
    passing_year                =models.CharField(max_length=50)

    class Meta:

        ordering=["user"]
        verbose_name="Education"
        verbose_name_plural="Educations"

    def __str__(self):

        return str(self.user.username)

class WorkHistory(models.Model):

    user                        =models.ForeignKey(settings.AUTH_USER_MODEL)
    company_name                =models.CharField(max_length=200)
    position                    =models.CharField(max_length=200,default="")
    start_date                  =models.CharField(max_length=200,help_text="Format: 10 Jan,2017")
    end_date                    =models.CharField(max_length=200,help_text="Format: 10 Jan,2017")

    class Meta:

        ordering=["user"]
        verbose_name="Work History"
        verbose_name_plural="Work Historys"

    def __str__(self):

        return str(self.user.username)



class Portfolio(models.Model):

    user                        =models.ForeignKey(settings.AUTH_USER_MODEL)
    project_name                =models.CharField(max_length=200)
    project_type                =models.CharField(max_length=200,help_text="Example : Web Development",default="")
    clients                     =models.CharField(max_length=200,default="")
    project_image               =models.ImageField(upload_to=upoload_location_for_portfolio,
                                       height_field="height_field",
                                       width_field="width_field",
                                )
    height_field                =models.IntegerField(default=100)
    width_field                 =models.IntegerField(default=100)
    project_url                 =models.CharField(max_length=200,blank=True)
    project_description         =models.CharField(max_length=200)

    def __str__(self):

        return str(self.user.username)


class Service(models.Model):

    user                        =models.ForeignKey(settings.AUTH_USER_MODEL)
    service_type                =models.CharField(max_length=200,help_text="Example : Web Development")
    little_description          =models.TextField()

    class Meta:

        verbose_name="Service"
        verbose_name_plural="Services"

    def __str__(self):

        return str(self.user.username)


class Succeess(models.Model):

    user                        =models.ForeignKey(settings.AUTH_USER_MODEL)
    total_complete_project      =models.CharField(max_length=100)
    total_happy_clients         =models.CharField(max_length=100)
    awards_won                  =models.CharField(max_length=100)
    total_ongoing_project       =models.CharField(max_length=100)

    class Meta:

        ordering=["user"]
        verbose_name="Succeess"
        verbose_name_plural="Succeess"

    def __str__(self):

        return str(self.user.username)


class WorkingProcess(models.Model):

    user                        =models.ForeignKey(settings.AUTH_USER_MODEL)
    title                       =models.CharField(max_length=100,help_text="Discuss Idea")
    short_note                  =models.CharField(max_length=100)

    class Meta:

        verbose_name="WorkingProcess"
        verbose_name_plural="WorkingProcess"

    def __str__(self):

        return str(self.user.username)


class Clients(models.Model):


    user                        =models.ForeignKey(settings.AUTH_USER_MODEL)
    name_of_clients             =models.CharField(max_length=200,default="")
    client_image                =models.ImageField(upload_to=upoload_location_for_client,
                                           height_field="height_field",
                                           width_field="width_field",
                                    )
    height_field                =models.IntegerField(default=100)
    width_field                 =models.IntegerField(default=100)

    class Meta:

        ordering=["user"]
        verbose_name="Client"
        verbose_name_plural="Clients"

    def __str__(self):

        return str(self.user.username)
