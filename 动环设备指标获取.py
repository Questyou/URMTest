import requests
import json
import xlwt
import xlrd


workbook  = xlwt.Workbook()
rworkbook = xlrd.open_workbook('E:\env.xls')

wworkbook = workbook.add_sheet('Temperture', cell_overwrite_ok=True)
# 表第一个单元
# 请求指标
def getData():
    envurl = 'http://172.17.13.96:16380/envDevice/getEnvIndicatorByMonitorDeviceIds'
    res = requests.post(envurl, data= {"type":"1,2"})
    resdatalist = res.json()['data']
    print(resdatalist)
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
    whitchtype(valueslist)
    # d = [ ]
    i = line
    j = 0
    for x in range(len(envvalueslist)):
        envvalueslistdict = envvalueslist[x]
        # whitchtype(envvalueslistdict)
        envvalueslistdict.items()
        # whitchtype(envvalueslistdict.items())
        # print(len(envvalueslistdict.items()))
        for key, value  in envvalueslistdict.items():
            wworkbook.write(i, j , key)
            wworkbook.write(i, j+1 , value)
            # print(key)
            # print(value)
            j += 2
        j += 1


        # namelist = envvalueslist.keys()
        # d[x] = str(decoded_json['name'])


envdata = getData()
# envname = getEnvName(envdata, 0)
# print(envname)

for i in range(len(envdata)):
    wenvname = getEnvName(envdata , i)

    envvalueslist = getEnvValuesList(envdata , i)
    getEnvvalues(envvalueslist , i)
    print(envvalueslist)

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





