from Entity import *


class GooglePlay(db.Model):
    __tablename__ = 'GooglePlay'

    def __init__(self
                 , App
                 , Link
                 , Autor
                 , Rate
                 , Download
                 , Publish
                 , Item
                 ):
        self.App = App
        self.Link = Link
        self.Autor = Autor
        self.Rate = Rate
        self.Download = Download
        self.Publish = Publish
        self.Item = Item
