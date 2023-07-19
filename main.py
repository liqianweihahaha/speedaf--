

import openpyxl



def readExecl():
    wb = openpyxl.load_workbook(r"D:\翻译\历史翻译表.xlsx")
    sheet = wb['Sheet1']
    rows = sheet.rows
    data_l = []
    for row in list(rows):  # 遍历每行数据
        case = []  # 用于存放一行数据
        for c in row:  # 把每行的每个单元格的值取出来，存放到case里
            case.append(c.value)

        data_l.append(case)

    return data_l


ex_datas = readExecl()

with open(r"D:\翻译\index.js", 'r', encoding='utf-8') as r:
    datas = r.readlines()
    for i in datas:

        r_v = i.replace("\n", "").replace(" ", "")
        if ":" in i:
            v_l = i.replace(" ", "").replace("\"", "").replace(",", "").replace("\n", "").split(":")
            for j in ex_datas:
                # print(v_l[1])
                # print(j[0])

                if str(v_l[1]) == str(j[0]):
                    print("========")
                    if str(j[4]) == "None":
                        r_v = v_l[0] + f": \"{j[0]}\", "
                    else:
                        r_v = v_l[0] + f": \"{j[4]}\", "

        with open(r"D:\翻译\index_bd.js", 'a', encoding='utf-8') as f:
            f.write(r_v + "\n")












