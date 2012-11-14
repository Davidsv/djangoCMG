# coding=utf8
# Create your views here.
from django.http import HttpResponse
import datetime

from django.template import Context
from django.template.loader import get_template

from screen.models import infochannel, message

from django.shortcuts import render_to_response
from django.template import RequestContext

#def info(request, infochannel_id):
#    #første lasting av en kanal. render selve infochannel templaten
#    return render_to_response('infochannel.html', context_instance=RequestContext(request))

def checkmessageexists(request):
    #kanalID = request.POST.get('channel')
    #beskjedID = request.POST.get('message')

    #TODO http://stackoverflow.com/questions/6020928/how-to-get-post-data-in-django-1-3

    kanalID = request.POST['channel']
    beskjedID = request.POST['message']
    if beskjedID is None:
            return HttpResponse('beskjed er none')
    if kanalID is None:
        return HttpResponse('kanal er none')

    return HttpResponse('kanal:'+kanalID + ' beskjed:'+beskjedID)
#    beskjed = message.objects.get(channel=kanalID)[beskjedID]
#    if beskjed is None :
#        return HttpResponse('ingen beskjed')
#       #return False
#    else:
#        return HttpResponse('fant beskjed')
#        #return True

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