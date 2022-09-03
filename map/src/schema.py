import strawberry
from typing import List

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

def get_books():
    return [
        Book(
            title="吾輩は猫である",
            author="夏目漱石",
        ),
    ]

@strawberry.type
class Book:
    title: str
    author: str

@strawberry.type
class Query:
    books: List[Book] = strawberry.field(resolver=get_books)

schema = strawberry.Schema(query=Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix='/graphql')