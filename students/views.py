# -*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render
#from django.http import Http404
from django.http import HttpResponse
#from django.template import RequestContext, loader


#Create your views here.
#request
#response
#def students_list(request):
#    from ipdb import set_trace; set_trace()
#    response =  HttpResponse('<h1>hello test</h1>')
#    return response

#def students_list(request, sid):
#    try:
#        sid = int(sid)
#    except ValueError:
#        raise Http404
#    else:
#        return HttpResponse('<h1>hello</h1>')

#def students_list(request):
#    template = loader.get_template('demo.html')
#    context = RequestContext(request, {})
#    return HttpResponse(template.render(context))


#views for students

#def students_list(request):
#    return render(request, 'students-list.html', {})


#def render(request, template_name, context=None, content_type=None, status=None, using=None):
#    """
#    Returns a HttpResponse whose content is filled with the result of calling
#    django.template.loader.render_to_string() with the passed arguments.
#    """
#    content = loader.render_to_string(template_name, context, request, using=using)
#    return HttpResponse(content, content_type, status)

def students_list(request):
    students = (
        {'id' : 1,
         'first_name' : 'Julia',
         'last_name' : 'Dizhak',
         'ticket' : 1,
         'image' : 'img/icon-book2.png'
        },
        {'id' : 2,
         'first_name' : 'Vasyl',
         'last_name' : 'Dizhak',
         'ticket' : 2,
         'image' : 'img/define-icon.png'
        },
        {'id' : 3,
          'first_name' : 'test',
          'last_name' : 'Test',
          'ticket' : 3,
          'image' : 'img/icon-book2.png'
        },
        {'id' : 4,
         'first_name' : u'Bacя',
         'last_name' : 'Run',
         'ticket' : 4,
         'image' : 'img/define-icon.png'
         }
    )
    return render(request, 'students-list.html', {'students' : students, 'name': 'test', 'date': datetime.now(), 'year' : datetime.now().year})

def students_add(request):
    return HttpResponse('<h1>Student add form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit student %s</h1>' % sid)

#def students_edit(request, sid, gid):
#    return HttpResponse('<h1>Edit student %s %s</h1>' % (sid, gid))

def students_delete(request, sid):
    return HttpResponse('<h1>Delete student %s</h1>' % sid)


#views for groups

def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')

def groups_add(request):
    return HttpResponse('<h1>Groups add form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Groups edit %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Groups delete %s</h1>' % gid)
