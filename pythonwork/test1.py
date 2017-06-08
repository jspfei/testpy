# -*- coding: utf-8 -*-
import json

path = 'E:\mywork\pythonwork\pydata-book-master\ch02\usagov_bitly_data2012-03-16-1331923249.txt'
#read all data by path
print open(path).readline()

#json to dict
recods = [json.loads(line) for line in open(path)]
print recods[0]
print recods[0]['tz']

#对时区进行计数
time_zones = [rec['tz'] for rec in recods if 'tz' in rec]
print time_zones[:10]

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] =1
    return counts
    
from collections import defaultdict

def get_counts2(sequence):
    counts = defaultdict(int)#初始化数值为 0
    for x in sequence:
        counts[x] +=1
    return counts
    
counts = get_counts(time_zones)
print counts['America/New_York']

print len(time_zones)

#前10位时区的计数
def top_counts(count_dict,n = 10):
    value_key_pairs = [(count,tz) for tz,count in count_dict.items()] 
        
    print len(value_key_pairs)
    value_key_pairs.sort()    
    return value_key_pairs[-n:]
    
print top_counts(counts)

# 另一个方法
from collections import Counter
counts = Counter(time_zones)
print counts.most_common(10)
    
