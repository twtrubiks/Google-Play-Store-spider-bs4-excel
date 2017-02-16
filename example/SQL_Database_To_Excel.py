from pyexcel_xlsx import save_data
from collections import OrderedDict
from example.dbModel import *

if __name__ == '__main__':
    db_data = University.query.all()
    first_row = [["ID", "縣市", "學校"]]
    for index, data in enumerate(db_data, start=1):
        County = data.County
        University = data.University
        first_row.append([index, County, University])

    dic = OrderedDict()

    dic.update({"Sheet 1": first_row})
    save_data("Excel-data.xlsx", dic)
    print('SQL Database TO Excel DONE')
