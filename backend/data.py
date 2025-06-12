
# backend/data.py
from models import db, Product, Category
from faker import Faker
import random

fake = Faker()

def generate_mock_data():
    # Create categories
    categories = ['Electronics', 'Books', 'Clothing', 'Home & Kitchen', 'Toys']
    for cat_name in categories:
        if not Category.query.filter_by(name=cat_name).first():
            db.session.add(Category(name=cat_name))
    db.session.commit()

    # Create products
    categories = Category.query.all()
    for _ in range(100):
        product = Product(
            name=fake.sentence(nb_words=3),
            description=fake.paragraph(nb_sentences=3),
            price=round(random.uniform(10, 1000), 2),
            image_url=f'https://picsum.photos/400/300?random={_}',
            stock=random.randint(0, 100),
            category_id=random.choice(categories).id
        )
        db.session.add(product)
    db.session.commit()