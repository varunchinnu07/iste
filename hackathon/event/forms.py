from django import forms
from .models import Team, Participant, Payment
()
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_name', 'college_name', 'district', 'domain', 'idea_description','idea_ppt']

        widgets = {
            'idea_description': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            }
        labels = {
            'idea_ppt': 'Upload your PPT',
        }

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        
        # Check if domain is "Design" and remove 'idea_ppt' if true
        if 'domain' in self.data and self.data.get('domain') == 'design':
            self.fields.pop('idea_ppt')

    def clean_idea_ppt(self):
        ppt_file = self.cleaned_data.get('idea_ppt')
        if ppt_file:
            # Check the file extension
            file_extension = ppt_file.name.split('.')[-1].lower()
            if file_extension not in ['ppt', 'pptx']:
                raise forms.ValidationError("Only PPT and PPTX files are allowed.")
            
            # Optional: Check the file size (e.g., 10MB max)
            if ppt_file.size > 10 * 1024 * 1024:  # 10MB limit
                raise forms.ValidationError("File size should not exceed 10MB.")
        
        return ppt_file    

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'phone_number', 'gender']
        
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['transaction_id','payment_person_name','receipt_image']