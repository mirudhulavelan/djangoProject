from django.shortcuts import render, redirect
from .form import uploadResume
from docx import *


def index(request):
    if request.method == 'POST':
        file1 = request.FILES['document']
        document = Document(file1)
        lin = []
        for para in document.paragraphs:
            temp = ""
            line = para.text.split()
            c = 0
            for x in line:
                if (x == ":"):
                    c = 1
                if (c > 1):
                    temp += x + " "
                c += 1
            lin.append(temp.strip())
            print(temp)

        context = {'fname': lin[0],
                   'lname': lin[1],
                   'mail': lin[2],
                   'number': lin[3],
                   'address': lin[4],
                   'city': lin[5],
                   'pin': lin[6],
                   'state': lin[7],
                   'country': lin[8],
                   'skill': lin[9],
                   'exp': lin[10],
                   'edu': lin[11]
                   }

        form = uploadResume(context)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/homepage')
    return render(request, 'homepage.html')

