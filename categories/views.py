from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect
from categories.models import techCategories
from categories.forms import CategoryForm

# Create your views here.

def create_category(request):
    #form = CategoryForm()
    if request.method == "POST":
        form  = CategoryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # category = techCategories.objects.create(**form.cleaned_data)
            return redirect('/categories/all')
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', context={'form': form})


def list_all_categories(request):
    categories = techCategories.get_all()

    return render(request, 'category_index.html', context={'categories': categories})

def show(request, id):
    category = get_object_or_404(techCategories, id=id)

    return render(request, 'category_show.html', 
    context={'category': category})

def delete_category(request,category_id):
    category = get_object_or_404(techCategories,id=category_id)
    category.delete()
    return redirect('../all')

# def edit_category(request, category_id):
#     category = get_object_or_404(techCategories,id=category_id)
#     form = CategoryForm(instance)


def edit_category(request, category_id):
    category = get_object_or_404(techCategories, pk=category_id)

    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect("/categories/all")
    else:
        form = CategoryForm(instance=category)  # pre-fill form with existing data

    return render(request, "category_edit.html", {"form": form, "category": category})