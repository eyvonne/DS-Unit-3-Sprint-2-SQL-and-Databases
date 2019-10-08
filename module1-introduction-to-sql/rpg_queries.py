import pandas as pd
import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')

# how many total characters are there?
curs = conn.cursor()
total = curs.execute('select count(1) from charactercreator_character;'
                     ).fetchone()[0]
print('There are ' + str(total) + ' characters')

# how many of each specific subclass
query = 'select count(1) from charactercreator_'
classes = ['cleric', 'fighter', 'mage', 'necromancer', 'thief']

for clas in classes:
    count = curs.execute(query+clas+';').fetchone()[0]
    print('There are '+str(count)+' '+clas+'s')

# how many total items?
totalitem = curs.execute('select count(1) from armory_item;').fetchone()[0]
print('There are '+str(totalitem)+' items')

# how many weapons/not Weapons
totalweapon = curs.execute('select count(1) from armory_weapon;').fetchone()[0]
print('There are '+str(totalweapon)+' weapons')

print('There are '+str(totalitem-totalweapon)+' non-weapon items')

# how many items does each character have (return first 20 rows)
print('the first twenty characters item counts')
print(curs.execute('''SELECT COUNT(character_id)
                    FROM charactercreator_character_inventory
                    Group by character_id
                    limit 20;''').fetchall())

# how many weapons does each character have (return first 20 rows)
print('the first twenty characters weapons counts')
print(curs.execute('''select count(character_id)
                    from charactercreator_character_inventory
                    inner join armory_weapon
                    on item_ptr_id=item_id
                    Group by character_id
                    limit 20;''').fetchall())

# on average how many items does each character have
print('average Items per character')
print(curs.execute('''SELECT
                     cast(COUNT(charactercreator_character_inventory.item_id) as float)/
                    COUNT(DISTINCT character_id)
                    FROM charactercreator_character_inventory
                    INNER JOIN armory_item
                    ON armory_item.item_id = charactercreator_character_inventory.item_id;
                    ''').fetchall())

# and how many Weapons
print('average weapons per character')
print(curs.execute('''SELECT
                    cast(COUNT(charactercreator_character_inventory.item_id) as float)/
                    COUNT(DISTINCT character_id)
                    FROM charactercreator_character_inventory
                    INNER JOIN armory_weapon
                    ON item_ptr_id = charactercreator_character_inventory.item_id;
                    ''').fetchall())

curs.close()
conn.commit()

"""part 2"""
print(' \n \n part two: \n \n ')

df = pd.read_csv('buddymove_holidayiq.csv')
df = df.rename({'User Id': 'user_id'}, axis=1)
conn2 = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql('buddymove_holidayiq', conn2, index_label='id')
curs2 = conn2.cursor()

# how many rows are There
rows = curs2.execute('select count(id) from buddymove_holidayiq').fetchone()[0]
print('there are', rows, 'rows')

# how many people reviewed over one hundred in nature and shopping?
natureshop = curs2.execute('''select count(user_id) from buddymove_holidayiq
                            where Shopping>99 and Nature>99''').fetchone()[0]
print(natureshop, 'people rated both nature and shopping at least 100')

# whats the average number of reviews in each
cats = ['Sports', 'Religious', 'Nature', 'Theatre', 'Shopping', 'Picnic']
for cat in cats:
    avg = curs2.execute('select avg('+cat+')from buddymove_holidayiq').fetchone()[0]
    print('The average number of reviews in', cat, 'is', avg)
