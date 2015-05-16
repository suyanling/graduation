# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
# 测试request参数包含的一些方法和属性
def testRequest(req):

    # return HttpResponse("welcome to the page at" + req.path)

    # ua = req.META.get('HTTP_USER_AGENT', 'unknown')
    # return HttpResponse("Your browser is %s" % ua)

    values = req.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % ''.join(html))


# 测试表单的使用的方法
def search(req):
    if 'q' in req.GET:
        message = 'you searched for: %s' % req.GET['q']
    else:
        message = 'you submitted an empty form'
    return HttpResponse(message)


def search_form(req):
    return render_to_response('search_form.html')


def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render('req', 'contact_form.html',
                  {'errors': errors})
