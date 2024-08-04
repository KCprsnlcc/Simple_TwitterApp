# twitter_app/views.py
from django.shortcuts import render, redirect
from .forms import StatusForm
from .models import Status
from better_profanity import profanity
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

def home(request):
    statuses = Status.objects.all().order_by('-created_at')
    form = StatusForm()
    return render(request, 'twitter_app/home.html', {'statuses': statuses, 'form': form})

def post_status(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            if profanity.contains_profanity(content):
                return render(request, 'twitter_app/home.html', {
                    'form': form,
                    'error': 'Your post contains inappropriate content.'
                })
            form.save()
            return redirect('home')
    return redirect('home')

@csrf_exempt
def check_profanity(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        content = data.get('content', '')
        profanity.load_censor_words()
        if profanity.contains_profanity(content):
            return JsonResponse({"error": "Your post contains inappropriate content."}, status=400)
        return JsonResponse({"message": "Content is appropriate."})


profanity.load_censor_words()
