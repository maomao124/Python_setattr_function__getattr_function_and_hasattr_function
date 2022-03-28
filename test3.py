"""
 * Project name(项目名称)：Python_setattr函数_getattr函数和hasattr函数
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/28 
 * Time(创建时间)： 13:22
 * Version(版本): 1.0
 * Description(描述)： Python setattr()函数
它最基础的功能是修改类实例对象中的属性值。其次，它还可以实现为实例对象动态添加属性或者方法。
setattr(obj, name, value)
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

    print(c.a)
    setattr(c, "a", 111)
    print(c.a)
    print(c.a1)
    setattr(c, "a1", 222)
    print(c.a1)
    setattr(c, "a4", 2224)
    print(c.a4)
