import argparse
import numpy as np
import types
import urllib2
import string
import re
import ast

def calculate(inputstr,return_float=False,wolfram_switch=False):
    pod_start = '<pod title=\'Result\''
    start_marker = '<plaintext>'
    end_marker = '</plaintext>'
    cursor = 0

    if inputstr.count('_') != 0:
        raise ValueError
    
    try:
        if wolfram_switch:
            raise KeboardInterrupt
        if return_float:
            return float(eval(inputstr,{}))
        else:
            print(ast.lieteral_eval(inputstr))
    except:
        print 'Sending to Wolfram Alpha'
        url = 'http://api.wolframalpha.com/v2/query?input=' + inputstr.replace(' ','+') + '&appid=LUYEXY-UYY5P5Y48T'
        search = urllib2.urlopen(url)
        parsed = search.read()
        pod_loc = parsed.find(pod_start,cursor)
        info_loc = parsed.find(start_marker,pod_loc)
        info_loc += len(start_marker)
        end_loc = parsed.find(end_marker,info_loc)
        if return_float:
            float_exp = re.sub(r'[\s,a-z,\(,\)]','',parsed[info_loc:end_loc])
            try:
                return float(ast.literal_eval(float_exp))
            except:
                float_exp = float_exp.replace(float_exp[6:11],'e')
                float_exp = float_exp.replace('10^','')
            #float_exp = re.sub(r'[\xc]',r'[\*]',float_exp)
            #print type(float_exp)
                return float(ast.literal_eval(float_exp))
            #return answer
        else:
            print parsed[info_loc:end_loc]
    
def test_1():
    assert abs(4. - calculate('2**2')) < 0.001

def test_2():
    assert abs(7.3459e22 - calculate('mass of moon')) < 0.001
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Evaluation Parser')

    parser.add_argument('required_arg_1', help='Required string for evaluating')
    parser.add_argument('-W', action='store_true', default=False, dest='wolfram_switch', help='Evaluate the string argument with Wolfram Alpha')
    parser.add_argument('-f', action='store_true', default=False, dest='return_float', help='Return a value for further work')
    results = parser.parse_args()
    
    calculate(results.required_arg_1, results.return_float, results.wolfram_switch)