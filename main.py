import os
import json

clear = lambda: os.system('cls')

def select_exam():

    print("""====== 欢迎来到Project Sekai段位考试 ======""")
    print()
    print("请选择考试：")

    exams = os.listdir('exams')

    exams = [exam for exam in exams if '.json' in exam]

    try:
        for index, exam in enumerate(exams):

            print(f"{index + 1}: {json.load(open(str('exams/' + exam), encoding='utf-8'))['name']}")
    except:
        
        print()
        print("【错误】 读取段位考试时出现问题，请确保exams文件夹中所有文件格式合法")

        exit()

    print()
    print("输入选项对应的数字并回车：", end='')

    choice = int(input())
    path = "exams/" + exams[choice - 1]

    exec_exam(open(path, encoding='utf-8'))

def exec_exam(cfg_file):

    clear()
    
    cfg = json.loads(cfg_file.read())

    print(cfg["name"])
    print(cfg['description'])
    print()
    print(cfg["rule"])
    print()

    print("请选择等级：")

    counter = 0

    level_list = {}

    for level in cfg["levels"]:

        counter = counter + 1
        level_list.update({counter: level})
        print(counter, ". ", level, sep='')

    print()
    print("输入选项对应的数字并回车：", end='')

    choice = int(input())
    choice = choice

    if (type(choice) != int):

        print("【错误】 请输入一个数字代表选项！")
        input()
        return

    if (choice < 1 or choice > counter):

        print("【错误】 请输入一个有效的选项！")
        input()
        return

    level = cfg["levels"][level_list.get(choice)]

    print("现在开始段位考试:", level_list.get(choice))
    
    life = level['life']

    great = []
    good = []
    bad = []
    miss = []
    life_archive = []

    for index, track in enumerate(level["tracks"]):

        print(f"曲目 {index + 1} : {track}")
        print()

        print("请输入Great数：", end='')
        great.append(int(input()))

        print("请输入Good数：", end='')
        good.append(int(input()))

        print("请输入Bad数：", end='')
        bad.append(int(input()) )

        print("请输入Miss数：", end='')
        miss.append(int(input()))

        print()

        life = life - great[index] * level['penalty'][0] - good[index] * level['penalty'][1] - bad[index] * level['penalty'][2] - miss[index] * level['penalty'][3]

        if (life <= 0):

            print("挑战失败！剩余生命值：", life, sep = '')
            input()
            return

        life = life + level['heal']

        if (life > level['life']):

            life = level['life']

        print("剩余生命值：", life, sep = '')
        print()

        life_archive.append(life)

    clear()

    print("恭喜你！挑战成功！")
    print()
    print("考试明细：")

    for index, track in enumerate(level["tracks"]):

        print(f"曲目 {index + 1} : {track}")
        print(f"Great: {great[index]} Good: {good[index]} Bad: {bad[index]} Miss: {miss[index]} 剩余生命值：{life_archive[index]}")

        if (good[index] + bad[index] + miss[index] == 0):

            if (great[index] == 0):

                print("ALL PERFECT!!")

            else:

                print("FULL COMBO!!")

        print()
  

    input()


if (__name__ == "__main__"):

    while (True):

        clear()

        select_exam()