import argparse
import numpy as np
import types
import urllib2
import string
import re

pod_start = '<pod title=\'Result\''
start_marker = '<plaintext>'
end_marker = '</plaintext>'
cursor = 0

parser = argparse.ArgumentParser(description='Evaluation Parser')

parser.add_argument('required_arg_1', help='Required string for evaluating')
parser.add_argument('-W', action='store_true', default=False, dest='wolfram_switch', help='Evaluate the string argument with Wolfram Alpha')

results = parser.parse_args()

try:
    if results.wolfram_switch:
        raise KeboardInterrupt
    print(eval(results.required_arg_1))
except:
    print 'Sending to Wolfram Alpha'
    url = 'http://api.wolframalpha.com/v2/query?input=' + results.required_arg_1.replace(' ','+') + '&appid=UAGAWR-3X6Y8W777Q'
    search = urllib2.urlopen(url)
    parsed = search.read()
    pod_loc = parsed.find(pod_start,cursor)
    info_loc = parsed.find(start_marker,pod_loc)
    info_loc += len(start_marker)
    end_loc = parsed.find(end_marker,info_loc)
    print parsed[info_loc:end_loc]