import string
import dateutil.parser
class mailTemplate:


    def __init__(self, events,template = "eventTemplate.html"):
        self.events = events
        self.template = template


    def newMessage(self):

        events= self.events

        template = open('eventTemplate.html',"r",encoding="utf-8").read()

        eventList = []
        if not events:
            print ('No upcoming events found.')
        for event in events:
            eventDict = dict()

            eventDict['start'] = event['start'].get('dateTime', event['start'].get('date'))
            eventDict['start'] = dateutil.parser.parse(eventDict['start']).strftime("%d %b %Y %H:%M:%S")

            eventDict['end'] = event['end'].get('dateTime', event['end'].get('date'))
            eventDict['end'] =  dateutil.parser.parse(eventDict['end']).strftime("%d %b %Y %H:%M:%S")

            try:
                eventDict['description'] = event['description']
            except KeyError:
                eventDict['description']="Puudu"

            try:
                eventDict['summary'] = event['summary']
            except KeyError:
                eventDict['summary']="Puudu"

            try:
                eventDict['location'] = event['location']
            except KeyError:
                eventDict['location']="Teadmata"
            eventList.append(eventDict)

        tpl = string.Template(template)


        events2mail = []

        for event in eventList:
            events2mail.append(tpl.substitute(event))

        eventsMerged = ''.join(events2mail)
        return eventsMerged



        #for event in events2mail:
        #    print (event)