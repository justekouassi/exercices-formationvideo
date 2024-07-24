import mysql.connector as mc

try:
    conn = mc.connect(host='localhost', database='jkwiz',
                      user='root', password='')
    cursor = conn.cursor()

    request = "SELECT * FROM francais LIMIT 10"
    cursor.execute(request)
    mission_list = cursor.fetchall()
    for mission in mission_list:
        print(mission[1])
except mc.Error as err:
    print(err)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
