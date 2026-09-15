"""Starter code for the Building REST APIs with FastAPI assignment."""

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Book Catalog API")


class BookCreate(BaseModel):
    """Data required to create or replace a book."""

    title: str
    author: str
    published_year: int


books = [
    {
        "id": 1,
        "title": "The Little Prince",
        "author": "Antoine de Saint-Exupery",
        "published_year": 1943,
    },
    {
        "id": 2,
        "title": "A Wrinkle in Time",
        "author": "Madeleine L'Engle",
        "published_year": 1962,
    },
]


@app.get("/")
def read_root():
    """Return a welcome message for the API."""
    return {"message": "Welcome to the Book Catalog API"}


@app.get("/books")
def read_books():
    """Return every book in the catalog."""
    # TODO: Return the books list.
    pass


@app.post("/books", status_code=201)
def create_book(book: BookCreate):
    """Add a validated book to the catalog."""
    # TODO: Assign an id, append the book, and return the created book.
    pass


@app.get("/books/{book_id}")
def read_book(book_id: int):
    """Return one book by id."""
    # TODO: Find the book or raise an HTTPException with status 404.
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookCreate):
    """Replace an existing book."""
    # TODO: Update the book or raise an HTTPException with status 404.
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    """Delete one book by id."""
    # TODO: Delete the book or raise an HTTPException with status 404.
    pass
