curl http://www.dumpalink.com/index/[1-396]>index_pages
pgrep -o "http://www.dumpalink.com/media/\d*/\w*" index_pages>index_pagelinks
wget -O pages -i index_pagelinks
pgrep -o "a href=\"http://\w+.dumpalink.com/media/\w+/\w+\.\w+\"" pages>vid_links
sed -i "s/.*\(http.*\.\w*\).*/\1/" vid_links
wget -i vid_links -c -e robots=off -nd -A .wmv
wget -i vid_links -c -e robots=off -nd -A .swf
