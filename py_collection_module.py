#author_by zhuxiaoliang
#2018-08-07 下午8:37

#1、可命名元祖
from collections import namedtuple
piont = namedtuple('point',['x','y'])
p = piont(2,1)
print(p)
print(p.x)#通过元素名字引用元素

#2、有序字典
from collections import OrderedDict
d = OrderedDict([('a',1),('b',2)])
print(type(d))

#3、默认字典
from collections import defaultdict
members = [
    ['male', 'John'],
    ['male', 'Jack'],
    ['female', 'Lily'],
    ['male', 'Pony'],
    ['female', 'Lucy'],
]
result = defaultdict(list)#传入默认的工厂方法，当获取一个不存在的key时候，使用该工厂方法的结果作为默认key值
for sex ,name in members:
    result[sex].append(name)
print(result)

#计数
s = 'ejroehfoealfjdlf'
from collections import Counter
print(Counter(s))


'''
输出：
point(x=2, y=1)
2
<class 'collections.OrderedDict'>
defaultdict(<class 'list'>, {'male': ['John', 'Jack', 'Pony'], 'female': ['Lily', 'Lucy']})
Counter({'e': 3, 'f': 3, 'j': 2, 'o': 2, 'l': 2, 'r': 1, 'h': 1, 'a': 1, 'd': 1})

'''