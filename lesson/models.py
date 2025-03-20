from django.db import models
from django.contrib.auth.models import User



class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='coach_profiles/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class LessonType(models.Model):
    """Categories for lessons (e.g., Python, Web Development)"""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    """Main lessons created by Admin"""
    lesson_type = models.ForeignKey(LessonType, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.PositiveIntegerField(default=1)  # Order of lessons
    is_published = models.BooleanField(default=False)  # Only published lessons are visible

    def __str__(self):
        return self.title

class SubLesson(models.Model):
    """Sub-lessons (topics) created by Coaches"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="sublessons")
    coach = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'coach'})
    title = models.CharField(max_length=255)
    content = models.TextField()
    video = models.FileField(upload_to='sublesson_videos/', blank=True, null=True)
    order = models.PositiveIntegerField(default=1)  # Order within lesson

    def __str__(self):
        return f"{self.lesson.title} - {self.title}"

class UserProgress(models.Model):
    """Tracks user progress in lessons"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'user'})
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    progress_percentage = models.FloatField(default=0.0)  # Track completion %
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title} - {self.progress_percentage}%"

class SubLessonProgress(models.Model):
    """Tracks user progress for each sub-lesson"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'user'})
    sublesson = models.ForeignKey(SubLesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.sublesson.title} - {'Completed' if self.completed else 'In Progress'}"

class Certificate(models.Model):
    """Issued upon lesson completion"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'user'})
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_file = models.FileField(upload_to='certificates/')

    def __str__(self):
        return f"Certificate for {self.user.username} - {self.lesson.title}"
