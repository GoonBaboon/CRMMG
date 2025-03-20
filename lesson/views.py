from django.shortcuts import render, get_object_or_404, redirect
from .models import Lesson
from .forms import LessonForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# List all lessons
@login_required
def lessons_view(request):
    lessons = Lesson.objects.all()
    return render(request, 'lesson/lesson_list.html', {'lessons': lessons})

# View details of a specific lesson
def lesson_detail_view(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'lesson/lesson_detail.html', {'lesson': lesson})

