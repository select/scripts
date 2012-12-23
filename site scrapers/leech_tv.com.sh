curl -L "http://www.tv.com/shows/az.html&era=&l=[a-z]&g=">tv.com_show_index_a-z 
curl -L "http://www.tv.com/shows/az.html&era=&l=9&g=">tv.com_show_index_9
cat tv.com_show_index_9 tv.com_show_index_a-z >tv.com_show_index_a-z9
rm tv.com_show_index_a-z
rm tv.com_show_index_9
egrep 'pg_artists' tv.com_show_index_a-z9 >subindex.html
wget -O tv.com_show_index_a-z9_subindex -F -i subindex.html -B http://www.tv.com
rm subindex.html
cat tv.com_show_index_a-z9 tv.com_show_index_a-z9_subindex >tv.com_show_index_a-z9_complete
rm tv.com_show_index_a-z9
rm tv.com_show_index_a-z9_subindex
egrep -o 'http://www.tv.com/(\w|-)+/show/\w+/summary.html' tv.com_show_index_a-z9_complete
