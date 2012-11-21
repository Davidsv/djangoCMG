# coding=utf8
# Create your views here.
from django.http import HttpResponse
import datetime


import sys

from django.template import Context
from django.template.loader import get_template

from screen.models import infochannel, message

from django.shortcuts import render_to_response
from django.template import RequestContext

#def info(request, infochannel_id):
#    #første lasting av en kanal. render selve infochannel templaten
#    return render_to_response('infochannel.html', context_instance=RequestContext(request))

#use this anywhere for printing stuff to console
#print >>sys.stderr, 'checkpoint!'

def checkmessageexists(request):
    #beskjed = message.objects.get(channel=1, id=1)

    kID = request.POST['channel']
    bID = request.POST['message']

    print >>sys.stderr, 'checkpoint!'

    beskjed = message.objects.get(channel=kID, id=bID)

    if beskjed is None :
        return HttpResponse("INGENTING")
    else:
        return HttpResponse(beskjed.headline + " " + beskjed.text)
        #return HttpResponse({'headline':beskjed.headline, 'text':beskjed.text})

    #return render_to_response('infochannel.html', context_instance=RequestContext(request))

def info(request, infochannel_id):
    template = get_template('infochannel.html')
    kanalen =  infochannel.objects.get(id=infochannel_id)

    #beskjeder = []
    #for m in message.objects.get(channel=infochannel_id) :
    #    beskjeder.append(m)

    #prøv å legge til beskjeder i dictionaryen som sendes til Context

    variables = Context({
        'head_title': u"Dette er infokanal %s." % kanalen.name,
        'page_title': u"Velkommen til infosiden med id %s." % kanalen.id,
        'channel_id': kanalen.id
        #'javascripttest' : message.objects.get(channel=infochannel_id).headline
    })
    output = template.render(variables)
    return HttpResponse(output)

#def info(request, infochannel_id):
#html = "<html><body>infochannels name is %s.</body></html>" % infochannel.objects.get(id=infochannel_id).name
#   html = "<html><body>message text is %s</body></html>" % message.objects.get(channel=infochannel_id).text
#  return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)