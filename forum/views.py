from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Answer
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def forum(request):
# Send Latest 50 messages(max) to forum page, store 50 in session
    count = Question.objects.count()
    #request.session['questions'] =[]
    if count > 10 and count < 50: 
        q = Question.objects.order_by('date')[0:count]    
    elif count <=10:
        q = Question.objects.all()
    else:
        q = Question.objects.order_by('date')[count-50:count]
    q_revised=[]
    for a in q:
        q_revised.insert(0,a)

    return render(request,'forums.html',context={'questions':q_revised})

@login_required
def answerdetails(request, id):
    if request.method == 'POST':
        q = Question.objects.get(id=int(id))
        answer = request.POST["answer"]
        reply_by = User.objects.get(username=request.user.username)
        add_answer = Answer(question=q,answer=answer,answered_by=reply_by)
        add_answer.save()
        return redirect('answerdetails',q.id)
    try:
        q = Question.objects.get(id=int(id))
        user = request.user.username
    except:
        return HttpResponse('Sorry something went wrong')
    
    if str(q.asked_by) == str(user):
        can_change = True
    else:
        can_change = False
    context ={
        'question':q,
        'answers':q.answer_set.all(),
        'can_change':can_change
    }
    print(context['answers'])
    return render(request,'answer_detail.html',context=context)

def resolved(request):
    question = request.GET.get('question', None)
    try:
        q = Question.objects.get(question=str(question))
        q.status = 'r'
        q.save()
        data = {
            'message':'Resolved Message Saved!'
        }
        return JsonResponse(data)
    except:
        data={
            'message': 'Something Went Wrong'
        }
        return JsonResponse(data)
    
