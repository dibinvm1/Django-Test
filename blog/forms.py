from django import forms

class CommentForm(forms.Form):
    '''Comments Form feilds declaration '''
    author = forms.CharField( 
        max_length=60, widget=forms.TextInput(attrs={ 'class':'form-control','placeholder' : 'Name' }))
    body = forms.CharField(
        widget=forms.Textarea( attrs={ 'class' : 'form-control', 'rows' : 3 , 'placeholder' : 'Leave a comment!'}))