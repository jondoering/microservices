#Baseclass for different transaction types

import datetime as dt
from marshmallow import Schema, fields

class Transaction(object):

    def __init__(self, description, amount, type):
        self.description = description
        self.amount = amount
        self.created_at = dt.datetime.now()
        self.type = type

    def __repr__(self):
        return '<Transaction(name={self.descritpion!r})>'.format(self=self)


#used to serialize and deserialise instances of Trnasaction from and to JSON objects
class TransactionSchema(Schema):
    description = fields.Str()
    amount = fields.Number()
    created_at = fields.Date()
    type = fields.Str()

