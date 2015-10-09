
import StringIO
import xlwt

from xlutils.copy import copy # http://pypi.python.org/pypi/xlutils
from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd
from xlwt import easyxf # http://pypi.python.org/pypi/xlwt


def genXls(rows):

    ##################################
    # Code for creating Excel data and
    # inserting into Flask response
    ##################################
    workbook = xlwt.Workbook()
    ws = workbook.add_sheet('A Test Sheet')

    i = 1
    ws.write(0, 0, "id")
    ws.write(0, 1, "data")
    
    for item in rows:
   
    	ws.write(i, 0, item['id'])
    	ws.write(i, 1, item['data'])
    	i = i +1
    
    #.... code here for adding worksheets and cells

    output = StringIO.StringIO()
    workbook.save(output)

    return output


def useTemplate(rows):


    id_ROW = 6 # 0 based (subtract 1 from excel row number)
    col_name = 1
    col_description = 2
    col_avalaible = 3
    
    rb = open_workbook('./Book.xls',formatting_info=True)

    r_sheet = rb.sheet_by_index(0) # read only copy to introspect the file
    wb = copy(rb) # a writable copy (I can't read values out of this, only write to it)
    w_sheet = wb.get_sheet(0) # the sheet to write to within the writable copy


    for row in rows:
      
        w_sheet.write(id_ROW, col_name, row['name'])
        w_sheet.write(id_ROW, col_description, row['description'])
        w_sheet.write(id_ROW, col_avalaible, row['available'])
        id_ROW = id_ROW + 1

    output = StringIO.StringIO()
    wb.save(output)

    return output
