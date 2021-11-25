# i have made this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext=request.POST.get("text", "default")
    removepunc=request.POST.get("removepunc", "off")
    fullcaps=request.POST.get("fullcaps", "off")
    newlineremover=request.POST.get("newlineremover", "off")
    extraspaceremover=request.POST.get("extraspaceremover", "off")
    charcount=request.POST.get("charcount", "off")
    print(removepunc)
    print(djtext)
    punctuations = '''!()-[]{};:'"\,<>.>/?@$#%^&*_~'''
    analyzed=""
    if removepunc == "on":
        # iterate kar diya 'djtext' ko for loop ki maddat se (each and every character is accessed)
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {"purpose": "Extra Space Removed", "analyzed_text": analyzed}
        djtext=analyzed
    # FULL CAPITAL LETTER KARNE KA PROGRAM HAI
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {"purpose": "Changed to Upper Case", "analyzed_text": analyzed}
        djtext = analyzed
        # return render(request, "analyze.html", params)

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        params = {"purpose": "Removed new lines", "analyzed_text": analyzed}
        djtext = analyzed
        # return render(request, "analyze.html", params)
    if(extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {"purpose": "Extra Space Removed", "analyzed_text": analyzed}
        # return render(request, "analyze.html", params)

    if (removepunc != "on" and fullcaps!= "on" and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse("ERROR")

    return render(request, "analyze.html", params)


