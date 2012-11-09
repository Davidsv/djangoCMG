# coding=utf8
# Create your views here.
from django.http import HttpResponse
import datetime

from django.template import Context
from django.template.loader import get_template

from screen.models import infochannel, message

def info(request, infochannel_id):
    template = get_template('infochannel.html')
    kanalen =  infochannel.objects.get(id=infochannel_id)

    beskjeder = []
    for m in message.objects.get(channel=infochannel_id) :
        beskjeder.append(m)

    #prøv å legge til beskjeder i dictionaryen som sendes til Context

    variables = Context({
        'head_title': u"Dette er infokanal %s." % kanalen.name,
        'page_title': u"Velkommen til infosiden med id %s." % kanalen.id,


        'javascripttest' : message.objects.get(channel=infochannel_id).headline
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