#!/usr/bin/env python

import argparse
import pythonwhois
import json
import datetime
import sys

filename = 'words_de-ending-with-it.txt'


def main():
    # fh = open('one-letter-id.txt')

    try:
        doman_storage = json.load(open('%s.json' % filename, 'r'))
        print 'found store',doman_storage
    except IOError:
        doman_storage = {}
        open('%s.json' % filename, 'w').write(json.dumps(doman_storage))

    fh = open(filename)
    for line in fh:
        line = line[:-1]
        if line in doman_storage:
            print 'skipped ',line
            continue
        data, server_list = pythonwhois.net.get_whois_raw(line, with_server_list=True)

        if len(server_list) > 0:
            parsed = pythonwhois.parse.parse_raw_whois(data, normalized=True, never_query_handles=False, handle_server=server_list[-1])
        else:
            parsed = pythonwhois.parse.parse_raw_whois(data, normalized=True)

        if 'status' not in parsed:
            print('free : %s' % line)
            doman_storage[line] = ['free.undefined']
        else:
            doman_storage[line] = parsed['status']
            print('%s : %s' % (parsed['status'][0], line))
        open('%s.json' % filename, 'w').write(json.dumps(doman_storage))
    fh.close()
    sys.exit(0)

if __name__ == "__main__":
    main()
