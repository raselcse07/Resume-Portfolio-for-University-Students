from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from .models import USERNAME_REGEX
from django.core.validators import RegexValidator
from django.db.models import Q
from .models import Profile



User=get_user_model()



class UserLoginForm(forms.Form):

    query        =forms.CharField(label='Username/Email')
    password     = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):

        query       =self.cleaned_data.get('query')
        password    =self.cleaned_data.get('password')

        user_qs=User.objects.filter(

                                Q(username__iexact=query)|
                                Q(email__iexact=query)
                            ).distinct()

        if not user_qs.exists() and user_qs.count() != 1:
            raise forms.ValidationError("Invalid credentials --Username/Email not exists")

        user_obj    =user_qs.first()

        if not user_obj.check_password(password):

            raise forms.ValidationError("Invalid credentials --Invalid Password")

        if not user_obj.is_active:

            raise forms.ValidationError("Inactive User.Please verify your email.")

        self.cleaned_data["user_obj"]=user_obj

        return super(UserLoginForm,self).clean(*args,**kwargs)


class UserCreationForm(forms.ModelForm):


    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email',)

    def clean_password2(self):

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):

        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active=False
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username','email', 'password', 'is_staff', 'is_active', 'is_admin')

    def clean_password(self):

        return self.initial["password"]

class ProfileUpdateForm(forms.ModelForm):

    class Meta:

        model = Profile
        fields = (
        'first_name',
        'last_name',
        'fathers_name',
        'mothers_name',
        'dept_name',
        'reg_number',
        'academic_year',
        'CGPA',
        )

class ProfileCreateForm(forms.ModelForm):

    class Meta:

        model=Profile

        fields = (
        'first_name',
        'last_name',
        'fathers_name',
        'mothers_name',
        'dept_name',
        'reg_number',
        'academic_year',
        'CGPA',
        )
