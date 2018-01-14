# Write By Sunwl
# 2017/10/26
#
# 学生管理系统
# 主模块用于启动
# python 3.6.2

import time
import student
import pickle as p
import os

# docs = []  # 放置格式化好的学生信息
student_infos = []  # 放置所有学生信息

# 初始化选择菜单
def menu():
    print("+-------------------------------+")
    print("| 1) 添加学生信息               |")
    print("| 2) 显示所有学生信息           |")
    print("| 3) 删除学生信息               |")
    print("| 4) 修改学生成绩               |")
    print("| 5) 按学生成绩高低显示学生信息 |")
    print("| 6) 按学生成绩低高显示学生信息 |")
    print("| 7) 保存学生信息               |")
    print("| 8) 打开已存的学生信息         |")
    print("| 9) 查找学生信息               |")
    print("| q) 退出（不保存）             |")
    print("+-------------------------------+")

# 绘制学生输出信息
def _lines():
    print("+-------------+-------------+-------------+")

def _title():
    print("|    姓名     |    年龄     |    成绩     |")

# 添加_学生信息
def add_student():
    try:
        while True:
            name = input("请输入姓名(退出请输入'q'):")
            if name == 'q':
                break
            else:
                age = int(input("请输入学生年龄:"))
                score = int(input("请输入学生成绩:"))
                # s = student.Student(name, age, score)
                D = {"name":name,"age":age,"score":score}
                # docs.append(s)
                student_infos.append(D)
                print('添加成功！')
    except:
        pass

# 显示_学生信息
def show_students(infos):
    width = 13
    _lines()
    _title()
    _lines()

    for x in infos:
        name_info = x['name']
        age_info = str(x['age'])
        score_info = str(x['score'])

        print('|%s|%s|%s|' % (name_info.center(width),
            age_info.center(width),
            score_info.center(width)))

    # for x in docs:
        # x.infos()
        # print(x)
    _lines()
    time.sleep(2)

# 删除_学生信息
def del_students():
    name = input('请输入要删除的学生姓名:')
    for x in student_infos:
        if name == x['name']:
            print('x',x)
            student_infos.remove(x)
            print(name,'信息已删除')

# 修改_学生信息
def edit_students():
    while True:
        name = input('请输入要修改的学生姓名(取消请输入#）:')
        if name == '#':
            break
        else:
            for x in student_infos:
                if name == x['name']:
                    while True:
                        nameState = input("请确认修改姓名(yes/no):")
                        if nameState == 'yes':
                            name = input("请修改学生姓名:")
                            x['name'] = name
                        elif name == 'no':
                            pass
                        else:
                            print("输入不正确,请重新输入:")
                            continue
                        age = int(input("请修改学生年龄:"))
                        score = int(input("请修改学生成绩:"))
                        x['age'] = age
                        x['score'] = score
                        print('修改完毕！')
                        return

# 成绩高低_学生信息
def score_gao_di():
    score_gao_di = sorted(student_infos, key = lambda x: x['score'],reverse = True)
    show_students(score_gao_di)

# 成绩低高_学生信息
def score_di_gao():
    score_di_gao = sorted(student_infos, key = lambda x: x['score'])
    show_students(score_di_gao)

# 保存_学生信息
def save_students():
    file = open(addStudentInfosFile,'wb')
    p.dump(student_infos,file)
    file.close()
    print('保存成功！')

# 打开已存_学生信息
def openSave_students():
    print('显示已存的学生信息')
    show_students(student_infos)
    # file = open(addStudentInfosFile,'rb')
    # try:
    #     all_the_text = file.read( )
    # finally:
    #     file.close( )

# 查找_学生信息
def search_students():
    name = input('请输入要查找的学生姓名:')
    width = 13
    for x in student_infos:
        if name == x['name']:
            name_info = x['name']
            age_info = str(x['age'])
            score_info = str(x['score'])
            print(x)
            _lines()
            _title()
            _lines()
            print('|%s|%s|%s|' % (name_info.center(width),
            age_info.center(width),
            score_info.center(width)))
            _lines()
            break
        else:
            print('此人不存在')
    time.sleep(2)

# =========== 自检文件是否存在  start ================
# 判断通讯录文件是否存在
addStudentInfosFile= 'addStudentInfos.txt' # data 格式 是二进制
# 如果存在，将文件读取到student_infos字典中
if os.path.exists(addStudentInfosFile):
    f= open(addStudentInfosFile,'rb')
    student_infos = p.load(f)
else:  # 如果不存在，提示并创建
    jCommand= input('未找到学生信息文件，是否创建？yes/no ')
    if jCommand == 'yes':
        # f= open(addStudentInfosFile,"r+")
        # f.writelines(student_infos)
        # f.close()
        f= open(addStudentInfosFile,'wb')
        p.dump(student_infos,f)
        f.close()
    elif jCommand == 'no':
        pass
# =========== 自检文件是否存在  end  ================


# 功能菜单选择项
while True:
    menu()
    s = input("请选择:")
    if 'q' == s:  # 'q' 退出
        break
    elif '1' == s: # 添加_学生信息
        add_student()
    elif '2' == s: # 显示_学生信息
        show_students(student_infos)
    elif '3' == s: # 删除_学生信息
        del_students()
    elif '4' == s: # 修改_学生信息
        edit_students()
    elif '5' == s: # 成绩高低_学生信息
        score_gao_di()
    elif '6' == s: # 成绩低高_学生信息
        score_di_gao()
    elif '7' == s: # 保存_学生信息
        save_students()
    elif '8' == s: # 打开已存_学生信息
        openSave_students()
    elif '9' == s: # 查找_学生信息
        search_students()
    else:
        print("输入不正确,请重新输入:")
        time.sleep(2)
