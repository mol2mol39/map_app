from sqlalchemy import Column, Integer, String

from settings import Base

class Country(Base):
    """
    国コードテーブル
    """
    __tablename__ = 'countries'

    id = Column(String, primary_key=True)
    jp_name = Column(String)
    en_name = Column(String)
    numeric_code = Column(Integer)
    alpha2 = Column(String)
    area = Column(String)
    administrative_division = Column(String)

    def __repr__(self):
        return "<User(id={}, jp_name={}, en_name={}, numeric_code={}," + \
        "alpha2={}, area={}, administrative_division={})>".format(
            self.id,
            self.jp_name,
            self.en_name,
            self.numeric_code,
            self.alpha2,
            self.area,
            self.administrative_division
        )