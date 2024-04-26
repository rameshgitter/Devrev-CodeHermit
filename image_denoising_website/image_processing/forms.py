from django import forms

class ImageForm(forms.Form):
    image = forms.ImageField()
    filter_type = forms.ChoiceField(choices=[('average', 'Average Filter'), ('median', 'Median Filter')])
    kernel_size = forms.IntegerField(min_value=1)
