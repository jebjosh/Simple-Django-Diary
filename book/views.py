from django.shortcuts import render, redirect

from .models import Entry
# Create your views here.

from .forms import EntryForm


def home(request):

    enties = Entry.objects.order_by('-date_added')

    return render(request, "book/index.html", {"entries": enties})


def addEntry(request):

    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        entryform = EntryForm()

    return render(request, "book/add.html", {"entryform": entryform})
