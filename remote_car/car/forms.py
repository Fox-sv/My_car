from django import forms
from . import models


class DateOilForm(forms.ModelForm):
    class Meta:
        model = models.Date_oil
        fields = '__all__'


class DateInsuranceForm(forms.ModelForm):
    class Meta:
        model = models.Date_insurance
        fields = '__all__'


class DateInspectionForm(forms.ModelForm):
    class Meta:
        model = models.Date_inspection
        fields = '__all__'


class NewExpensesForm(forms.ModelForm):
    class Meta:
        model = models.Expenses
        exclude = ['responsible_user_id']


class ShareContactForm(forms.Form):
    name = forms.CharField(max_length=230, required=True, label='Your Email')
    message = forms.CharField(required=True, widget=forms.Textarea, )
