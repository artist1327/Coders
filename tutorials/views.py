from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Topics, Mocktest
from django.shortcuts import get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'tutorials/tutorials_home.html'
    context_object_name = 'topics'
    def get_queryset(self):
        return Topics.objects.all()


def details(request, tutorials_id):
    try:
        topic = Topics.objects.get(id=tutorials_id)
    except Topics.DoesNotExist:
        raise Http404("Sorry you are lost! Trackback!!!!")
    return render(request, 'tutorials/details.html', {'topic': topic})



def mock(request, section_id):
    return HttpResponse('<h3>Start Mock Test of section :' + str(section_id) + ' ' + Topics.objects.get(
        id=section_id).name + '</h3><br>')

def favourite(request, tutorials_id):
    topic = get_object_or_404(Topics, pk=tutorials_id)
    try:
        selected_mock = topic.mocktest_set.get(pk=request.POST['mocktest'])
    except (KeyError, Mocktest.DoesNotExist):
        return render(request, 'tutorials/details.html',
                      {'topic': topic, 'error_message': "You have not selected any mock",})
    else:
        selected_mock.is_fav = True
        selected_mock.save()
        return render(request, 'tutorials/details.html', {'topic': topic})


class TopicCreate(CreateView):
    model = Topics
    fields = ['unique_no', 'name', 'top_rated', 'ques']

class UserFormView(View):
    model = UserForm
    template_name = 'tutorials/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active():
                    login(request, user)
                    return redirect('index')
        return render(request, self.template_name, {'form':form})