from django.contrib import admin

# Register your models here.
from  .models import noticeboard,tender,acadcalendar,scedule,result,careerDB,upcomingeventss

admin.site.register(noticeboard)
admin.site.register(tender)
admin.site.register(acadcalendar)
admin.site.register(scedule)
admin.site.register(result)

admin.site.register(careerDB)
admin.site.register(upcomingeventss)