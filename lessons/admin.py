from django.contrib import admin
from .models import Course, Lesson, Task

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'level')
    search_fields = ('title', 'level')
    list_filter = ('level',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    search_fields = ('title', 'course__title')
    list_filter = ('course',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('question', 'lesson', 'task_type')
    search_fields = ('question', 'lesson__title')
    list_filter = ('task_type',)
