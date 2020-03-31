#题目2
#输出作者信息
def whoami():
    print("By QLNU" + "\n" + "AnMing")
    print("完成于3.30日14:59")

#Cirlce类，用来存放圆的周长，及求周长、面积的方法
class Cirlce:
    def __init__(self, round):
        self.round=round

    def perimeter(self):
        perimeter=2*Pi*self.round
        print("该圆的周长为：",perimeter)

    def area(self):
        area=Pi*self.round*self.round
        print("该圆的面积为：",area)
#获取圆半径的方法
def get_round():
    try:
        r = input("请输入圆的半径，默认值为5:\n")
        if r=='':
            return 5        #默认值为5
        else:
            return int(r)
    except:
        print("请检查输入！")

if __name__ == '__main__':
    whoami()
    Pi=3.14
    r=get_round()
    print("该圆的周长为：",r)
    round1 = Cirlce(r)
    round1.perimeter()
    round1.area()
