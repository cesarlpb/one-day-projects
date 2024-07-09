from django.shortcuts import render

def index(request):
  print("Han solicitado invoices/")
  clientes = [1, 2, 3]
  facturas = ['a', 'b', 'c']

  context = {
    "secret": "Supersafe123/",
    "clientes": clientes,
    "facturas": facturas,
  }

  return render(request, "a_invoices/index.html", context=context)
