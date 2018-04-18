from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Poll, Choice
from django.contrib.auth.models import User

# Create your views here.
def polls_list(request):
    if request.method == 'POST':
        poll = Poll.objects.create(
            question = request.POST.get('question', ''),
            created_by = User.objects.get(username=request.POST.get('username', ''))
        )
        data = {"question": poll.question}
        return JsonResponse(data)
    
    MAX_OBJECTS=20
    polls = Poll.objects.all()[:20]
    data = {"results": list(polls.values("question", "created_by__username", "pub_date"))}
    return JsonResponse(data)

def polls_details(request, pk):
    poll = get_object_or_404(Poll, pk)
    data = {"results":{
        "question": poll.question,
        "created_by": poll.created_by.username,
        "pub_date": poll.pub_date
    }}
    return JsonResponse(data)
