from django import forms
from django.core.exceptions import ValidationError


class registerScooterForm(forms.Form):
    model = forms.CharField(max_length=100)
    image = forms.ImageField()
    color = forms.CharField()
    rate_per_hour = forms.IntegerField()
    start_time = forms.TimeField()
    end_time = forms.TimeField()

    def clean(self):
        cleaned_data = super().clean()
        # start_time = cleaned_data.get("start_time")
        # end_time = cleaned_data.get("end_time")

        # if end_time < start_time:
        #     raise ValidationError("End time should be after start time")
        return cleaned_data