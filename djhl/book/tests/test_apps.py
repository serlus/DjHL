from djhl.book.apps import BookConfig


def test_core():
    assert BookConfig.name == "book"
