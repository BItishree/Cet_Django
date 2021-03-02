from django.db import models

# Create your models here.
class noticeboard(models.Model):
    date_of_notice = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    desc =models.TextField()
    link = models.URLField(max_length = 200)


class upcomingeventss(models.Model):
    start_date = models.DateTimeField()
    end_date=models.DateTimeField()
    event_name = models.TextField()
    venue=models.TextField()
    contact=models.TextField()
    doc=models.URLField()


class tender(models.Model):

    opening_date = models.DateTimeField()
    close_date=models.DateTimeField()
    tender_link=models.URLField()
    tender_name=models.TextField()
    contact=models.TextField()
    dept=models.TextField()

class acadcalendar(models.Model):
    name = models.TextField()
    link = models.URLField()


class scedule(models.Model):
    section = models.TextField()
    desc = models.TextField()
    date = models.DateTimeField()
    link = models.URLField()


class result(models.Model):
    section = models.TextField()
    dept = models.TextField()
    sem = models.TextField()
    date=models.DateTimeField()
    title=models.TextField()
    link = models.URLField()
    type=models.TextField()

class careerDB(models.Model):
    dept= models.TextField()
    post = models.TextField()
    vacancy= models.IntegerField()
    last_date=models.DateTimeField()
    specialization=models.TextField()
    qualification=models.TextField()
    appl_link = models.URLField()
    full_notification_link=models.URLField()
