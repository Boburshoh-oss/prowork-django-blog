from django.core.paginator import Paginator
from django.shortcuts import render 

class ObjectListView:
    model=None
    template=None
    queryset=None

    def get(self,slug):
        pages=Paginator(self.queryset,3)
        posts=pages.page(self.request.GET.get('page',1))
        return render(self.request,self.template,context={self.model.__name__.lower()+"s":posts})