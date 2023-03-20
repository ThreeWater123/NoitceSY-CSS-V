from django.views import generic
from django.urls import reverse_lazy
# from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import group

# Create your views here.
class group_list(generic.ListView):

    model=group

    template_name="group.html"


######################################


class group_detail(generic.DetailView):

    slug_field='slug'

    slug_url_kwarg='slug'

    model=group

    template_name="group_detail.html"


################################################


class group_notice_update(generic.UpdateView,LoginRequiredMixin,PermissionRequiredMixin):
    

    # form=GroupForm

    model=group

    template_name="group_update.html"

    fields=('notice',)

    success_url=reverse_lazy("catalog:group")

    login_url='/account/login'

    permission_required = 'catalog.notice'


###################################


class get_notice(generic.DetailView):

    

    model=group

    template_name="get.html"


###################################


class group_create(generic.CreateView,LoginRequiredMixin,PermissionRequiredMixin):

    # form=GroupForm

    model=group

    template_name="group_create.html"

    fields=('notice','name',)
    
    success_url=reverse_lazy("catalog:group")

    login_url='/account/login'#没有权限/未登录用户自动跳转的网站

    permission_required = 'catalog.notice'#权限设置

##############################################
   

class group_delete(generic.DeleteView,LoginRequiredMixin,PermissionRequiredMixin):

    model=group    

    template_name='group_delete.html'

    success_url=reverse_lazy("catalog:group")

    permission_required = 'catalog.notice'

    login_url='/account/login'


    ############################################


class user_create(generic.CreateView):

    # form=UserForm

    model=User

    fields=('username','password','email')

    template_name='user_create.html'

    success_url=reverse_lazy("login")