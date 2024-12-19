from django.contrib import admin
from app2.models import Message

# Define the admin class to define 
# the display of the model
# (in this case defining which of the columns to display in the admin interface).
class MessageAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']

# Register your models.
admin.site.register(Message, MessageAdmin)