from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.core.urlresolvers import reverse
from django.views import generic
from groups.models import Group, GroupMember
from django.shortcuts import get_object_or_404
from django.contrib import messages
# Create your views here.


class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = Group


class SingleGroup(generic.DetailView):
    model = Group


class ListGroups(generic.ListView):
    model = Group


class JoinGroup(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        except IntegrityError:
            messages.warning(self.request,('Warning already a member!'))
        else:
            messages.success(self.request,('You are now a member!'))

        return super().get(request,*args,**kwargs)


class LeaveGroup(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    
    def get(self,request,*args,**kwargs):

        try:
            membership = models.GroupMember.objects.filter(
                    user=self.request.user,
                    group_slug=self.kwargs.get('slug')
                    ).get()
        except models.GroupMember.DoesNotExist:
            messages.warning(self.request,('You are not in this group!'))
        else:
            membership.delete()
            messages.success(self.request,('You left the group!'))
            return super().get(request,*args,**kwargs)
