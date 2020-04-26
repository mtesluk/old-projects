from django.shortcuts import render


def api_info(request):
    return render(request, 'api/info_api.html')
