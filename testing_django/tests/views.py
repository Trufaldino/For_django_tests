from django.shortcuts import render


def index(request):
    template = 'index.html'
    context = {
        'scheme': request.scheme,
        'body': request.body,
        'path': request.path,
        'path_info': request.path_info,
        'method': request.method,
        'encoding': request.encoding,
        'content_type': request.content_params,
        'GET': request.GET,
        'POST': request.POST,
        'COOKIES': request.COOKIES,
        'FILES': request.FILES,
        'META': request.META,
        'headers': request.headers,    
        'resolver_match': request.resolver_match,
        'session': request.session,
        # 'user': request.user,
    }
    return render(request, template, context) 
