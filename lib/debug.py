#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

# Setup database connection
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    # Fetching seeded data
    amazon = session.query(Company).filter_by(name='Amazon').first()
    google = session.query(Company).filter_by(name='Google').first()

    gloria = session.query(Dev).filter_by(name='Gloria').first()
    lucky = session.query(Dev).filter_by(name='lucky').first()

    #Initial Overview
    print("=== INITIAL DATA ===")
    print(f"Companies: {amazon.name}, {google.name}")
    print(f"Developers: {gloria.name}, {lucky.name}")
    print()

    #indicates available Freebies
    print("=== EXISTING FREEBIES ===")
    for f in session.query(Freebie).all():
        print(f"{f.item_name} (${f.value}) - Dev: {f.dev.name}, Company: {f.company.name}")
    print()

    #Dev & Freebie 
    print("=== DEVELOPER FREEBIES ===")
    print(f"{gloria.name}'s freebies: {[f.item_name for f in gloria.freebies]}")
    print(f"{lucky.name}'s freebies: {[f.item_name for f in lucky.freebies]}")
    print()

    #Company & Freebie 
    print("=== COMPANY FREEBIES ===")
    print(f"{google.name}'s freebies: {[f.item_name for f in google.freebies]}")
    print(f"{amazon.name}'s freebies: {[f.item_name for f in amazon.freebies]}")
    print()

    #Company & Devs
    print("=== COMPANY DEVELOPERS ===")
    print(f"{google.name}'s devs: {[dev.name for dev in google.devs]}")
    print(f"{amazon.name}'s devs: {[dev.name for dev in amazon.devs]}")
    print()

    # Dev - Companies - Freebies
    print("=== DEVELOPER COMPANIES ===")
    print(f"{gloria.name}'s companies: {[c.name for c in gloria.companies]}")
    print(f"{lucky.name}'s companies: {[c.name for c in lucky.companies]}")
    print()

    #Test for give_freebie
    print("=== GIVE FREEBIE ===")
    google.give_freebie(session, gloria, "Tote Bag", 12)
    amazon.give_freebie(session, lucky, "Hat", 10)
    session.commit()

    for f in session.query(Freebie).all():
        print(f"{f.item_name} - Dev: {f.dev.name}, Company: {f.company.name}")
    print()

    # Testing the oldest_company
    print("=== OLDEST COMPANY ===")
    oldest = Company.oldest_company(session)
    print(f"Oldest: {oldest.name} ({oldest.founding_year})")
    print()

    # Testing the received_one
    print("=== RECEIVED CHECK ===")
    print(f"Gloria has Mug? {gloria.received_one('Mug')}")
    print(f"Gloria has Tote Bag? {gloria.received_one('Tote Bag')}")
    print(f"Lucky has Hat? {lucky.received_one('Hat')}")
    print()

    # Testing the give_away
    print("=== GIVE AWAY ===")
    tote_bag = session.query(Freebie).filter_by(item_name='Tote Bag').first()
    print(f"Before: {tote_bag.item_name} - Owner: {tote_bag.dev.name}")
    gloria.give_away(session, lucky, tote_bag)
    session.refresh(tote_bag)
    print(f"After: {tote_bag.item_name} - Owner: {tote_bag.dev.name}")
    print()

    session.close()
