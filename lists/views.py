from django.shortcuts import render


def home_page(request):
    print("yay" + request.POST.get("item_text", ""))
    return render(request, "home.html", {
        "new_item_text": request.POST.get("item_text", ""),
    })
