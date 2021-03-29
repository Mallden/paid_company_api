from typing import Optional

from fastapi import FastAPI

from app.database import session, base
from app.models import CompanyPaid
from app.settings import engine

app = FastAPI()


@app.get("/")
def read_root():
    return {"Welcome": "PaidAPI"}


@app.get("/items/{item_id}/")
async def read_item(item_id: int):
    company_info_paid = CompanyPaid.objects().filter_by(company_id=item_id)
    return company_info_paid[0]


@app.put("/items/")
async def update_items(items: dict):
    info_companies = CompanyPaid.objects().filter(CompanyPaid.company_id.in_(items.keys()))
    update_list = list()

    for info in info_companies:
        object_paid = info.__dict__
        object_paid.pop('_sa_instance_state')
        object_paid['paid'] = items[str(object_paid['company_id'])]
        update_list.append(object_paid)

    CompanyPaid.bulk_update(update_list)
    return {"result": "ok"}


@app.put("/items/{item_id}/")
async def update_item(item_id: int, info: bool):
    info_company = CompanyPaid.objects().filter_by(company_id=item_id).first()
    info_company.paid = info
    session.commit()
    return {"result": "ok"}


@app.post("/items/")
async def added_items(items: dict):
    added_list = list()
    for key in items:
        added_list.append(CompanyPaid(company_id=key, paid=items[key]))
    CompanyPaid.bulk_create(added_list)
    return {"result": "ok"}
