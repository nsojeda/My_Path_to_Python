hr = ('\n\n*******************************')

print(hr)
print('*                             *')
print('*          Welcome            *')
print('*   to my D&D Mad Lib story   *')
print('*                             *')
print(hr)

print('''\n"Welcome, adventurers! Gather round the fire. 
\nBefore we begin our quest, I require a toll of words from each of you. 
Speak quickly, and do not look at the parchment! 
Give me adjectives, nouns, verbs, and places—any words will do! 
Once I have your treasures, I shall weave them into the tale of your destiny.
\nSo, what say you? Do you accept the challenge?"''')

adjective = input('\nPlease give me an adjective:\n')
noun = input('\nPlease give me a noun:\n')
place_name = input('\nPlease give me a place name:\n')
character_name = input('\nPlease give me a character name:\n')
character_class = input('\nPlease give me a character class:\n')
creature = input('\nPlease give me a creature:\n')
villain_name = input('\nPlease give me a villain name:\n')
magical_item = input('\nPlease give me a magical item:\n')
weapon = input('\nPlease give me a weapon:\n')
animal = input('\nPlease give me an animal:\n')
silly_name = input('\nPlease give me a silly name:\n')
plural_noun = input('\nPlease give me a plural noun:\n')
building = input('\nPlease give me a building:\n')
occupation = input('\nPlease give me an occupation:\n')
food = input('\nPlease give me a food:\n')
object = input('\nPlease give me an object:\n')
liquid = input('\nPlease give me a liquid:\n')
exclamation = input('\nPlease give me an exclamation:\n')
magical_item = input('\nPlease give me a magical item:\n')

print(f'''The Quest of the ___{adjective}___ ___{noun}___

It all began in the village of ___{place_name}___, where our hero,
___{character_name}___, a brave ___{character_class}___,
received a scroll from a mysterious ___{creature}___.

The scroll read: "Beware! The evil ___{villain_name}___ has stolen
the legendary ___{magical_item}___! Without it, our land will fall
into eternal ___{noun}___!"

Without hesitation, our hero grabbed their trusty ___{weapon}___ and
set off toward the ___{adjective}___ Mountains. Along the way, they
befriended a talking ___{animal}___ named ___{silly_name}___, who
offered to guide them through the Forest of ___{plural_noun}___.

Deep in the woods, they stumbled upon a cursed ___{building}___,
where a grumpy ___{occupation}___ guarded the only bridge. 

"You may pass," he growled, 
"Only if you solve my riddle about ___{food}___!"

After cracking the riddle (barely!), they reached the villain's lair —
a giant ___{object}___ floating above a pit of boiling ___{liquid}___.
The final battle was fierce! Our hero swung their ___{weapon}___
while the villain cast a spell that turned everyone into ___{plural_noun}___.

But with a mighty shout of "___{exclamation}___!", our hero broke the
curse, snatched back the ___{magical_item}___, and defeated the
___{villain_name}___ once and for all.

The kingdom threw a grand feast in their honor, where they ate ___{food}___
until they couldn't move. And as the bard sang songs of their ___{adjective}___
deeds, our hero smiled, already dreaming of the next adventure...

THE END''')
