javascript:(function(){
	l=document.getElementsByTagName('embed');
	t=l[0].attributes.flashvars.value;
	p=/fad=([^&]*)&startpic/;
	m=p.exec(t);
	l=document.getElementById('video_titel').getElementsByTagName('div');
	t=l[1].innerHTML;
	t=t.replace(/[^\w\s\.äöüÄÖÜß]/g,'_');
	r='curl '+m[1]+' -o "'+t+'.mp4"';
	window.prompt ("Copy to clipboard: Ctrl+C, Enter", r);
})();