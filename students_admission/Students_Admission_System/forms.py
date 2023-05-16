from django import forms
from .models import Application
from crispy_forms.helper import FormHelper
from django.forms import ModelForm, Textarea, HiddenInput, DateInput
from .admission_selector import generate_admission_number


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ('user', 'Application_Status', 'message',)


        
    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        #self.helper = FormHelper()
        self.fields['application_id'].widget.attrs['readonly'] = True
        #self.fields["application_id"].widget = HiddenInput()


