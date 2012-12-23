#!/usr/bin/env python
# coding: utf-8
'''
PB.txt2Homebank.csv is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PB.txt2Homebank.csv is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PB.txt2Homebank.csv.  If not, see <http://www.gnu.org/licenses/>.

Copyright (c) 2009 by Falko Krause <falko.krause@biologie.hu-berlin.de>.
'''
import re,codecs
from optparse import OptionParser

category_filter = [
        ('Haus','miete'),
        ('Haus','HELLWEG'),
        ('Haus','GEZ'),
        ('Haus','EICHNER'),
        ('Haus','NUON'),
        ('Gesundheit','APOTHEKE'),
        ('Gesundheit','DROGERIEMARKT'),
        ('Telekommunikation','FONIC'),
        ('Telekommunikation','SKYPE'),
        ('Nahrungsmittel','KAISERS'),
        ('Nahrungsmittel','ALDI'),
        ('Nahrungsmittel','REWE'),
        ('Nahrungsmittel','KAUFLAND'),
        ('Luxus','RESTAURANT'),
        ('Luxus','PIZZERIA'),
        ('Luxus','hotel'),
        ('Luxus','CAFE'),
        ('Luxus','UFA'),
        ('Telekommunikation','1&1'),
        ('Transport','BVG'),
        ('Transport','SHELL'),
        ('Transport','ARAL'),
        ('Kind','SOZIALWIRTSCHAFT')
        ]

if __name__ == "__main__":

    parser = OptionParser("%prog [options]\n\n Postbank Deutschland txt 2 Homebank csv\n Convert Postbank transfer exports to Homebank csv format")
    parser.add_option("-i", "--infile", dest="inf", help="in file name" )
    parser.add_option("-o", "--outfile", dest="outf", help="out file name" )
    (options, args) = parser.parse_args()
    if not options.inf or not options.outf:
        parser.print_help()
        parser.exit()
        
    fn=options.inf

    file_in = codecs.open(fn,'r','ISO-8859-1').read()
    out = u''
    #format PostBank
    #Datum;Wertstellung;Art;Buchungshinweis;Auftraggeber;Empfaenger;Betrag Euro;Saldo Euro
    for day,month,year,type,description,payee,reciver,eu,cnt in re.findall('\d{2}\.\d{2}\.\d{4}\t(\d{2})\.(\d{2})\.(\d{4})\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]*)\t(-*[\d\.]+),(\d{2})\t-*[\d\.]+,\d{2}',file_in):
        if reciver: description = reciver+': '+description
        curtag = ''
        for tag,keyword in category_filter:
            if keyword.lower() in description.lower():
                curtag = tag
                break
        eu = re.sub('\.','',eu)
        out += u"%s-%s-%s;0;%s;%s;%s;%s.%s;%s\n"%(day,month,year[2:],curtag,payee,description,eu,cnt,type)
        # format HomeBank:
        # date         => format should be DD-MM-YY
        # mode         => from 0=none to 5=personal transfert
        # info         => a string
        # payee        => a payee name
        # description  => a string
        # amount       => a number with a '.' as decimal seperator, ex: -24.12 or 36.75
        # date;mode;info;payee;description;amount;category
        #15-02-04;0;;;Some cash;-40,00;Withdrawal of cash

    outfn=options.outf
    codecs.open(outfn,'w','utf-8').write(out)

