from operator import index
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def removepunc(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    print(djtext)
    #Analyze the text
    return HttpResponse("remove punc")


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if fullcaps == "on":
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'capitalize', 'analyzed_text': analyzed}
        djtext=analyzed


    if newlineremover == "on":
        analyzed=""
        for char in djtext:
            print(char)
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose':'capitalize', 'analyzed_text': analyzed}
        djtext=analyzed

    if (extraspaceremover == "on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass

            else:
                analyzed = analyzed + char

        params = {'purpose':'capitalize', 'analyzed_text': analyzed}
        djtext=analyzed

    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse("plz select checkbox")

        
        
    return render(request, 'analyze.html', params)
        


# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remove first")


# def spaceremove(request):
#     return HttpResponse("space remover back")

# def charcount(request):
#     return HttpResponse("charcount ")