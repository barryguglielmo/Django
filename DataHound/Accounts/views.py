from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import generic
from django.contrib.messages import constants as messages
from .forms import TheCsvForm, GraphForm
from .models import Your_CSV
# Create your views here.
def your_home(request):
    return render(request, "accounts/your_home.html")

####################################################################
class Register(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register_form.html'
    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login' )

class LoginView(generic.FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login_form.html'
    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect('your_home')

def New_CSV(request):
    if request.method == 'POST':
        form = TheCsvForm(request.POST, request.FILES)
        if form.is_valid():
            csv = Your_CSV()
            csv.user = request.user
            csv.your_csv = form.cleaned_data["your_csv"]
            csv.description = form.cleaned_data["description"]
            csv.save()
            return redirect('DataListView')
    else:
        form = TheCsvForm()
    return render(request, 'accounts/new_csv_form.html', {'form':form} )

class DataListView(LoginRequiredMixin, generic.ListView):
    template_name='accounts/your_csvs.html'
    context_object_name = 'Data_List'
    def queryset(self):
        user = self.request.user
        queryset =  Your_CSV.objects.filter(user = user).order_by('-date')
        return queryset

def simple_graph(request):
    return render(request, "accounts/simple_graph.html")
def bodata(request):
    return render(request, "accounts/bodata.csv")
