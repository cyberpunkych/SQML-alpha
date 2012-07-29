#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys

def split(string, ch):
    arr = map(lambda x: x.strip(), string.split(ch))
    return filter(lambda x: x != '', arr)

def error():
    print 'Error'
    sys.exit(0)

class Tag:
    def __init__(self, arr):
        self.attributes = arr
    def testme(self, condition):
        try:
            for k in self.attributes.keys():
                t = self.attributes[k].replace('"', '\"')
                exec('_'+str(k)+'="'+t+'"')
            __ans = eval(condition)
            if (__ans == None or __ans == False):
                return False
            return True
        except:
            return False
    def get(self,arr):
        data = {}
        for k in arr:
            t = k[1:]
            if (self.attributes.has_key(t)):
                data[t] = self.attributes[t]
            else:
                return {}
        return data

class Parser:
    def __init__(self):
        self.clear()
    def clear(self):
        self.text = ''
        self.result = [[]]
        self.count = 0
        self.value = {}
        self.tags = []
    def load(self, text):
        self.text = text
        t = re.findall('<(\w+)', self.text)
        t = list(set(t))
        self.tags = t
    def _parse_query(self, query):
        query = query.strip()
        if (query == 'SHOW ALL TAGS'):
            return 'SHOW ALL TAGS', None, None, None
        query = query.replace('@','_')
        m = re.search('SELECT (.+) FROM ([\S]+)(?: WHERE (.+))?', query)
        if (m != None):
            (data, tag_name, cond) = m.groups()
            data = data.strip()
            if (cond):
                cond = cond.strip()
            if (data == '' or cond == ''):
                error()
        else:
            error()
        return 'SELECT', data, tag_name, cond

    def _select_result(self, data, tag_name, cond):
        val = split(data,',')
        regexp = re.compile('<'+tag_name+'([^<>]*)>(?:(.*?)</'+tag_name+'>)?',re.DOTALL)
        parsed = regexp.findall(self.text)
        for row in parsed:
            params = re.findall('(\w+)=[\'|"](.+?)[\'|"]',row[0])
            params += re.findall('(\w+)=(\d+)',row[0])
            h = {}
            for k in params:
                h[k[0]] = k[1]
            h['_content'] = row[1]
            current_tag = Tag(h)
            if (cond and not(current_tag.testme(cond))):
                continue
            tmp = current_tag.get(val)
            if (tmp):
                m1 = []
                for s in val:
                    s = s[1:]
                    t = tmp[s]
                    m1.append(t)
                    if (self.value.has_key(s)):
                        self.value[s].append(t)
                    else:
                        self.value[s] = [t]
                self.result.append(m1)
        for k in self.value.keys():
            tmp = list(set(self.value[k]))
            tmp.sort()
            self.value[k] = tmp
        return self.result

    def query(self, query):
        self.result = []
        self.value = {}
        query_type, data, tag_name, cond = self._parse_query(query)
        if query_type == 'SELECT':
            return self._select_result(data, tag_name, cond)
        elif query_type == 'SHOW ALL TAGS':
            return self.tags

