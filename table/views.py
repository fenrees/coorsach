from django.shortcuts import render, HttpResponse
import sys
import string
import os
import json
from django.utils import timezone
from .models import Post

def open_file(name):
    file = r"/table/{0}.json".format(name)
    path = os.getcwd() + file
    with open(path, "r", encoding='utf-8') as f:
        data = json.load(f)
    return data


def write_in_file(name, text):
    file = r"/table/{0}.json".format(name)
    path = os.getcwd() + file
    with open(path, "w", encoding='utf-8') as f:
        f.write(text)
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
    syst = open_file("system")
    return render(request, "table/Title.html", {'syst': syst})


def add_book(request):
    if request.POST:
        id = request.POST.get("id")
        name = request.POST.get("name")
        author = request.POST.get("author")
        date0 = request.POST.get("date0")
        date1 = request.POST.get("date1")
        reason = request.POST.get("reason")

        book = {
                "id": id,
                "name": name,
                "author": author,
                "date0": date0,
                "date1": date1,
                "reason": reason,
        }
        with open("system.json", "r", encoding='utf-8') as f:
            data = json.load(f)
        f.close()

        with open("system.json", 'w', encoding='utf-8') as f:
            data.append(book)
            f.write(json.dumps(data, indent=4))
            f.close()
        return render(request, "table/Title.html")