from django.db import models


class Myform(models.Model):
    id = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=200, null=False, blank=False )
    LastName = models.CharField(max_length=200, null=False, blank=False, default='SOME STRING')
    MyEmail = models.EmailField(max_length=55, null=False, blank=False, default='our string')
    PassWord = models.CharField(max_length=55, null=False, blank=False, default='my string') 
    created_at = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ["-created_at"]

def _str_(self):
        return self.FirstName


# class Lastname(models.Model):
#     id = models.AutoField(primary_key=True)
    
#     created_at = models.DateTimeField(auto_now=True)

#     class meta:
#         ordering = ["-created_at"]

# class MyEmail(models.Model):
#     id = models.AutoField(primary_key=True)
   
#     created_at = models.DateTimeField(auto_now=True)

#     class meta:
#         ordering = ["-created_at"]

# class Mypassword(models.Model):
#     id = models.AutoField(primary_key=True)
    
#     created_at = models.DateTimeField(auto_now=True)

#     class meta:
#         ordering = ["-created_at"]

# Create your models here.
