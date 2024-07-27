from django.db import models
from courses.models import Courses
from classes.models import Class

# Create your models here.
class ClassroomPeriod(models.Model):
   start_time=models.TimeField()
   end_time=models.TimeField()
   course=models.ForeignKey(Courses, default=None, on_delete=models.CASCADE, related_name='course_name')
   classroom=models.ForeignKey(Class, default=None, on_delete=models.CASCADE, related_name='class_name')
   day_of_the_week=models.DateField()
   def __str__(self):
        return f"{self.start_time} {self.end_time}"
    
