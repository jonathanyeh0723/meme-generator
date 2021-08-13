"""Implement a simple quote model class."""


class QuoteModel:
    """blueprint for quote."""

    def __init__(self, body: str, author: str):
        """Class initialization."""
        self.body = body
        self.author = author

    def __repr__(self):
        """To represent a class's objects as a string."""
        return f'<{self.body}, {self.author}>'
