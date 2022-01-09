# I created this file
from django.shortcuts import render


#
#
def index(request):
    return render(request, 'index.html')


def uppercase(request):
    djtext = request.POST.get('text', 'default')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    allspaceremover = request.POST.get('allspaceremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    if fullcaps == 'on':
        full = ""
        for char in djtext:
            full = full + char.upper()
        param = {'purpose': 'In Upper case: ', 'upper': full}
        djtext = full

    if newlineremover == 'on':
        remove = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                remove = remove + char
        param = {'purpose': 'New Line Removed: ', 'upper': remove}
        djtext = remove

    if allspaceremover == 'on':
        sremove = ""
        for char in djtext:
            if char != ' ':
                sremove = sremove + char
        param = {'purpose': 'All space Removed: ', 'upper': sremove}
        djtext = sremove

    if extraspaceremover == 'on':
        eremove = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                eremove = eremove + char
        param = {'purpose': 'Extra space removed: ', 'upper': eremove}
        djtext = eremove

    if fullcaps != 'on' and newlineremover != 'on' and allspaceremover != 'on' and extraspaceremover != 'on':
        param = {'purpose': 'Error Occurred', 'upper': 'Not Selected any Feature'}
        return render(request, 'uppercase.html', param)
    return render(request, 'uppercase.html', param)
