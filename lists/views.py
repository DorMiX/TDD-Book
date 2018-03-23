from django.shortcuts import render, redirect
from lists.models import Item, List
from django.core.exceptions import ValidationError
# Create your views here.


def home_page(request):
    """View of Homepage."""
    return render(request, 'home.html')


def view_list(request, list_id):
    """View of List."""
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'], list=list_)
        return redirect(f'/lists/{list_.id}/')
    return render(request, 'list.html', {'list': list_})


def new_list(request):
    """View of new list."""
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {'error': error})
    return redirect(f'/lists/{list_.id}/')
