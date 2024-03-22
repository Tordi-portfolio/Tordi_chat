from django.contrib import admin
from .models import Room, Message
from .models import EmailUs
from .models import CustomUser
from .forms import CustomUserCreationForm

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(EmailUs)
admin.site.register(CustomUser)
admin.site.register(CustomUserCreationForm)