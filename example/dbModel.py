from Entity import *


class University(db.Model):
    __tablename__ = 'University'

    def __init__(self
                 , County
                 , University
                 ):
        self.County = County
        self.University = University
