from django.shortcuts import render

# Create your views here.

def greeting(request):
    return render (request, 'students.html')

def result(request):
    stu = [
        {'name' : 'Swofvan', 'grade': 86, 'res': 'Passed'},
        {'name' : 'Lakshmi', 'grade': 99, 'res': 'Passed'},
        {'name' : 'Akhila', 'grade': 12, 'res': 'Failed'},
        {'name' : 'Nikhil', 'grade': 56, 'res': 'Passed'},
    ]
    
    show = {'stu': stu}
    return render(request, 'students.html', show)


# Each student has a name, grade, and whether they passed.
