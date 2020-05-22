import csv
from datetime import datetime
import time
import re
#
# with open('amount.txt', 'r') as f:
#     reader = csv.reader(f, delimiter=',')
#     for row in reader:
#         data=row[:-1]
#         float_list = sorted([float(x) for x in data])

#03:45:47.394625
#### BURADAKI AMAC SATIR SAYINISINI BULUP VE TARIHI ESLESTIRIP EN ESKILERINI SILIP GUNCEL TEK VERIYI SAKLAMAK.
data=[]
with open('saved.txt', 'r') as f:
    a=f.readlines()
    count=len(a)-1

    regex=re.compile(r"(\d{4})-(\d\d)-(\d\d) (\d\d):(\d\d):(\d\d).(\d{6})")
    for am in a:

        c=re.findall(regex,am)
        print(c)

#####SILIYOR ANCAK BUTUN SATIRI MATCH ETMESI LAZIM
new_file = open("saved.txt", "w")
for line in a:

    if line.strip("\n") != "DATE: 2020-05-01 03:45:24.133691 --- 10.34 eur/day":
        new_file.write(line)

new_file.close()

############################################the end ############################################



# c=datetime.today()
# time.sleep(10)
#
# z=datetime.now()
# print(z)
#
# if (z > c):
#     print("okay")
#
# else:
#     print("NO")

