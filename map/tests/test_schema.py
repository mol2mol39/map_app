import pytest

import src.schema as schema

def test_query_authors():
    query = """
        query {
            authors {
                name
            }
        }
    """
    result = schema.schema.execute_sync(query)
    assert result.errors is None
    assert result.data["authors"] == [
        {"name": "夏目漱石"},
        {"name": "test"}
    ]

def test_query_books():
    query = """
        query {
            books {
                title
                author {
                    name
                }
            }
        }
    """
    result = schema.schema.execute_sync(query)
    assert result.errors is None
    assert result.data["books"] == [
        {
            "title": "我輩は猫である",
            "author": {"name": "夏目漱石"}
        },
        {
            "title": "test",
            "author": {"name": "test"}
        }
    ]
