#author_by zhuxiaoliang
#2018-07-31 下午6:45

#定义元类，需要继承type类，默认习惯用mataclass结尾
#元类中需要实现__new__()方法，而且该方法中要有返回值。
class MyClassMetaclass(type):
    def __new__(cls, *args, **kwargs):
        pass
        return super.__new__()
#之所以继承type类并实现__new__()方法，因为在创建类时，内部表用了__new__()方法为类分配空间，当内存空间分配好之后，调用type的__init__()
#方法进行初始化