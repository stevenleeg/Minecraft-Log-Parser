#!/usr/bin/env python
import re, datetime, operator, sys

actions = {
	"login": re.compile("([0-9]{4})\-([0-9]{2})\-([0-9]{2}) ([0-2][0-9])\:([0-9]{2})\:([0-9]{2}) \[INFO\] ([A-z0-9]*) ?\[\/[0-9.]{4,15}\:[0-9]*\]"),
	"logout": re.compile("([0-9]{4})\-([0-9]{2})\-([0-9]{2}) ([0-2][0-9])\:([0-9]{2})\:([0-9]{2}) \[INFO\] ([A-z0-9]*) lost connection")
}

path = "server.log"
if sys.argv[1]:
    path = sys.argv[1]

f = open(path)

online = {}
totals = {}
for line in f.readlines():
	regex = None
	action = None
	player = None
	time = None
	for action in actions:
		if actions[action].match(line):
			regex = actions[action]
			break
	
	if regex is not None:
		# Get the user's name and parse the datetime
		data = regex.split(line)
		player = data[7]
		time = datetime.datetime(int(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[5]), int(data[6]))
	
		# Now do things!
		if action is "login":
			online[player] = time
		elif action is "logout":
			if player not in totals:
			   totals[player] = 0
			delta = time - online[player]
			totals[player] += delta.seconds

sort = sorted(totals.iteritems(), key=operator.itemgetter(1))
times = []
for player in sort:
    # Convert to hours/minutes/seconds
    time = "%20s: " % player[0]
    total = player[1]
    days = total / 86400
    if days > 0:
        time += "%2s days" % int(days)
        total -= int(days) * 86400
    else:
        time += "       "
    hours = total / 3600
    if hours > 0:
        time += " %2s hours" % int(hours)
        total -= int(hours) * 3600
    else:
        time += "         "
    mins = total / 60
    if mins > 0:
        time += " %2s minutes" % int(mins)
        total -= int(mins) * 60
    else:
        time += "           "
    if total > 0:
        time += " %2s seconds" % total
    
    times.append(time)

times.reverse()

counter = 0
for time in times:
    counter = counter + 1
    print "%2d) %s" % (counter, time)
f.close()
