from django.shortcuts import render

def index(request):
  print("Han solicitado invoices/")
  return render(request, "a_invoices/index.html")
