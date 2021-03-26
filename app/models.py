from sqlalchemy import Column, Integer, Boolean

from app.database import base, session


class CompanyPaid(base):
    __tablename__ = 'company_paid'

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, unique=True)
    paid = Column(Boolean)

    def __str__(self):
        return f'Платность компании {self.company_id}'

    def __repr__(self):
        return f'Платность компании {self.company_id}'

    @classmethod
    def objects(cls):
        return session.query(cls)

    @classmethod
    def create(cls, object_create):
        session.add(object_create)
        session.commit()
        return cls.objects().filter_by(company_id=object_create.company_id)[0]

    @staticmethod
    def bulk_create(objects_create):
        session.bulk_save_objects(objects_create)
        session.commit()

    @classmethod
    def bulk_update(cls, objects_update):
        session.bulk_update_mappings(cls, objects_update)
        session.commit()
