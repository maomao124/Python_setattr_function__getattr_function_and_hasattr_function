"""
 * Project name(项目名称)：Python_setattr函数_getattr函数和hasattr函数
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/28 
 * Time(创建时间)： 13:19
 * Version(版本): 1.0
 * Description(描述)： Python getattr() 函数
getattr() 函数获取某个类实例对象中指定属性的值。没错，和 hasattr() 函数不同，该函数只会从类对象包含的所有属性中进行查找。
getattr() 函数的语法格式如下：
getattr(obj, name[, default])
其中，obj 表示指定的类实例对象，name 表示指定的属性名，而 default 是可选参数，用于设定该函数的默认返回值，
即当函数查找失败时，如果不指定 default 参数，则程序将直接报 AttributeError 错误，反之该函数将返回 default 指定的值。

 """


class C:
    a = 1
    b = 2
    c = 3

    def __init__(self, a1, a2, a3) -> None:
        self.__a1 = a1
        self.a2 = a2
        self.a3 = a3

    def f1(self):
        print("hello")


if __name__ == '__main__':
    c = C(2, 3, 4)

    print(getattr(c, "f1"))
    print(getattr(c, "f2", "没找到"))
    print(getattr(c, "a", "没找到"))
    print(getattr(c, "b", "没找到"))
    print(getattr(c, "c", "没找到"))
    print(getattr(c, "_C__a1", "没找到"))
    print(getattr(c, "a1", "没找到"))
    print(getattr(c, "a2", "没找到"))
    print(getattr(c, "a3", "没找到"))




