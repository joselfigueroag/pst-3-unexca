from django.contrib import admin

from .models import Section, Grade, Teacher, Subject

# Register your models here.

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
  pass


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
  pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
  pass


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
  pass
