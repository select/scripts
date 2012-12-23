#!/usr/bin/env python
from SOAPpy import WSDL
from optparse import OptionParser

#--------------------------------------------------------------
parser = OptionParser()
parser.add_option("-e", "--searchec", dest="ecnumber", help="search enzyme by ECNUMBER", metavar="ECNUMBER")
parser.add_option("-n", "", dest="ebyname", help="search enzyme by NAME", metavar="NAME")
(options, args) = parser.parse_args()


#http://sabio.villa-bosch.de/SABIORK/webservicedoc.jsp
#--------------------------------------------------------------
WSDLFILE = 'http://sabio.villa-bosch.de/sabiows/sabiork.jws?wsdl'
#WSDLFILE = 'sabiork.wsdl'

#--------------------------------------------------------------
server = WSDL.Proxy(WSDLFILE)


#--------------------------------------------------------------
#actual ws function access
result = ''
if options.ecnumber:
	result = server.searchEnzymesByECNumber(options.ecnumber)
if options.ebyname:
	result = server.searchEnzymesByName(options.ebyname) 

#--------------------------------------------------------------

result = server.getReactionIDFromEnzyme(result[0])
kID2rID = {}
for reactID in result:
	for kinID in server.getKinLawIDsNotNull(reactID):
		kID2rID[kinID]=reactID
		print 'products for '+str(kinID)+' ('+server.getOrganismFromKLID(kinID)+') are: \n'
		print server.getProducts(reactID)
		print 'substrates for '+str(kinID)+' ('+server.getOrganismFromKLID(kinID)+') are: \n'
		print server.getSubstrates(reactID)
		print '/////////////////////////////////////////////////////////////////'
		#print 'sorry no kinetic laws for '+kinID+' ('+server.getOrganismFromKLID(kinID)+') \n'
kinID = 'X'
print kID2rID.keys()
#while not kID2rID.has_key(kinID):
kinID=raw_input("Wich ID do you want?")
print kinID
#now we get the SBML file for only one reaction
result = server.GenerateSBMLentities([kID2rID[kinID]],{kID2rID[kinID]:kinID},1,2,'test model name')
print result

"""
>functions list
getPathwayNames
searchCompounds 
searchEnzymesByName 
searchEnzymesByECNumber 
GenerateSBMLentities
getReactionIDs
getReactionEquation 
getKinLawIDs 
getKinLawIDsNotNull 
getSubstrates 
getProducts 
getKineticLaw 
getPubmedID 
getParametersXML 
getReactionIDFromCompound 
getReactionIDFromEnzyme 
getOrganismFromKLID 
getCompoundID 
getKEGGID 
getCHEBIID 
getECFromReactionID 
getExpConditions 
getActivator 
getInhibitor 
getCofactor 
getSpeciesID 
getLocationID 
getLocationName 
getTissue 
getWildType """


		
