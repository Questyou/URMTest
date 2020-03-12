import requests
import json
import xlwt
import xlrd


workbook  = xlwt.Workbook()
rworkbook = xlrd.open_workbook('E:\env.xls')

wworkbook = workbook.add_sheet('Temperture', cell_overwrite_ok=True)
# 表第一个单元
# 请求指标
urlList = [' http://172.17.13.96:16380/envDevice/getEnvIndicatorByMonitorDeviceIds', ' http://172.17.13.92:16380/envDevice/getEnvIndicatorByMonitorDeviceIds']

ListNotNull = True


def getData(urlnum):
    envurl = urlList[urlnum]
    print('请求第次', str(urlnum))
    res = requests.post(envurl, data={"type": "1,2"})
    resdatalist = res.json()['data']
    # print(resdatalist)
    return resdatalist

def getEnvName(datalist, x):
    envname = datalist[x]['name']
    # print(envname)
    return envname

def getEnvValuesList(valeslist , x ):
    envvaluesList = valeslist[x]['indicatorList']
    # listornot = type(envvaluesList)
    # print(listornot)
    return envvaluesList

def whitchtype(data):
    datawhitchtype = data
    print(datawhitchtype)
    whitchtype = type(datawhitchtype)
    print(whitchtype)

def getEnvvalues(valueslist, line):
    # whitchtype(valueslist)
    # d = [ ]
    i = line +1
    j = 1
    for x in range(len(envvalueslist)):
        envvalueslistdict = envvalueslist[x]
        envvalueslistdict.items()
        for key, value  in envvalueslistdict.items():
            # wworkbook.write(i, j , key)
            writeToExcel(key,i, j)
            writeToExcel(value, i, j+1)
            # wworkbook.write(i, j+1 , value)
            # print(key)
            # print(value)
            j += 2
        j += 1

def writeToExcel(obj, row ,col):
    wworkbook.write(row, col, obj)

lisrnum = 0
# envdata = getData(lisrnum)
envdata = getData(lisrnum)

while ListNotNull:
    # list是空的问题先不考虑
    flag = 0
    for i in range(len(envdata)):
        envData = envdata
        wenvname = getEnvName(envData, i)
        writeToExcel(wenvname , 0 , 0)
        envvalueslist = getEnvValuesList(envData, i)
        print(envvalueslist)
        getEnvvalues(envvalueslist, i)
        flag += 1
        if flag == int(len(envvalueslist)):
            print('envvalueslist取完了')
    lisrnum += 1
    if i == int(len(envdata) - 1):
        print('循环完了')
        ListNotNull = False
    else:
        ListNotNull = True


workbook.save(r'E:\env.xls')




# # 做参考
# ll = list(resdatalist[0].keys())
# ld = list(resdatalist[0].values())
# print(ll)
# print(ld)
# for i in range(len(ll)):
#     print(ll[i])
#     print(ld[i])
#     temp.write(0, i, ll[i])
#     temp.write(1, i, str(ld[i]))
#
# indicdata = resdatalist[0]['indicatorList']
#
# nub00 = str(rworkbook.sheet_by_name('Temperture').cell(rworkbook, 0, 0).value)
# print(nub00)
# # 写表头
# def wtittle():
#     tittlelist = list(indicdata[0].keys())
#     print(tittlelist)
#     for i in range(len(tittlelist)):
#         temp.write(2, i, tittlelist[i])
#
# if nub00 == 'name':
#     print("表头写好了")
# else:
#     wtittle()


# indicdatatil = list(indicdata[0].keys())
#
# for i in range(len(indicdata)):
#     devname = indicdata[i]['name']
#     devvalue = indicdata[i]['value']
#     devtype = indicdata[i]['type']
#     devalarm = indicdata[i]['alarm']
#     titlevalue = [devname, devvalue, devtype, devalarm]
#     # onlytemp.write(0 , i , indicdatatil[i])
#     for j in range(len(indicdatatil)):
#         temp.write(j , {i + 1} , indicdatatil[i])
#     print(devname)



    # temp.write(1, i, int(ld['id']))
# print(ll[0])



# resdataindicatoerlist = resdatalist[0]['indicatorList']
# zhibiao = len(resdataindicatoerlist)
# print(zhibiao)


#
#
# for x in range(len(resdataindicatoerlist)):
#     print(str(resdataindicatoerlist[x]))
#     data = str(resdataindicatoerlist[x])
#     indicname = data['name']
#     indicvla = data['value']
#
#     x += 1



# print(nevname)





