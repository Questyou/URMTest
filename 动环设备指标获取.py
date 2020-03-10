import requests
import json
import xlwt
import xlrd


workbook  = xlwt.Workbook()
rworkbook = xlrd.open_workbook('E:\env.xls')
temp = workbook.add_sheet('Temperture')
# onlytemp = workbook.add_sheet('onlytemp')
# 表第一个单元
nub00 = rworkbook.sheet_by_name('Temperture').cell(0, 0).value

res = requests.post('http://172.17.13.96:16380/envDevice/getEnvIndicatorByMonitorDeviceIds', data= {"type":"1,2"})

# print(res.status_code)

# resjson  = res.json()
resdatalist = res.json()['data']
print(resdatalist)

# 做参考
ll = list(resdatalist[0].keys())
ld = list(resdatalist[0].values())
print(ll)
print(ld)
for i in range(len(ll)):
    print(ll[i])
    print(ld[i])
    temp.write(0, i, ll[i])
    temp.write(1, i, str(ld[i]))

indicdata = resdatalist[0]['indicatorList']

# 写表头
def wtittle():
    tittlelist = list(indicdata[0].keys())
    print(tittlelist)
    for i in range(len(tittlelist)):
        temp.write(2, i, tittlelist[i])

if str(nub00) == 'name':
    print("表头写好了")
else:
    wtittle()


indicdatatil = list(indicdata[0].keys())
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

workbook.save('E:\env.xls')

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





