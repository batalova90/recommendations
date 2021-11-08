from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render



def index(request):
    # code here...
    return render(request, 'reviews/index.html', {'here_context': 'context'})
