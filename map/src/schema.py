from typing import List
import strawberry
from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper, StrawberrySQLAlchemyLoader
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from src.models import country
from settings import session

strawberry_sqlalchemy_mapper = StrawberrySQLAlchemyMapper()

@strawberry_sqlalchemy_mapper.type(country.Country)
class Country:
    pass

def get_countries() -> List[Country]:
    s = session()
    countries = s.query(country.Country).all()
    return countries

@strawberry.type
class Query:
    countries: List[Country] = strawberry.field(resolver=get_countries)

# def custom_context_dependency():
#     return StrawberrySQLAlchemyLoader(bind=session())


# async def get_context(
#     custom_value=Depends(custom_context_dependency),
# ):
#     return {
#         "custom_value": custom_value,
#     }

strawberry_sqlalchemy_mapper.finalize()
additional_types = list(strawberry_sqlalchemy_mapper.mapped_types.values())

schema = strawberry.Schema(query=Query, types=additional_types)

graphql_app = GraphQLRouter(schema)#, context_getter=get_context,)

app = FastAPI()

# origins = [
#     "http://localhost:3000"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(graphql_app, prefix='/graphql')
