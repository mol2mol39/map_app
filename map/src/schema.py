from typing import List
import strawberry

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter


book_data = [{
    "title": "我輩は猫である",
    "author": "夏目漱石"
}, {
    "title": "test",
    "author": "test"
}]


def get_author_for_book(root) -> "Author":
    name = ''
    for book in book_data:
        if root.title == book['title']:
            name = book['author']
    return Author(name=name)


@strawberry.type
class Book:
    title: str
    author: "Author" = strawberry.field(resolver=get_author_for_book)


def get_books_for_author(root):
    books = [Book(title=book['title']) for book in book_data
             if root.name == book['author']]
    return books


@strawberry.type
class Author:
    name: str
    books: List['Book'] = strawberry.field(resolver=get_books_for_author)


def get_authors() -> List[Author]:
    authors = [Author(name=book['author']) for book in book_data]
    return authors


def get_books(root):
    books = [Book(title=book['title']) for book in book_data]
    return books


@strawberry.type
class Query:
    authors: List[Author] = strawberry.field(resolver=get_authors)
    books: List[Book] = strawberry.field(resolver=get_books)


@strawberry.input
class AddBookInput:
    title: str = strawberry.field(description="The title of the book")
    author: str = strawberry.field(description="The name if the auther")


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, book: AddBookInput) -> Book:
        book_data.append({"title": book.title, "author": book.author})
        return Book(title=book.title)


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)

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
