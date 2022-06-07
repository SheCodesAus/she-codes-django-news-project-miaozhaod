# reverse_lazy: change django to a url
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm

# Create your views here.
# login and logout's views are predefined in django
class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    # reverse_lazy lookup the url path from the saved name
    success_url = reverse_lazy("login")
    template_name = "users/createAccount.html"


class ViewAccountView(generic.DetailView):
    model = CustomUser
    template_name = "users/viewAccount.html"
