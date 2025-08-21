from django.db import models
from django.shortcuts import reverse
# Create your models here.
class techCategories(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def show_url(self):
        return reverse('departments.show', args=[self.id])

    # get all objects from model ??
    @classmethod
    def get_all(cls):
        # order data, exclude some fields , do any operation. 
        return cls.objects.all()





