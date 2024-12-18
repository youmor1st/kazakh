from .models import Course, Lesson, Task
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = Lesson.objects.filter(course=course)
    return render(request, 'course_detail.html', {'course': course, 'lessons': lessons})


def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    course = lesson.course
    lessons = course.lessons.order_by('order')

    previous_lesson = lessons.filter(order__lt=lesson.order).last()
    next_lesson = lessons.filter(order__gt=lesson.order).first()

    return render(request, 'lesson.html', {
        'lesson': lesson,
        'previous_lesson': previous_lesson,
        'next_lesson': next_lesson,
    })


def task(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    questions = Task.objects.filter(lesson=lesson)

    if request.method == 'POST':
        score = 0
        total = questions.count()

        for question in questions:
            user_answer = request.POST.get(f"q{question.id}")
            if user_answer and int(user_answer) == question.correct_answer:
                score += 1

        return render(request, 'task_result.html', {'lesson': lesson, 'score': score, 'total': total})

    return render(request, 'task.html', {'lesson': lesson, 'questions': questions})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Проверка совпадения паролей
        if password != confirm_password:
            messages.error(request, "Пароли не совпадают")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Пользователь с таким логином уже существует")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Регистрация прошла успешно! Теперь вы можете войти.")
        return redirect('login')

    return render(request, 'register.html')
