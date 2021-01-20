from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request,"Account created for {}".format(username))
            return redirect('/')

    else:
        form = UserRegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'user/register.html', context)
