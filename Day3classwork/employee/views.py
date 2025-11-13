from django.shortcuts import render

# Create your views here.

def employee(request):
    return render(request, 'employee.html')

def details(request):
    det = [
        {'name': 'Swofvan', 'job' : 'Fullstack Devoloper', 'salary' : 75000, 'type' : 'Full-Time'},
        {'name': 'Akhila', 'job' : 'Backend Devoloper', 'salary': 60000, 'type' : 'Full-Time'},
        {'name': 'Lakshmi', 'job' : 'Frontent Devoloper', 'salary' : 50000, 'type' : 'Part-Time'}
    ]

    context = {'det': det}
    return render(request, 'employee.html', context)
