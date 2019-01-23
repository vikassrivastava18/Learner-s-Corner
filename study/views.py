from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from .models import Subject, Course, Notes
from forum.models import Question, Topic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def study(request):
    study = []
    subjects = Subject.objects.all()
    for subject in subjects:
        course = Course.objects.filter(subject__name=subject)
        study.append({'subject':subject,'course':course})
    
    return render(request, 'study.html',context={'study':study})

def courses(request, course):
    course = Course.objects.get(name=course)
    user = User.objects.get(username=request.user.username)
    link = course.link
    notes = Notes.objects.filter(user=user,course=course)
    return render(request,'course.html',context={'link':link,'notes':notes,'course':course})

@login_required
def save_notes(request):
    notes = request.GET.get('notes', None)
    course_name = request.GET.get('course', None)
    course = Course.objects.get(name=course_name)
    user = User.objects.get(username=request.user.username)
    saved_notes = Notes.objects.filter(user=user,course=course)
    
    if saved_notes:
        saved_notes = Notes.objects.get(user=user,course=course)
        saved_notes.notes = saved_notes.notes + "<p>" + notes + "</p>"
        saved_notes.save()
    else:
        saved_notes = Notes(course=course,user=user,notes=notes)
        saved_notes.save()
    data = {
        'notes': saved_notes.notes
    }
    return JsonResponse(data)
@login_required
def question(request):
    question = request.GET.get('question', None)
    course_name = request.GET.get('course', None)
    course = Course.objects.get(name=course_name)
    topic_name = course.subject
    print(topic_name)
    user = User.objects.get(username=request.user.username)
    topic = Topic.objects.get(topic=topic_name)
    q = Question(question=question,topic=topic,asked_by=user)
    q.save()
    data = {
        'notes': 'Question Sent To Forum'
    }
    return JsonResponse(data)

