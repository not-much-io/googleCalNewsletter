import string
import dateutil.parser
from sendMail import mailer

class mailTemplate:


    def __init__(self, events,template = "eventTemplate.html"):
        self.events = events
        self.template = template


    def newMessage(self):

        events= [{'end': {'dateTime': '2015-09-07T20:00:00+03:00'}, 'organizer': {'email': 'c28hbeqbtg3ri59eebm6fp3bto@group.calendar.google.com', 'displayName': 'Lahedad IT üritused', 'self': True}, 'htmlLink': 'https://www.google.com/calendar/event?eid=MGRtcnEyamd0c2pwZXRkdmpoMWpzYmdxajQgYzI4aGJlcWJ0ZzNyaTU5ZWVibTZmcDNidG9AZw', 'summary': 'Hackerspace Projects FollowUp', 'created': '2015-08-29T13:30:59.000Z', 'etag': '"2883269676430000"', 'reminders': {'useDefault': True}, 'iCalUID': '0dmrq2jgtsjpetdvjh1jsbgqj4@google.com', 'kind': 'calendar#event', 'sequence': 0, 'status': 'confirmed', 'updated': '2015-09-07T14:07:18.215Z', 'id': '0dmrq2jgtsjpetdvjh1jsbgqj4', 'start': {'dateTime': '2015-09-07T18:00:00+03:00'}, 'location': 'Room: 314 IT College, Mustamäe, Tallinn, Tallinna linn, Estonia', 'creator': {'email': 'kristo.koert@gmail.com', 'displayName': 'Kristo Koert'}}, {'end': {'dateTime': '2015-09-08T20:00:00+03:00'}, 'organizer': {'email': 'c28hbeqbtg3ri59eebm6fp3bto@group.calendar.google.com', 'displayName': 'Lahedad IT üritused', 'self': True}, 'htmlLink': 'https://www.google.com/calendar/event?eid=NWNtMnY5b25obzRoczBxZGNnaWdwaHVydjggYzI4aGJlcWJ0ZzNyaTU5ZWVibTZmcDNidG9AZw', 'summary': 'Lapikute infoõhtu 2', 'created': '2015-09-01T16:22:35.000Z', 'etag': '"2882249136076000"', 'reminders': {'useDefault': True}, 'iCalUID': '5cm2v9onho4hs0qdcgigphurv8@google.com', 'kind': 'calendar#event', 'sequence': 0, 'status': 'confirmed', 'updated': '2015-09-01T16:22:48.038Z', 'id': '5cm2v9onho4hs0qdcgigphurv8', 'start': {'dateTime': '2015-09-08T18:00:00+03:00'}, 'location': 'Lapikute kontor, Akadeemia tee 5', 'creator': {'email': 'lauri.vosandi@gmail.com', 'displayName': 'Lauri Võsandi'}}, {'end': {'dateTime': '2015-09-09T20:00:00+03:00', 'timeZone': 'Europe/Tallinn'}, 'originalStartTime': {'dateTime': '2015-09-09T18:00:00+03:00', 'timeZone': 'Europe/Tallinn'}, 'organizer': {'email': 'c28hbeqbtg3ri59eebm6fp3bto@group.calendar.google.com', 'displayName': 'Lahedad IT üritused', 'self': True}, 'htmlLink': 'https://www.google.com/calendar/event?eid=aWJldTkyY282bGpqamoxamduYW9xNXRpNzhfMjAxNTA5MDlUMTUwMDAwWiBjMjhoYmVxYnRnM3JpNTllZWJtNmZwM2J0b0Bn', 'summary': 'CodeClub: Python', 'created': '2015-08-29T12:06:43.000Z', 'etag': '"2881700896946000"', 'reminders': {'useDefault': True}, 'iCalUID': 'ibeu92co6ljjjj1jgnaoq5ti78@google.com', 'kind': 'calendar#event', 'sequence': 1, 'status': 'confirmed', 'updated': '2015-08-29T12:14:08.473Z', 'recurringEventId': 'ibeu92co6ljjjj1jgnaoq5ti78', 'id': 'ibeu92co6ljjjj1jgnaoq5ti78_20150909T150000Z', 'start': {'dateTime': '2015-09-09T18:00:00+03:00', 'timeZone': 'Europe/Tallinn'}, 'location': 'TTÜ innovatsiooni- ja ettevõtluskeskus MEKTORY, Raja 15, Mustamäe, 12618 Harju County, Estonia', 'creator': {'email': 'kristo.koert@gmail.com', 'displayName': 'Kristo Koert'}}, {'end': {'dateTime': '2015-09-10T19:00:00+03:00'}, 'organizer': {'email': 'c28hbeqbtg3ri59eebm6fp3bto@group.calendar.google.com', 'displayName': 'Lahedad IT üritused', 'self': True}, 'summary': 'Getting started with Raspberry Pi', 'created': '2015-08-27T16:21:52.000Z', 'etag': '"2881386251816000"', 'reminders': {'useDefault': True}, 'iCalUID': '0412rtunv2bcuhpia1s6mrotuo@google.com', 'kind': 'calendar#event', 'sequence': 0, 'status': 'confirmed', 'updated': '2015-08-27T16:32:05.908Z', 'description': 'Organized by Linux User Group of Estonian IT College', 'id': '0412rtunv2bcuhpia1s6mrotuo', 'start': {'dateTime': '2015-09-10T17:00:00+03:00'}, 'htmlLink': 'https://www.google.com/calendar/event?eid=MDQxMnJ0dW52MmJjdWhwaWExczZtcm90dW8gYzI4aGJlcWJ0ZzNyaTU5ZWVibTZmcDNidG9AZw', 'creator': {'email': 'lauri.vosandi@gmail.com', 'displayName': 'Lauri Võsandi'}}, {'end': {'dateTime': '2015-09-14T18:00:00+03:00'}, 'organizer': {'email': 'c28hbeqbtg3ri59eebm6fp3bto@group.calendar.google.com', 'displayName': 'Lahedad IT üritused', 'self': True}, 'summary': 'Robootika lahti', 'created': '2015-09-07T15:20:06.000Z', 'etag': '"2883278416656000"', 'reminders': {'useDefault': True}, 'iCalUID': '5svud0m41o1v7mkgihmpoqaje4@google.com', 'kind': 'calendar#event', 'sequence': 0, 'status': 'confirmed', 'updated': '2015-09-07T15:20:08.328Z', 'id': '5svud0m41o1v7mkgihmpoqaje4', 'start': {'dateTime': '2015-09-14T14:00:00+03:00'}, 'htmlLink': 'https://www.google.com/calendar/event?eid=NXN2dWQwbTQxbzF2N21rZ2lobXBvcWFqZTQgYzI4aGJlcWJ0ZzNyaTU5ZWVibTZmcDNidG9AZw', 'creator': {'email': 'lauri.vosandi@gmail.com', 'displayName': 'Lauri Võsandi'}}, {'end': {'dateTime': '2015-09-14T20:00:00+03:00'}, 'organizer': {'email': 'c28hbeqbtg3ri59eebm6fp3bto@group.calendar.google.com', 'displayName': 'Lahedad IT üritused', 'self': True}, 'htmlLink': 'https://www.google.com/calendar/event?eid=MGhscm1mNmtobjJpMjM4Ym5na2FvZnY4bm8gYzI4aGJlcWJ0ZzNyaTU5ZWVibTZmcDNidG9AZw', 'summary': 'The fundamentals of writing code', 'created': '2015-08-29T11:59:12.000Z', 'etag': '"2881710013732000"', 'reminders': {'useDefault': True}, 'iCalUID': '0hlrmf6khn2i238bngkaofv8no@google.com', 'kind': 'calendar#event', 'sequence': 1, 'status': 'confirmed', 'updated': '2015-08-29T13:30:06.866Z', 'id': '0hlrmf6khn2i238bngkaofv8no', 'start': {'dateTime': '2015-09-14T18:00:00+03:00'}, 'location': 'IT College, 12616 Tallinn, Estonia', 'creator': {'email': 'kristo.koert@gmail.com', 'displayName': 'Kristo Koert'}}, {'end': {'dateTime': '2015-09-16T18:00:00+03:00'}, 'organizer': {'email': 'c28hbeqbtg3ri59eebm6fp3bto@group.calendar.google.com', 'displayName': 'Lahedad IT üritused', 'self': True}, 'summary': 'Sumorobotite töötuba', 'created': '2015-09-07T15:19:07.000Z', 'etag': '"2883278333528000"', 'reminders': {'useDefault': True}, 'iCalUID': 'i0phu7ic0ci2dqdrm8plav7hm8@google.com', 'kind': 'calendar#event', 'sequence': 0, 'status': 'confirmed', 'updated': '2015-09-07T15:19:26.764Z', 'id': 'i0phu7ic0ci2dqdrm8plav7hm8', 'start': {'dateTime': '2015-09-16T16:00:00+03:00'}, 'htmlLink': 'https://www.google.com/calendar/event?eid=aTBwaHU3aWMwY2kyZHFkcm04cGxhdjdobTggYzI4aGJlcWJ0ZzNyaTU5ZWVibTZmcDNidG9AZw', 'creator': {'email': 'lauri.vosandi@gmail.com', 'displayName': 'Lauri Võsandi'}}, {'end': {'dateTime': '2015-09-16T20:00:00+03:00', 'timeZone': 'Europe/Tallinn'}, 'originalStartTime': {'dateTime': '2015-09-16T18:00:00+03:00', 'timeZone': 'Europe/Tallinn'}, 'organizer': {'email': 'c28hbeqbtg3ri59eebm6fp3bto@group.calendar.google.com', 'displayName': 'Lahedad IT üritused', 'self': True}, 'htmlLink': 'https://www.google.com/calendar/event?eid=aWJldTkyY282bGpqamoxamduYW9xNXRpNzhfMjAxNTA5MTZUMTUwMDAwWiBjMjhoYmVxYnRnM3JpNTllZWJtNmZwM2J0b0Bn', 'summary': 'CodeClub: Python', 'created': '2015-08-29T12:06:43.000Z', 'etag': '"2881700896946000"', 'reminders': {'useDefault': True}, 'iCalUID': 'ibeu92co6ljjjj1jgnaoq5ti78@google.com', 'kind': 'calendar#event', 'sequence': 1, 'status': 'confirmed', 'updated': '2015-08-29T12:14:08.473Z', 'recurringEventId': 'ibeu92co6ljjjj1jgnaoq5ti78', 'id': 'ibeu92co6ljjjj1jgnaoq5ti78_20150916T150000Z', 'start': {'dateTime': '2015-09-16T18:00:00+03:00', 'timeZone': 'Europe/Tallinn'}, 'location': 'TTÜ innovatsiooni- ja ettevõtluskeskus MEKTORY, Raja 15, Mustamäe, 12618 Harju County, Estonia', 'creator': {'email': 'kristo.koert@gmail.com', 'displayName': 'Kristo Koert'}}, {'end': {'dateTime': '2015-09-17T19:00:00+03:00'}, 'organizer': {'email': 'c28hbeqbtg3ri59eebm6fp3bto@group.calendar.google.com', 'displayName': 'Lahedad IT üritused', 'self': True}, 'summary': 'Getting started with Python', 'created': '2015-08-27T16:31:38.000Z', 'transparency': 'transparent', 'etag': '"2881411384052000"', 'reminders': {'useDefault': True}, 'iCalUID': '5m76dng5dg4jpa1uetn55j2140@google.com', 'kind': 'calendar#event', 'sequence': 3, 'status': 'confirmed', 'updated': '2015-08-27T20:01:32.026Z', 'description': 'Organized by Linux User Group of Estonian IT College', 'id': '5m76dng5dg4jpa1uetn55j2140', 'start': {'dateTime': '2015-09-17T17:00:00+03:00'}, 'htmlLink': 'https://www.google.com/calendar/event?eid=NW03NmRuZzVkZzRqcGExdWV0bjU1ajIxNDAgYzI4aGJlcWJ0ZzNyaTU5ZWVibTZmcDNidG9AZw', 'creator': {'email': 'lauri.vosandi@gmail.com', 'displayName': 'Lauri Võsandi'}}, {'end': {'dateTime': '2015-09-19T17:00:00+03:00'}, 'organizer': {'email': 'c28hbeqbtg3ri59eebm6fp3bto@group.calendar.google.com', 'displayName': 'Lahedad IT üritused', 'self': True}, 'htmlLink': 'https://www.google.com/calendar/event?eid=MGsxNWxxcTc2MmJzbnNqODMxbzRyYjBmcWcgYzI4aGJlcWJ0ZzNyaTU5ZWVibTZmcDNidG9AZw', 'summary': 'Software Freedom Day', 'created': '2015-08-27T16:19:17.000Z', 'transparency': 'transparent', 'etag': '"2881384860712000"', 'reminders': {'useDefault': True}, 'iCalUID': '0k15lqq762bsnsj831o4rb0fqg@google.com', 'kind': 'calendar#event', 'sequence': 1, 'status': 'confirmed', 'updated': '2015-08-27T16:20:30.356Z', 'description': 'Organized by Estonian Free and Open-Source Software Association', 'id': '0k15lqq762bsnsj831o4rb0fqg', 'start': {'dateTime': '2015-09-19T12:00:00+03:00'}, 'location': 'Vabaduse väljak, Tallinn, Estonia', 'creator': {'email': 'lauri.vosandi@gmail.com', 'displayName': 'Lauri Võsandi'}}]

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