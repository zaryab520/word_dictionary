from app import db

class New_Word(db.Model):
    __tablename__ = 'new_words'

    id = db.Column(db.Integer, primary_key=True)
    english_word = db.Column(db.String())
    dari_translate = db.Column(db.String())
    pashto_translate = db.Column(db.String())

    def __init__(self, english_word, dari_translate, pashto_translate):
        self.english_word = english_word
        self.dari_translate = dari_translate
        self.pashto_translate= pashto_translate

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'english_word': self.english_word,
            'dari_translate': self.dari_translate,
            'pashto_translate':self.pashto_translate
        }