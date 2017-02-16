from pyexcel_xlsx import save_data
from collections import OrderedDict
from dbModel import *

if __name__ == '__main__':
    db_data = GooglePlay.query.all()
    first_row = [["ID", "App", "Link", "Autor", "Rate", "Download", "Publish", "Item"]]
    for data in db_data:
        Id = data.Id
        App = data.App
        Link = data.Link
        Autor = data.Autor
        Rate = data.Rate
        Download = data.Download
        Publish = data.Publish
        Item = data.Item
        first_row.append([Id, App, Link, Autor, Rate, Download, Publish, Item])

    dic = OrderedDict()

    dic.update({"Sheet 1": first_row})
    save_data("Excel-data.xlsx", dic)
    print('SQL Database TO Excel DONE')
