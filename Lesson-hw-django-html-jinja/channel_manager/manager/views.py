from django.shortcuts import render
from .models import Transaction, PaidContent

# Create your views here.

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, "transaction_list.html", {"transactions": transactions})

def article(request):
    paidcontents = PaidContent.objects.get(title='Время всегда хорошее')
    return render(request, "index.html", {"paidcontents": paidcontents})

def article2(request):
    paidcontents = PaidContent.objects.get(title='Правдивая история Деда Мороза')
    return render(request, "index.html", {"paidcontents": paidcontents})

def article3(request):
    paidcontents = PaidContent.objects.get(title='Порри Гаттер. Всё!')
    return render(request, "index.html", {"paidcontents": paidcontents})