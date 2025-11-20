'''To read excel_files, we use xlrd

To install xlrd
    Go to command prompt    -->     pip install xlrd==1.2.0

    STEP1   :   import xlrd
    STEP2   :   open the excel file
    STEP3   :   open the worksheet
    STEP4   :   Convert the sheet object to the generator object

'''

import xlrd

## open the excel_file
path = (r'C:\Users\Jiya Abbot\OneDrive\Desktop\M40\detalis_all.xlsx')
workbook = xlrd.open_workbook(path)
# print(workbook)                 ## Book object

## open the worksheet
worksheet = workbook.sheet_by_name('personal_data')
# print(worksheet)                ## Sheet object

## Convert the sheet object to the generator object
rows = worksheet.get_rows()
print(rows)                ## generator object

##---------------------------------------------------------------------------------------
# for ele in rows:
#     print(ele)
#
# ## ## text:'name', text:'place' , text:'email_id' , text:'phone_number'
# # ## text:'chetna' , text:'Hyderabad' , text:'chetna@gmail.com', number:9080706050.0
# # ## text:'manju' , text:'jammu' , text:'manju@gmail.com' , number:9181716151.0
# # ## text:'jiya' , text:'delhi , text:'jiya@gmail,com' , number:9282726252.0
# # ## text:'navneet' , text:'Mumbai' , text:'nav@gmail.com' , number:9383736353.0
# # ## text:
##---------------------------------------------------------------------------------------
# for ele in rows:
#     print(ele[0], ele[1], ele[2], ele[3])

# ## text:'name' text:'place' text:'email_id' text:'phone_number'
# ## text:'chetna' text:'Hyderabad' text:'chetna@gmail.com' number:9080706050.0
# ## text:'manju' text:'jammu' text:'manju@gmail.com' number:9181716151.0
# ## text:'jiya' text:'delhi text:'jiya@gmail,com' number:9282726252.0
# ## text:'navneet' text:'Mumbai' text:'nav@gmail.com' number:9383736353.0
# ## text:

##---------------------------------------------------------------------------------------
# for ele in rows:
#     print(ele[0].value, ele[1].value, ele[2].value, ele[3].value)

## name place email_id phone_number
#chetna Haryana chetna@gmail.com 978478874777.0
#manju jammu manju@gmail.com 9187745757951.0
#Jiya delhi jiya@gmail,com 978867933252].0
#himani Mumbai haimani@gmail.com 9383736353.0
#Navneet Himachal nav@gmail.com 9832346545.0