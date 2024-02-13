from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

    
class Book(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    checked_out = models.BooleanField(default=False)
    checked_out_date = models.DateTimeField('date checked out', null=True, blank=True)
    checked_in_date = models.DateTimeField('date checked in', null=True, blank=True)

    def __str__(self):
        return self.title
    
