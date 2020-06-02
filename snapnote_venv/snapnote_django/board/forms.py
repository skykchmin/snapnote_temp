from django import forms

from .models import File

from multiupload.fields import MultiFileField
from .models import Attachment

# class FileForm(forms.ModelForm):
#     title = forms.CharField(
#         error_messages={
#             'required': '제목을 입력해주세요'    
#         }, 
#         max_length=128, label="제목")
#     pdf = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

#     class Meta:
#         model = File
#         fields = {'title', 'pdf'}

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

# class FileForm(forms.ModelForm):
#     title = forms.CharField(
#         error_messages={
#             'required': '제목을 입력해주세요'    
#         }, 
#         max_length=128, label="제목")
#     pdf = models.FileField(upload_to='files/pdfs/', widget=forms.ClearableFileInput(attrs={'multiple': True}))

#     class Meta:
#         model = File
#         fields = {'title', 'pdf'}        

# class FileForm(forms.Form):
#     title = forms.CharField(
#         error_messages={
#             'required': '제목을 입력해주세요'    
#         }, 
#         max_length=128, label="제목")
#     pdf = MultiFileField(min_num=1, max_num = 3, max_file_size=1024*1024*5)

#     class Meta:
#         model = File
#         fields = {'title', 'pdf'}

# class FileFieldForm(forms.Form):
#     file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

# class UploadForm(forms.ModelForm):
#     class Meta:
#         model = Attachment
#         fields = ['files',]
     
#     files = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)

#     def save(self, commit=True):
#         instance = super(UploadForm, self).save(commit)
#         for each in self.cleaned_data['files']:
#             Attachment.objects.create(file=each, message=instance)

#         return instance

# class UploadForm(forms.ModelForm):
#     class Meta:
#         model = File
#         fields = ['title', 'files',]  
    
#     title = forms.CharField(max_length=128, label="제목")
#     files = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)

#     def save(self, commit=True):
#         instance = super(UploadForm, self).save(commit)
#         for each in self.cleaned_data['files', 'title']:
#             File.objects.create(file=each, message=instance, title = each)
            

#         return instance

class UploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['title', 'files',]  

    files = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)

    def save(self, commit=True):
        instance = super(UploadForm, self).save(commit)
        for each in self.cleaned_data['files']:
            File.objects.create(file=each, message=instance)

        return instance