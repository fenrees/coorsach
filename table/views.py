from django.shortcuts import render
import sys
import string
import os
import json
from django.utils import timezone
from .models import Post

def open_file(name):
    file = r"\table\{0}.json".format(name)
    path = os.getcwd() + file
    with open(path, "r", encoding='utf-8') as fh:
        data = json.load(fh)
    return data


def write_in_file(name, text):
    file = r"\table\{0}.json".format(name)
    path = os.getcwd() + file
    with open(path, "w", encoding='utf-8') as fh:
        fh.write(text)
    pass


def title(request):
    syst = open_file("system")
    return render(request, "table/Title.html", {'syst': syst})


def admin(request):
    syst = open_file("system")
    logininfo = open_file("Admin")
    for i in logininfo:
        if request.POST.get('login') == i["login"] and request.POST.get('password') == i["password"]:
            return render(request, "table/Admin.html", {'syst': syst})

    return render(request, "table/Title.html", {'syst': syst})  


def get_system(request):
    syst = open_file ("system")
    return render(request, "table/Title.html", {'syst': syst})


def add_book(request):
    syst = open_file("system")
    for i in syst:
        if i["id"] == request.POST.get("1"):
            book = {
            "name" : request.POST.get("название"),
            "autor" : request.POST.get("автор"),
            "date0" : request.POST.get("дата поступления в фонд"),
            "date1" : request.POST.get("дата выхода из фонда"),
            "reason" : request.POST.get("причина выхода")
                        }
            i["book"].append(book)
            write_in_file("system", str(syst).replace("\'", "\""))
            return render(request, "table/Admin.html", {'syst': syst})

    return render(request, "table/Title.html", {'syst': syst}) 
