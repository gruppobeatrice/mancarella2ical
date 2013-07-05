from icalendar import Calendar, Event, UTC, LocalTimezone
from datetime  import datetime, timedelta

calendars = {}

inizio_corsi = datetime(2008, 2, 18)

file = open("current.gap")
for i in file.readlines():
	giorno, sigla, corso, ora_inizio, ora_fine, docente, anno_corso, laurea, codice_corso = i.split(";")

	ora_inizio_lezione, minuti_inizio_lezione = ora_inizio.split(":")
	ora_fine_lezione,   minuti_fine_lezione   = ora_fine.split(":")

	inizio_lezione = timedelta (days    = int(giorno) - 1,
	                            hours   = int(ora_inizio_lezione),
				    minutes = int(minuti_inizio_lezione))
	fine_lezione   = timedelta (days    = int(giorno) - 1,
	                            hours   = int(ora_fine_lezione),
				    minutes = int(minuti_fine_lezione))
	
	event = Event()
	event.add('dtstart', inizio_corsi + inizio_lezione)
	event.add('dtend',   inizio_corsi + fine_lezione)
	event.add('summary', sigla)

	try:
		calendars[sigla].add_component(event)
	except KeyError:
		calendars[sigla] = Calendar()
		calendars[sigla].add('prodid', '-//Importer Orario v0.1a//Gruppo Beatrice//')
		calendars[sigla].add('version', '2.0')
		calendars[sigla].add_component(event)

for sigla, cal in calendars.iteritems():
	output = open('cals/' + sigla.strip() + '.ics', 'w')
	output.write(cal.as_string())
