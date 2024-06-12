from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    phone_number = db.Column(db.String(10), nullable=False)

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Author name cannot be empty")
        return name

    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        if len(phone_number) != 10:
            raise ValueError("Phone number must be exactly 10 digits")
        return phone_number

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    summary = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)

    @validates('content')
    def validate_content(self, key, content):
        if len(content) < 250:
            raise ValueError("Post content must be at least 250 characters long")
        return content

    @validates('summary')
    def validate_summary(self, key, summary):
        if len(summary) > 250:
            raise ValueError("Post summary cannot be more than 250 characters")
        return summary

    @validates('category')
    def validate_category(self, key, category):
        if category not in ["Fiction", "Non-Fiction"]:
            raise ValueError("Category must be either Fiction or Non-Fiction")
        return category

    @validates('title')
    def validate_title(self, key, title):
        clickbait_phrases = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any(phrase in title for phrase in clickbait_phrases):
            raise ValueError("Title must be sufficiently clickbait-y")
        return title
