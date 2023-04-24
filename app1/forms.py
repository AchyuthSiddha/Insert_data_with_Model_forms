from django import forms

from app1.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'



class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name']
        # fields=['topic_name','name']
        # labels={'topic_name':'TN','name':'N'}
        #exclude=['topic_name']
        # help_texts={'name':'only alphabets','email':'combination of alpha and numerical charcter and special character'}
        # widgets={'url':forms.PasswordInput}

        
class Access_RecordForm(forms.ModelForm):
    class Meta:
        model=Access_record
        fields='__all__'
