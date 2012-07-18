<<<<<<< HEAD
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
=======
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
    def query(self, query):
        self.result = []
        self.value = {}
        cond = None
        query = query.strip()
        if (query == 'SHOW ALL TAGS'):
            return self.tags
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
>>>>>>> e80a5218d724dc95c5a445f80b52f0bb1960461c
