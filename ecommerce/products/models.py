from django.db import models
# import PIL


# Create your models here.
class Product(models.Model):
  title = models.CharField(max_length=120 , null=False, blank=False)
  description = models.TextField(null = True, blank=True)
  price = models.DecimalField(decimal_places=2,max_digits=100 , default=29.99)
  sale_price = models.DecimalField(decimal_places=2,max_digits=100 , null=True, blank=True)

  slug = models.SlugField(unique=True)
  timestamp = models.DateTimeField(auto_now_add=True , auto_now=False)
  updated = models.DateTimeField(auto_now_add=False , auto_now=True)
  active = models.BooleanField(default=True)

  def __unicode__(self):
    return self.title

  class Meta:
    unique_together = ('title' , 'slug')

  def get_price(self):
    return self.price
