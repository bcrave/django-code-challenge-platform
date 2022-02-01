from django.shortcuts import render
from django.http import HttpResponse

from challenges.models import Challenge
from .forms import ChallengeForm

def challenge_welcome(request):
  return HttpResponse('Welcome to Cognizant Code Challenger')

def challenge_submit(request):
  form = ChallengeForm()

  if request.method == 'POST':
    form = ChallengeForm(request.POST)
    if form.is_valid():
      form.save()
  context = { 'form': form }
  
  return render(request, 'challenge-submit.html', context)
