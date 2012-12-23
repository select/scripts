#!/usr/bin/env python
'''
fritz.box.stats is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

fritz.box.stats is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with fritz.box.stats.  If not, see <http://www.gnu.org/licenses/>.

Copyright (c) 2009 by Falko Krause <falko.krause@biologie.hu-berlin.de>.
'''

from optparse import OptionParser

if __name__ == "__main__":

	parser = OptionParser("%prog [options]\n\n FRITZ!Box telephone call history export statistics")
	parser.add_option("-i", "--infile", dest="infile", help="in file name" )
	(options, args) = parser.parse_args()
	if not options.infile:
		parser.print_help()
		parser.exit()

	#------------------------------------------
	#read table into dict
	types=['Typ','Datum','Name','Rufnummer','Nebenstelle','Eigene Rufnummer','Dauer']
	call_type={1:'incoming',2:'missed',3:'outgoing'}
	FH=open(options.infile,'r')
	start=False
	table=[]
	for line in FH.readlines():
		if line.startswith('Typ') or line=='\n':
			start=True
			continue
		if start:
			line=line[:-1].split(';')
			entry={}
			for i,type in enumerate(types):
				entry[type]=line[i]
			if entry['Rufnummer'].startswith('030'):entry['Rufnummer']=entry['Rufnummer'][3:]
			table.append(entry)
	#------------------------------------------
	#read table into dict
	#make stats
	length_per_number={}
	calls_length_per_number_by_type={1:{},2:{},3:{}}
	calls_per_number={}
	Rufnummer2Name={}
	num_calls_all=0
	for entry in table:
		num_calls_all+=1
		if not Rufnummer2Name.has_key(entry['Rufnummer']):
			Rufnummer2Name[entry['Rufnummer']]=entry['Name']
		(h,m)=entry['Dauer'].split(':')
		h=int(h)
		m=int(m)
		m+=h*60
		try:
			calls_length_per_number_by_type[int(entry['Typ'])][entry['Rufnummer']][0] += m
			calls_length_per_number_by_type[int(entry['Typ'])][entry['Rufnummer']][1] += 1
		except KeyError:
			calls_length_per_number_by_type[int(entry['Typ'])][entry['Rufnummer']] = [m,1]
		try:
			length_per_number[entry['Rufnummer']] += m
		except KeyError:
			length_per_number[entry['Rufnummer']] = m
		try:
			calls_per_number[entry['Rufnummer']] += 1
		except KeyError:
			calls_per_number[entry['Rufnummer']] = 1

	from operator import itemgetter
	# Items sorted by value
	#    The keyword argument `key` allows easy selection of sorting criteria
	length_per_number=sorted(length_per_number.items(), key=itemgetter(1))

	for number,min in length_per_number:
		num_calls=calls_per_number[number]
		name = Rufnummer2Name[number] or number
		if not name: name = 'unbekannt'
		print '%-20s%4s%5s%5s%5s%5s%5s%5s%5s'%(name,min,num_calls,calls_length_per_number_by_type[1][number][0],calls_length_per_number_by_type[1][number][1],calls_length_per_number_by_type[2][number][0],calls_length_per_number_by_type[2][number][1],calls_length_per_number_by_type[3][number][0],calls_length_per_number_by_type[3][number][1],)
	print '-------------'
	print '%-20s%9s'%('Anzahl aller Anrufe',num_calls_all)

