# # '''
# #
# #    Workbook()  --> creates a new excel_workbook
# #   .active     --> gets the current sheet
# #
# # ''
#
# from openpyxl import Workbook
#
# # open the new excel_workbook
# excel_workbook = Workbook()
#
# ## initialize the worksheet
# worksheet = excel_workbook.active
#
# ## set the title for the worksheet(optional)
# worksheet.title = 'personal_data'
#
# ## Add the data to the excel_file
# worksheet['A1'] = 'Name'
# worksheet['B1'] = 'Place'
# worksheet['C1'] = 'Email_id'
# worksheet['D1'] = 'Phone_number'
#
# data_list = [
#     ['chetna', 'Haryana', 'chetna@gmail.com', 978478874777],
#     ['manju', 'jammu', 'manju@gmail.com', 9187745757951],
#     ['Jiya', 'delhi', 'jiya@gmail,com', 978867933252],
#     ['himani', 'Mumbai', 'haimani@gmail.com', 9383736353],
#     ['Navneet','Himachal','nav@gmail.com',9832346545]
# ]
#
# for data in data_list:
#     worksheet.append(data)
#
# # excel_workbook.save('e19_data.xlsx')    ## The file will be stored in the same location as our python file
#
# ## To store the data in some other location
# excel_workbook.save(r'C:\Users\Jiya Abbot\OneDrive\Desktop\M40\detalis_all.xlsx')
#
#
