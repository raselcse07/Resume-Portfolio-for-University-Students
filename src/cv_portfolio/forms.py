from django import forms
from .models import (
                AdditionalInfo,
                UploadCV,
                Portfolio,
                TechnicalSkills,
                Education,
                WorkHistory,
                Service,
                Succeess,
                WorkingProcess,
                Clients
                )


class AdditinalInfoCreationForm(forms.ModelForm):

    class Meta:

        model=AdditionalInfo
        exclude = ['user']

class ResumeUploadForm(forms.ModelForm):

    class Meta:

        model=UploadCV
        exclude = ['user']


class PortfolioForm(forms.ModelForm):

    class Meta:

        model=Portfolio
        exclude = ['user']

class TechnicalSkillCreateForm(forms.ModelForm):

    class Meta:

        model=TechnicalSkills
        exclude = ['user']


class EducationalInfoForm(forms.ModelForm):

    class Meta:

        model=Education
        exclude = ['user']


class WorkHistoryForm(forms.ModelForm):

    class Meta:

        model=WorkHistory
        exclude = ['user']


class ServiceCreationForm(forms.ModelForm):

    class Meta:

        model=Service
        exclude = ['user']


class SuccessCreationForm(forms.ModelForm):

    class Meta:

        model=Succeess
        exclude = ['user']


class WorkingProcessCreationForm(forms.ModelForm):

    class Meta:

        model=WorkingProcess
        exclude = ['user']

class ClientsCreationForm(forms.ModelForm):

    class Meta:

        model=Clients
        exclude = ['user']
