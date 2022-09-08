from mtgsdk import Card
import json

#cards = Card.where(name='Supervisor Inspirador').where(language='Portuguese (Brazil)').all()

##print(json.dumps(cards[0].__dict__))

cards = Card.where(name='"Liliana of the Veil"').all()

#print(cards[0].__dict__)

teste = cards[0].__dict__["foreign_names"]

print(cards[0].__dict__)

print()
print()
print()

for value in teste:
    if value["language"] == "Portuguese (Brazil)":
        print(value)
        print()