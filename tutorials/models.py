from django.db import models
#from django.urls import reverse
#from django.core.urlresolvers import reverse
from django.urls import reverse

# Create your models here.
class Topics(models.Model):
    unique_no = models.IntegerField()
    name = models.CharField(max_length=500)
    top_rated = models.CharField(max_length=250)
    ques = models.IntegerField()

    def get_absolute_url(self):
        return reverse('details', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.unique_no)+'-'+self.name


class Mocktest(models.Model):
    duration = models.IntegerField()
    domain = models.ForeignKey(Topics, on_delete=models.CASCADE)
    is_fav = models.BooleanField(default=False)

    def __str__(self):
        return self.domain.name+'-'+str(self.duration)

