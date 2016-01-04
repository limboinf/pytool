# coding=utf-8
"""
序列中出现次数最多的元素
collections.Counter
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '1/4/16'


words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_count = Counter(words)
# 出现频率最高的3个单词
top_three = word_count.most_common(3)
print top_three
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]

print word_count['my']      # 3
