from django.shortcuts import redirect, render

from lists.models import Item, List


def home_page(request):
    return render(request, "home.html")

def new_list(request):
    new_list = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=new_list)
    return redirect("/lists/the-only-list-in-the-world/")

def view_list(request):
    return render(request, "list.html", {"items": Item.objects.all()})
