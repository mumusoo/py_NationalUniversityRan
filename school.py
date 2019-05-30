#
# data.json 引用地址 https://www.forwardpathway.com/ranking
import json
import re
import uuid

import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             db='education',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
with open("data6.json", 'r') as load_f:
    load_dict = json.load(load_f)
try:
    for item in load_dict['data']:
        ranking = item[0]
        name = re.sub(r'<.*k\'>', "", item[1])
        name = re.sub(r'<.*>', "", name)
        english_name = re.sub(r'<.*k\'>', "", item[2])
        english_name = re.sub(r'<.*>', "", english_name)
        logo = item[3]
        address = re.sub(r'<.*k\'>', "", item[4])
        address = re.sub(r'<.*>', "", address)
        id = str(uuid.uuid1());
        # print(ranking)
        # print(name)
        # print(english_name)
        # print(logo)
        # print(address)
        # print(id)
        with connection.cursor() as cursor:
            sql = "INSERT INTO `t_school_dict` (`id`,`ranking`, `name`,`english_name`,`logo`,`address`,`create_date`) VALUES (%s,%s, %s,%s, %s,%s,str_to_date(%s,'%%Y-%%m-%%d %%H:%%i:%%s'))"
            cursor.execute(sql, (id, ranking, name, english_name, logo, address, "2019-04-15 00:00:00"))
        print(name)
    connection.commit()
    print("-- commit --")
finally:
    print("-- end --")
    connection.close()
