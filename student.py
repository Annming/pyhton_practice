#输出个人信息
def whoami():
    print("By QLNU" + "\n" + "AnMing")
    print("完成于3.30日16:24")

#创建Student类，用于存放学生信息及输出查询结果
class Student:
    def __init__(self,name,age,mathematics,political,english):
        self.name = name
        self.age = age
        self.mathematics = mathematics
        self.political = political
        self.english = english

    def getName(self):
        print(self.name,'同学')

    def getAge(self):
        print(self.name,'年龄为',self.age,'岁')

    def getGrade(self):
        strength=max(self.political,self.mathematics,self.english)
        if(strength == self.political):
            print (str(self.name)+"最好科目为政治"+str(self.political)+"分")
        if(strength == self.mathematics):
            print (str(self.name)+"最好科目为数学" + str(self.mathematics) + "分")
        if(strength == self.english):
            print (str(self.name)+"最好科目为英语" + str(self.english) + "分")

#输入学生姓名，并检查输入，若输入错误，可重新输入或输入0退出程序
def Input():
    while 1:
        person = input()
        if person == 'dm':
            student=dm
            print("您要查询的是：")
            student.getName()
            break
        elif person == 'xm':
            student=xm
            print("您要查询的是：")
            student.getName()
            break
        elif person == '0':
            break
        else:
            print('查无此人！请重新输入！(输入0退出程序)')
    return student

#查询函数，对查询结果输出，可通过输入代码查询想要的数值
def select(student):
    while 1:
        code=input('查询代码如下：\n    1.查询全部信息\n    2.查询年龄\n    3.查询最好成绩\n    0.结束查询\n请输入查询代码：\n')
        if code=='1':
            student.getName()
            student.getAge()
            student.getGrade()
            break
        elif code=='2':
            student.getAge()
            break
        elif code=='3':
            student.getGrade()
            break
        elif code=='0':
            break
        else:
            print('代码错误，请重新输入!')


if __name__ == '__main__':
    whoami()
    #实例化大明及小明两个同学
    zjw=Student("大明",18,100,100,99)
    xm=Student("小明",17,80,81,60)
    print("现有大明及小明两位同学，请输入要查询的同学的首字母：")
    select(Input())
