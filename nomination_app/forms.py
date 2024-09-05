from django import forms

class NomineeForm(forms.Form):
    subscriber_name = forms.CharField(label="Subscriber Name", max_length=100)
    marital_status = forms.CharField(label="Marital Status", max_length=50)
    account_number = forms.CharField(label="Account Number", max_length=100)
    place = forms.CharField(label="Place", max_length=100)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    # Add nominee fields for dynamic form
    nominee_name = forms.CharField(label="Nominee Name", max_length=100)
    nominee_address = forms.CharField(label="Permanent Address", widget=forms.Textarea)
    nominee_aadhar = forms.CharField(label="Aadhar Number", max_length=12)
    nominee_relationship = forms.CharField(label="Relationship with Subscriber", max_length=50)
