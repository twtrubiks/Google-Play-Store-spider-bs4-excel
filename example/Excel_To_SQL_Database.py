import pyexcel as pe
from example.dbModel import *

if __name__ == '__main__':

    records = pe.iget_records(file_name="university.xlsx")
    for record in records:
        insert_data = University(
            County=record['縣市'],
            University=record['學校']
        )
        db.session.add(insert_data)
    db.session.commit()
    print("Excel TO SQL Database DONE")
