# coding=utf8
# Create your views here.
from django.http import HttpResponse
import datetime

import sys

from django.db.models import Min, Max

from django.template import Context
from django.template.loader import get_template

from screen.models import infochannel, message

#def info(request, infochannel_id):
#    #første lasting av en kanal. render selve infochannel templaten
#    return render_to_response('infochannel.html', context_instance=RequestContext(request))

#use this anywhere for printing stuff to console
#print >>sys.stderr, 'checkpoint!'

def checkmessageexists(request):
    #følgende funker ikke med beskjed 'cannot concatenate 'str' and 'RawQuerySet' objects'
    #maxid = message.objects.raw('''SELECT MAX(id) as maxid FROM screen_message''')# WHERE channel_id = ' + kID)
    #print >>sys.stderr, 'maxid: ' + maxid

    kID = request.POST['channel']
    bID = request.POST['message']
    print >>sys.stderr, 'beskjed ID: ', bID
    print >>sys.stderr, 'kanal ID: ', kID

    if not _HasMessages(kID):
        response = HttpResponse()
        response['status'] = "EMPTY"
        return response

    if int(bID) == 0:
        print >>sys.stderr, 'henter minBeskjedId...'
        minID = message.objects.filter(channel=kID, active=True).aggregate(Min('id'))['id__min']
        print >>sys.stderr, 'min beskjed ID: ', minID
        bID = minID

    maxBeskjedId = message.objects.filter(channel=kID, active=True).aggregate(Max('id'))['id__max']
    print >>sys.stderr, 'maxBeskjedID: ', maxBeskjedId

    print >>sys.stderr, 'henter beskjed...'
    beskjed = None
    while beskjed is None:
        print >>sys.stderr, 'prøver beskjed id: ', bID
        if int(bID) > maxBeskjedId:
            response = HttpResponse()
            response['status'] = "MAX"
            return response
        print >>sys.stderr, 'ikke over max id...'
        try:
            beskjed = message.objects.get(channel=kID, id=bID)
            if not beskjed.active:
                beskjed = None
            else:
                print >>sys.stderr, 'hentet beskjed id: ', bID
        except message.DoesNotExist:
            beskjed = None
            bID = int(bID) + 1
            print >>sys.stderr, 'fant ingen beskjed'

    if beskjed is None or not beskjed.active:
        return HttpResponse('')
    else:
        #return HttpResponse(beskjed.headline + ' ' + beskjed.text)
        response = HttpResponse()
        response['status'] = "RETURNED"
        response['headline'] = beskjed.headline
        response['text'] = beskjed.text
        response['returnedMsgID'] = beskjed.id
        print >>sys.stderr, 'response none?: ', response is None
        print >>sys.stderr, 'response: ', response['headline'], response['text']
        return response

    #return render_to_response('infochannel.html', context_instance=RequestContext(request))

def _HasMessages(infochannel_id):
    antallAktiveBeskjeder = message.objects.filter(channel=infochannel_id, active=True).count()
    print >>sys.stderr, 'antallBeskjeder: ', antallAktiveBeskjeder
    return antallAktiveBeskjeder > 0

def info(request, infochannel_id):
    template = get_template('infochannel.html')
    kanalen =  infochannel.objects.get(id=infochannel_id)

    variables = Context({
        'head_title': u"Dette er infokanal %s." % kanalen.name,
        'page_title': u"Velkommen til infosiden med id %s." % kanalen.id,
        'channel_id': kanalen.id
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