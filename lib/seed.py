from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Dev, Company, Freebie

# Connection to the SQLite database
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# removes prev data b4 seeding
session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()

# Creating some companies
google = Company(name="Google", founding_year=1998)
microsoft = Company(name="Microsoft", founding_year=1975)
amazon = Company(name="Amazon", founding_year=1994)
netflix = Company(name="Netflix", founding_year=1997)

# Creating the devs
lucky= Dev(name="lucky")
gloria = Dev(name="Gloria")
elijah = Dev(name="Elijah")
naima = Dev(name="Naima")
alex = Dev(name="Alex")

# Creating the freebies
f1 = Freebie(item_name="T-shirt", value=10, company=google, dev=lucky)
f2 = Freebie(item_name="Sticker Pack", value=3, company=google, dev=gloria)
f3 = Freebie(item_name="Water Bottle", value=8, company=amazon, dev=lucky)
f4 = Freebie(item_name="Hoodie", value=20, company=microsoft, dev=elijah)
f5 = Freebie(item_name="USB Drive", value=5, company=netflix, dev=naima)
f6 = Freebie(item_name="Backpack", value=25, company=google, dev=alex)
f7 = Freebie(item_name="Mug", value=6, company=amazon, dev=gloria)
f8 = Freebie(item_name="Notebook", value=4, company=microsoft, dev=naima)
f9 = Freebie(item_name="Phone Stand", value=7, company=netflix, dev=elijah)
f10 = Freebie(item_name="Laptop Sticker", value=2, company=google, dev=lucky)

# Add and commit all data
session.add_all([
    google, microsoft, amazon, netflix,
    lucky, gloria, elijah, naima, alex,
    f1, f2, f3, f4, f5, f6, f7, f8, f9, f10
])
session.commit()

print("Database seeded successifully!")

