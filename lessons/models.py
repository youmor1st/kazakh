from django.db import models

class Course(models.Model):
    LEVELS = [
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    level = models.CharField(max_length=2, choices=LEVELS)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=100)
    content = models.TextField()
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Task(models.Model):
    TASK_TYPES = [
        ('choice', 'Выбор ответа'),
    ]
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, related_name='tasks')
    question = models.TextField()
    task_type = models.CharField(max_length=10, choices=TASK_TYPES, default='choice')
    option1 = models.TextField(null=True, blank=True)
    option2 = models.TextField(null=True, blank=True)
    option3 = models.TextField(null=True, blank=True)
    option4 = models.TextField(null=True, blank=True)
    option5 = models.TextField(null=True, blank=True)
    correct_answer = models.IntegerField()

    def __str__(self):
        return f"Куиз: {self.question}"
