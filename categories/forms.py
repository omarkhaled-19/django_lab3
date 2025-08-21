from django import forms
from categories.models import techCategories

# class CategoryForm(forms.Form):
#     name = forms.CharField(max_length=255, required=True)
#     description = forms.CharField(widget=forms.Textarea, required=False)
#     image = forms.ImageField(widget=forms.ClearableFileInput, required=False)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = techCategories
        fields = ["name", "description", "image"]  # choose fields you want


    def clean_name(self):
        name = self.cleaned_data.get('name')
        
        if techCategories.objects.filter(name=name).exists():
            raise forms.ValidationError("Category with this name already exists")
        return name
    