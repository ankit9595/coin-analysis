from django.shortcuts import render
from core.form import CoinSearchForm
from .models import Coin

# def find_coin(request):
#     form = CoinSearchForm(request.GET or None)
#     coins = None
#     if form.is_valid():
#         filters = {f"{field}__icontains": value for field, value in form.cleaned_data.items() if value}
#         coins = Coin.objects.filter(**filters)
#     return render(request, 'find.html', {'form': form, 'coins': coins})

# def all_data(request):
#     coins = Coin.objects.all()
#     return render(request, 'alldata.html')
