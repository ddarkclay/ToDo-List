from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
    all_items = {}
    if request.method == 'POST':  
        this_item = request.POST['add_item']
        item_add = List(item=this_item, completed=False)
        item_add.save()
        all_items = List.objects.all()
        print(all_items)
        messages.success(request, ('Items Has been Added To List !'))
        return render(request, 'home.html', {'all_items':all_items})
        # form = ListForm(request.POST or None) 
        # print(form)
        # print(all_items)
        # print(form.is_valid())
        # if form.is_valid():
        #     form.save()
        #     all_items = List.objects.all()
        #     messages.success(request, ('Items Has been Added To List !'))
        #     return render(request, 'home.html', {'all_items':all_items})
        # return render(request, 'home.html', {'all_items':all_items})
    else:
        all_items = List.objects.all()
        print(all_items)
        return render(request, 'home.html', {'all_items':all_items})

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Items Has Deleted Successfully'))
    return redirect('HomePage')

def crossoff(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('HomePage')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('HomePage')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item Edited Successfully'))
            return redirect('HomePage')

    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})