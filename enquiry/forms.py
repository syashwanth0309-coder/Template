from django import forms
from .models import Enquiry
class EnquiryForm(forms.ModelForm):
    website = forms.CharField(required=False, widget=forms.HiddenInput)
    class Meta:
        model = Enquiry
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder":"Your name", "autocomplete":"name"}),
            "email": forms.EmailInput(attrs={"placeholder":"you@example.com", "autocomplete":"email"}),
            "message": forms.Textarea(attrs={"placeholder":"Tell me about your idea or opportunity…", "rows":6, "maxlength":4000}),
        }
    def clean_website(self):
        if self.cleaned_data.get("website"):
            raise forms.ValidationError("Unable to submit this enquiry.")
        return ""
