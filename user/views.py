from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request,"Account created for {}".format(username))
            return redirect('/')
    else:
        form =UserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'user/register.html', context)
