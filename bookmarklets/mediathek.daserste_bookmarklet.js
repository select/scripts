javascript:(function(){
	s=document.getElementsByTagName('script');
	t='';
	for (i=0;i<s.length;++i){ 
		if (s[i].innerHTML.indexOf('mediaCollection.addMediaStream') !== -1) t=s[i].innerHTML; 
	}
	p=/mediaCollection.addMediaStream.0, 2, "rtmp:..vod.daserste.de\/ardfs\/.,..mp4:videoportal.mediathek.([^"]*).mp4/;
	m=p.exec(t);
	t=document.getElementsByClassName("boxTopHeadline")[0].innerHTML;
	r='curl rtmp://vod.daserste.de/ardfs/videoportal/mp4:mediathek/'+m[1]+'.mp4 -o "'+t+'.mp4"';
	window.prompt ("Copy to clipboard: Ctrl+C, Enter", r);
})();