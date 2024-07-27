from django.db import models

# Create your models here.
class Class(models.Model):
      class_name= models.CharField(max_length=20).primary_key
      class_id = models.PositiveSmallIntegerField()
      names_of_teachers = models.TextField()
      number_of_enrolled_students = models.PositiveSmallIntegerField()
      number_of_classrooms= models.TextField()
      meeting_days = models.CharField(max_length=20)
      academic_year = models.PositiveSmallIntegerField()
      class_capacity = models.PositiveSmallIntegerField()
      
      def __str__(self):
        return f"{self.class_name} {self.class_id}"