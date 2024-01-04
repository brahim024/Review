from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from .models import Ticket
from .models import Review
from .models import UserFollows

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def ticket_view(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'ticket.html', {'ticket': ticket})

def review_view(request, review_id):
    review = Review.objects.get(id=review_id)
    return render(request, 'review.html', {'review': review})

def user_follows_view(request):
    userfollows = UserFollows.objects.filter(user=request.user)
    return render(request, 'userfollows.html', {'userfollows': userfollows})




