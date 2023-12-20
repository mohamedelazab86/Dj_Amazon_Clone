import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from faker import Faker
import random
from products.models import Product,Brand

def seed_brand(n):
    fake=Faker()
    images=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg',]
    for _ in range(n):
        Brand.objects.create(
            name=fake.name(),
            image=f'photo_brand/{images[random.randint(0,8)]}'

        )
def seed_product(n):
    fake=Faker()
    flag_tupe=['New','Sale','Feature']
    brand=Brand.objects.all()
    images=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg',]
    
    for _ in range(n):
        Product.objects.create(
            name=fake.name(),
            flag=flag_tupe[random.randint(0,2)],
            price=round(random.uniform(5.99,99.99),2),
            image=f'photo_image{images[random.randint(0,8)]}',
            sku=random.randint(100,10000000),
            subtitle=fake.text(max_nb_chars=4000),
            description=fake.text(max_nb_chars=40000),
            brand=brand[random.randint(0,len(brand)-1)]

        )
#seed_brand(155)
seed_product(1200)
