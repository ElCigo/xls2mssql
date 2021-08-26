import pandas as pd
import pyodbc as pyodbc
import csv

# server = '10.7.1.34'
# database = 'TestKPI'
server = '10.0.0.121'
database = 'AR_B2K_CRO_PROD'

cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server}; '
                      'Server=' + server + ';'
                      'DATABASE=' + database + '; '
                      'uid=kpiTest; '
                      'pwd=Logitech2020!; '
                      'Trusted_Connection=Yes;')
cursor = cnxn.cursor()
script = '''SELECT * FROM ##masterica'''

cnxn.commit()

cursor.execute(script)



columns = [desc[0] for desc in cursor.description]
# columns = [column[0] for column in cursor.description]
# data = cursor.fetchall()
# columns = [desc[0] for desc in cursor.description]
data = cursor.fetchall()
# df = pd.DataFrame(list(data), columns=columns)
# print(data)
# columns = [column[0] for column in cursor.description]
# print(columns)
# df = pd.DataFrame(list(data), columns=columns)
df = pd.read_sql_query(script,cnxn)
# df = pd.DataFrame(script,columns=["idCilja","Exception"])
# df = pd.DataFrame({'Cigo': ["idCilja","Exception","opisCilja","nazivCilja","datCilja","idKategorije","unosDT","CreatedBy"]})
# df = pd.DataFrame({'idCilja': script(0),'Exception':[2]})

# print(df)

writer = pd.ExcelWriter('foo.xlsx')
df.to_excel(writer, sheet_name='bar')
writer.save()
# df.to_excel(writer, sheet_name='bar')
# writer.save()

# csv import
# with open('foo.csv','w') as file:
#     for row in data:
#         csv.writer(file).writerow(row)
#
# cursor.close()
# del cursor
#
# cnxn.close()


