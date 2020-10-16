from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import AddItemForm
from .models import AddItem


@login_required(login_url='login:index')   #redirect to login if user has not been authenticated
def home(request): 
    if request.method == 'POST':
        request.POST.keys()
        form = AddItemForm(request.POST, label_suffix =' ')
        # if form.is_valid():
        #     print(request.POST.keys())
        if form.is_valid() and request.POST.get('action')=='edit':
            data = AddItem.objects.get(id=request.POST.get('item_id'))
            data.itemName = request.POST.get('itemName')
            data.itemPrice = request.POST.get('itemPrice')
            data.itemType = request.POST.get('itemType')
            data.dateDisplayed = request.POST.get('dateDisplayed')
            data.save()
            return redirect('overview:home')         
        elif form.is_valid() and request.POST.get('action')=='new':
            addItem = form.save(commit=False)
            addItem.itemType = form.cleaned_data['itemType']
            addItem.user = request.user
            addItem.save()    #save form after the user and itemType have been determined
            itemName = form.cleaned_data['itemName']
            itemPrice = form.cleaned_data['itemPrice']
            return redirect('overview:home')
        else:
            context = {'form': form}  
    else:
        # only show objects for authenticated user
        essential_items = AddItem.objects.filter(user=request.user, itemType='essential', dateDisplayed__range=["2020-10-12", "2020-10-18"])
        leisure_items = AddItem.objects.filter(user=request.user, itemType='leisure', dateDisplayed__range=["2020-10-12", "2020-10-18"])
        optional_items = AddItem.objects.filter(user=request.user, itemType='optional', dateDisplayed__range=["2020-10-12", "2020-10-18"])
        unexpected_items = AddItem.objects.filter(user=request.user, itemType='unexpected', dateDisplayed__range=["2020-10-12", "2020-10-18"])

        # sums  
        essSum = AddItem.objects.filter(dateDisplayed__range=["2020-10-12", "2020-10-18"])

        # Forms
        essForms = {}
        leiForms = []
        optForms = []
        unxForms = []

        # Make all the individual forms for the items
            # Make a list of form objects to be used with the correct id later.
            # Maybe include the id of the object or just make it a prefix
            # Remember, a prefix can make it unique
        for i in essential_items:
            essForms[i.id] = AddItemForm()
        for i in leisure_items:
            leiForms = AddItemForm(prefix=i.id)
        print(essForms)
        context = {
            'essForms': essForms,
            'essSum': essSum,
            'essential_items': essential_items,
            'leisure_items': leisure_items,
            'optional_items': optional_items,
            'unexpected_items': unexpected_items,
            }

    return render(request, 'home.html', context)
