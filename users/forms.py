from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'שם פרטי',
            'last_name': 'שם משפחה',
            'email': 'כתובת אימייל',
            'username': 'שם משתמש',
            'password1': 'הכנס סיסמה',
            'password2': 'אימות סיסמה',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name','last_name','email','username','location','short_intro'
        ,'bio','profile_image','social_facebook','social_instagram',
        'social_youtube','social_tiktok','social_website']
        labels = {
            'first_name': 'שם פרטי',
            'last_name': 'שם משפחה',
            'email': 'כתובת אימייל',
            'username': 'שם משתמש',
            'location': 'מיקום',
            'short_intro': 'תיאור קצר',
            'bio': 'קצת עלי',
            'profile_image': 'תמונת פרופיל',
            'social_facebook': 'פייסבוק',
            'social_instagram': 'אינסטגרם',
            'social_youtube': 'יוטיוב',
            'social_tiktok': 'טיקטוק',
            'social_website': 'אתר אישי',
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})