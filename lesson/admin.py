from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Lesson)
admin.site.register(SubLesson)
admin.site.register(SubLessonProgress)
admin.site.register(LessonType)
admin.site.register(Certificate)