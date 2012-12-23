#!/usr/bin/perl
use SOAP::Lite;
use Getopt::Std;
use warnings;
use strict;

#this is the documentation url
#http://sabio.villa-bosch.de/SABIORK/webservicedoc.jsp
#are there the right entry points for us? Can we ask for more entry points (e.g. searchReactionIDfromKeggID)
#

#--------------------------------------------------------------------
#option parser and option printout
use vars qw($opt_s $opt_t $opt_h);

my $helptext ="sabiork_soap_client.pl [OPTIONS]\n
\t-s <(parital)searchstring> getPathwayNames
\t-t <(parital)searchstring> searchCompounds 
\t-h print this help text\n\n";

my $not_yet_implemented_functions = "

\tsearchEnzymesByName 
\tsearchEnzymesByECNumber 
\tGenerateSBMLentities


\tgetReactionIDs
\tgetReactionEquation 
\tgetKinLawIDs 
\tgetKinLawIDsNotNull 
\tgetSubstrates 
\tgetProducts 
\tgetKineticLaw 
\tgetPubmedID 
\tgetParametersXML 
\tgetReactionIDFromCompound 
\tgetReactionIDFromEnzyme 
\tgetOrganismFromKLID 
\tgetCompoundID 
\tgetKEGGID 
\tgetCHEBIID 
\tgetECFromReactionID 
\tgetExpConditions 
\tgetActivator 
\tgetInhibitor 
\tgetCofactor 
\tgetSpeciesID 
\tgetLocationID 
\tgetLocationName 
\tgetTissue 
\tgetWildType ";


if ($#ARGV <0){print $helptext; exit 0;}
my $prog =  $0;
$prog =~ s,.*/,,;
getopts('s:t:h') or do{
	print $helptext; 
	exit 0;
};
if (defined $opt_h){print $helptext; exit 0;}


#--------------------------------------------------------------------
#INTERESTING PART STARTS HERE
#--------------------------------------------------------------------
#config
our $wsbaseurl = "http://sabio.villa-bosch.de/sabiows/sabiork.jws";


#--------------------------------------------------------------------
#function implementation, only testing
if(defined $opt_s){
	my $soap = getWs();
	my $result = $soap-> searchEnzymesByName($opt_s);
	foreach( returnArrayWsResultError($result)){
		print "$_\n";
	}
}
if(defined $opt_t){
	my $soap = getWs();
	my $result = $soap-> searchCompounds($opt_t);
	foreach( returnArrayWsResultError($result)){
		print "$_\n";
	}
}

#--------------------------------------------------------------------
#help functions for connecting the webservice and getting results
sub getWs {
        my $soap = SOAP::Lite
                -> uri("$wsbaseurl")
                -> proxy("$wsbaseurl", timeout => 9999);
	return $soap;
}

sub printWsResultError {
	my $result = shift;	
	unless ($result->fault) {                                                                                                    
                print $result->result();#print result, will show pointer to array if an array is returned
        } else {                                                                                                                     
                print join ', ',                                                                                                     
                $result->faultcode,                                                                                                  
                $result->faultstring;                                                                                                
        }	
}
sub returnArrayWsResultError {
	my $result = shift;	
	unless ($result->fault) {                                                                                                    
                return @{$result->result()};#return result as array
        } else {#if an error occured print what went wrong
                print join ', ',                                                                                                     
                $result->faultcode,                                                                                                  
                $result->faultstring;                                                                                                
        }
	return ();
}

sub method2_byWSDLfile {#no error messages last time I tryed so lets leave this as last resort
	print SOAP::Lite
    		-> service("$wsbaseurl?wsdl")
		-> searchEnzymesByName("phospho");
}
