from django import forms

from .models import File

class FileForm(forms.ModelForm):
    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요'    
        }, 
        max_length=128, label="제목")
    pdf = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = File
        fields = {'title', 'pdf'}