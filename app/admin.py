from django.contrib import admin
from .models import *

class FirstnameAdmin(admin.ModelAdmin):
    first_name = ['id', 'FirstName', 'created_at']
    last_name = ['id', 'LastName', 'created_at']
    email = ['id', 'MyEmail', 'created_at' ]
    password = ['id', 'PassWord', 'created_at' ]

# class LastnameAdmin(admin.ModelAdmin):
    

# class EmailAdmin(admin.ModelAdmin):
    

# class PasswordAdmin(admin.ModelAdmin):
    


# admin.site.register(Mypassword, PasswordAdmin)
# admin.site.register(MyEmail, EmailAdmin)
admin.site.register(Myform, FirstnameAdmin)
# admin.site.register(Lastname, LastnameAdmin)
# Register your models here.
