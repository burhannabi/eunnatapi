from django.db import models

# Create your models here.

class Deptartment(models.Model):
    department_name = models.CharField(max_length=200, blank=False, null=False)
    service_title = models.CharField(max_length=200, blank=False, null=False)
    psga_time = models.IntegerField(blank=False, null=False)
    user_feedback = models.IntegerField(blank=False, null=False)
    up_down = models.IntegerField(blank=False, null=False)
    availability = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.department_name


class Images(models.Model):
    image = models.ImageField()
    department = models.OneToOneField(Deptartment, on_delete=models.PROTECT)

    def __str__(self):
        return self.image