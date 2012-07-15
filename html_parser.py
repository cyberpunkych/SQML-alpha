#!/usr/bin/env python
import re

def split(string, ch):
    arr = map(lambda x: x.strip(), string.split(ch))
    return filter(lambda x: x != '', arr)

def error():
    print 'Error'
    sys.exit(0)

class Parser:
    def __init__(self):
        self.types = {}
        self.types['INT'] = '(\d+)'
        self.types['WORD'] = '(\w+)'
        self.types['DATE'] = '([\d]{4,4}[-|:|/][\d]{2,2}[-|:|/][\d]{2,2})'
        self.types['TEXT'] = '([\w!?.,- ]+)'
        self.clear()
    def clear(self):
        self.text = ''
        self.result = []
        self.count = 0
        self.value = {}
    def load(self, text):
        self.text = text
    def query(self, query):
        self.result = []
        m = re.search('SELECT(.+)FROM(.+)',query.strip())
        if (m != None):
            (data, tag_name) = m.groups()
        else:
            error()
        tag_name = tag_name.strip()
        if (tag_name == ''):
            error()
        values = split(data,',')
        regexp = '(<'+tag_name+'(?:[^<>]*)>[^<>]*</'+tag_name+'>)'
        tags = re.findall(regexp, self.text)
        for row in tags:
            r = ''
            h = {}
            for curr in values:
                (attr_type, attr_name) = split(curr,' ')
                if (self.types.has_key(attr_type)):
                    r = self.types[attr_type]
                else:
                    continue
                if (attr_name != '@@content'):
                    r = ' '+attr_name+'="'+r+'"'
                else:
                    r = '<'+tag_name+'.*>'+r+'</'+tag_name+'>'
                m = re.search(r, row)
                if (m != None):
                    h[attr_name] = m.groups()[0]
                else:
                    h[attr_name] = None
            ok = 0
            for k in h.keys():
                if (h[k] != None):
                    ok = 1
                    break
            if (ok):
                self.result.append(h)
        self.count = len(self.result)
        for a in self.result:
            for k in a.keys():
                if (a[k] == None):
                    continue
                if (self.value.has_key(k)):
                    self.value[k].append(a[k])
                else:
                    self.value[k] = [a[k]]
        for k in self.value.keys():
            t = self.value[k]
            self.value[k] = list(set(t))
            self.value[k].sort()
