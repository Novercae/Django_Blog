import email
from django.forms import ModelForm, Textarea
from .models import Comment
from django.contrib import messages
import requests


class CommentForm(ModelForm):
    def clean(self):
        raw_data = self.data
        recapcha_response = raw_data.get('g-recaptcha-response')

        recapcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': '6Lc9pFofAAAAALxlMzd061MCM7J4-th90kM4S3Px',
                'response': recapcha_response
            }
        )
      
        if not recapcha_request.json()['success']: 
            self.add_error('comment', 'Please verify that you are not a robot.')       

        cleaned_data = self.cleaned_data
        name = cleaned_data.get('name_comment')
        comment = cleaned_data.get('comment')
        email = cleaned_data.get('email_comment')

        if len(name) < 3:
            self.add_error('name_comment', 'Name must be at least 3 characters long.')
        
        if email and not email.endswith('@gmail.com')\
            and not email.endswith('@yahoo.com')\
            and not email.endswith('@hotmail.com')\
            and not email.endswith('@outlook.com')\
            and not email.endswith('@aol.com'):
            self.add_error('email_comment', 'Email must be a valid email address.')

            


 

    class Meta:
        model = Comment
        fields = ('name_comment', 'email_comment', 'comment')
        
        