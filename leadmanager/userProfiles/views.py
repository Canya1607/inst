from django.shortcuts import render
from django.http import HttpResponse
from .models import  userProfile
from rest_framework import viewsets
from .serializers import userProfileSerializer
from .forms import UserUpdateFrom, ProfileUpdateForm

class userProfileView(viewsets.ModelViewSet):
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer

def user_detail_view(request, username, *args, **kwargs):
    return render(request,{"username": username})



#@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateFrom(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   nstance=request.user.profile )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your acc has been updated!')
            return redirect('userProfile')
    else:
        u_form = UserUpdateFrom(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile )

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, context)