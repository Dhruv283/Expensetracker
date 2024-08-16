from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    if request.method=="POST":
        data=request.POST
        date=data.get("date")
        category=data.get("category")
        amount=data.get("amount")
        Expense.objects.create(date=date,category=category,amount=amount)
        expense_list=Expense.objects.all()
        
    return render(request,"index.html")
    
def view(request):
    expense_list=Expense.objects.all()
    if request.GET.get('search'):

        expense_list=expense_list.filter(category__icontains=request.GET.get('search'))
        
    context={"expense_list":expense_list}
    return render(request,"viewexpense.html",context)

def delete(request,id):
    Expense.objects.get(id=id).delete()
    return redirect('/viewexpense')

def update(request,id):
    old_ele=Expense.objects.get(id=id)
    
    
    if request.method=="POST":
        data=request.POST
        date=data.get("date")
        category=data.get("category")
        amount=data.get("amount")

        old_ele.date=date
        old_ele.category=category
        old_ele.amount=amount
        old_ele.save()

       
        return redirect('/viewexpense')
        
    return render(request,"update.html",context={"old_ele":old_ele})