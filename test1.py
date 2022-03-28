"""
 * Project name(项目名称)：Python_setattr函数_getattr函数和hasattr函数
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/28 
 * Time(创建时间)： 13:15
 * Version(版本): 1.0
 * Description(描述)： hasattr()函数
hasattr() 函数用来判断某个类实例对象是否包含指定名称的属性或方法。
hasattr(obj, name)
其中 obj 指的是某个类的实例对象，name 表示指定的属性名或方法名。同时，该函数会将判断的结果（True 或者 False）作为返回值反馈回来。
 """


class C:
    a = 1
    b = 2
    c = 3

    def __init__(self, a1, a2, a3) -> None:
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def f1(self):
        print("hello")


if __name__ == '__main__':
    c = C(2, 3, 4)
    print(hasattr(c, "a"))
    print(hasattr(c, "b"))
    print(hasattr(c, "c"))
    print(hasattr(c, "d"))
    print(hasattr(c, "A"))
    print(hasattr(c, "a1"))
    print(hasattr(c, "a2"))
    print(hasattr(c, "a3"))
    print(hasattr(c, "a4"))
    print(hasattr(c, "f1"))
    print(hasattr(c, "__init__"))
