
def ramdomnum(second):
    if second == '0' :
        i = 0
    elif second == '1' :
        i = -2
    while i < 5 :
        randomnumber = random.randint(1,nrows)       #生成随机数
        name = table.cell_value(randomnumber,0)      #获取随机数对应用户名名称
        uid = int(table.cell_value(randomnumber,1))  #获取随机数对应用户UID
        uids.append(uid)
        if uids.count(uid) > 1 :        #判断是否重复抽取同一人并排除
            continue
        elif i == -2 :
            print()
            print()
            print('              用户名: ',name,'  UID: ',uid)
            print()
            print()
            return 0
        else:
            if i != 0 :
                input('按下 Enter 以显示下一数据...')
            print()
            print()
            print('              用户名: ',name,'  UID: ',uid)
            print()
            print()
        i = i+1

def main():
    print("正在抽取...")
    ramdomnum('0')
    ask = 'n'
    while ask != 'y' :
        ask = input('是否需要下一数据?(y/n):')
        if ask == 'n' :
            break
        elif ask == 'y' :
            ramdomnum('1')
            ask = ' '
    input ('按下 Enter 以退出程序...')

if __name__ == '__main__':
    uids = []
    import random
    import xlrd
    import tkinter as tk
    from tkinter import filedialog
    '''打开选择文件夹对话框'''
    root = tk.Tk()
    root.withdraw()
    file = filedialog.askopenfilename(filetypes=[('Excel XLS 文件', '.xls')],title = '选择 .xls 文件') 
    print('正在读取文件:',file)
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]        #获取 Sheet 名称
    nrows = table.nrows - 1         #获取数据总量
    main()