from django.db import models

# Create your models here.
class CourseModel(models.Model):
    name = models.CharField(max_length=128)
    images=models.ImageField(upload_to='images/',default="")

    
    def __str__(self):
        return self.name

class VideoModel(models.Model):
    name = models.CharField(max_length=128,default='')
    course = models.ForeignKey(CourseModel,on_delete=models.CASCADE)
    video = models.FileField(upload_to = 'videos/')
    pdf = models.FileField(upload_to = 'pdfs/',default=None,null=True,blank=True)
    images=models.ImageField(upload_to='images/',default="images/video_hjR01iq.png")


    def __str__(self):
        return self.course.name


