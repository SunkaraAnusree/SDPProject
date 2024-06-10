from django import forms
from .models import Registration, Contactus, Admin, RecruiterRegistration, Enroll


class DateInput(forms.DateInput):
    input_type = "date"



class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"
        widgets = {"password":forms.PasswordInput()}

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"                 # it will display all the fields the forms except default fields like id and registrationtime
        widgets = {"password":forms.PasswordInput(),"dateofbirth":DateInput()}  # additional features of the fields
        labels = {"gender":"Select Gender","location":"Provide Location"}  #using this, we can change label name in the form
        #exclude = {"gender"}       #using this, we can hide the fields in the form

class ContactusForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = "__all__"                 # it will display all the fields the forms except default fields like id and registrationtime
        #widgets = {"password":forms.PasswordInput(),"dateofbirth":DateInput()}  # additional features of the fields
        #labels = {"gender":"Select Gender","location":"Provide Location"}  #using this, we can change label name in the form
        #exclude = {"gender"}       #using this, we can hide the fields in the form


class RecruiterRegistrationForm(forms.ModelForm):
    class Meta:
        model = RecruiterRegistration
        fields = "__all__"                 # it will display all the fields the forms except default fields like id and registrationtime
        widgets = {"password":forms.PasswordInput(),"dateofbirth":DateInput()}  # additional features of the fields
        labels = {"gender":"Select Gender","location":"Provide Location"}  #using this, we can change label name in the form
        #exclude = {"gender"}       #using this, we can hide the fields in the form


class EnrollForm(forms.ModelForm):
    class Meta:
        model = Enroll
        fields = "__all__"