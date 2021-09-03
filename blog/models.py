from django.db import models
from django.db.models.fields import DateField
from django.shortcuts import reverse
# class Category(models.Model):
#     name=models.CharField(max_length=255)

#     def __str__(self):
#         return self.name
    
class Post(models.Model):
    title=models.CharField(max_length=255,db_index=True)
    slug=models.SlugField(max_length=255,unique=True)
    body=models.TextField(blank=True)
    data_pub=models.DateField(auto_now_add=True)
    tags=models.ManyToManyField('Tag',blank=True,related_name='posts')

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug":self.slug})

        
    def __str__(self):
        return self.title

class Tag(models.Model):
    name=models.CharField(max_length=150)
    slug=models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse("tag_detail_url", kwargs={"slug": self.slug})
    

    def __str__(self):
        return self.name
    

    
    
