import pyodbc
import os
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

connection = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};"
                      "Server=YOURSERVERNAME;"
                      "Database=YOURDATABASENAME;"
                      "Trusted_Connection=yes;")

cursor = connection.cursor()
def index(request):
    return render(request, "index.htm")

def importdata(request):
    return HttpResponse("Hello World")

def databaseView(request):
    content = open("templates/viewDatabase.htm", "r").read()
    cursor.execute("select username, password, data from BasicAuthentication;")
    data = cursor.fetchall()
    fullData = ""
    for i in data:
        fullData = fullData + f"""
<tr>
    <td>{i[0]}</td>
    <td>{i[1]}</td>
    <td>{i[2]}</td>
</tr>"""
    
    content = content.format(open("styling.css").read(), fullData)
    return HttpResponse(content)

def creation(request):
    return render(request, "creation.htm")

def editdatabase(request):
    data = request.GET
    username = data.get("username")
    password=data.get("password")
    dataDetailed=data.get("data")

    if username != None and password != None and dataDetailed != None and dataDetailed != "" and password != "" and username != "":
        try:
            cursor.execute(f"""
    INSERT INTO BasicAuthentication(username, password, data)
    VALUES('{username}', '{password}', '{dataDetailed}')""")
            cursor.commit()
        except pyodbc.IntegrityError:
            pass
    return render(request, "editDatabase.htm")
