# Task 1.1
from itertools import combinations as com 
Kevin = {"Halsey", "Taylor Swift", "Mitski", "Joji", "Shawn Mendes", "Sabrina Carpenter", "Nicky Minaj ", "Conan Gray", "One Direction", "Justin Bieber"}

Stuart = {"Kendrick Lamar", "Steve Lacy", "Tyler the Creator", "Joji", "TheWeeknd", "Coldplay", "Kanye West", "Travis Scott", "Frank Ocean", "Brent Faiyaz"}

Bob = {"Conan Gray", "Joji", "Dove Cameron", "Mitski", "Arctic Monkeys", "Steve Lacy", "Kendrick Lamar", "Isabel LaRosa", "Shawn Mendes","Coldplay", "Lauv"}

Edith = {"Metallica", "Billie Eilish", "TheWeeknd" "Mitski", "NF", "Conan Gray", "Kendrick Lamar", "Nicky Minaj", "Kanye West", "Coldplay"}

l = [Kevin, Stuart, Bob, Edith]
lMap = ['Kevin', 'Stuart', 'Bob', 'Edith']
DJ_Dict = {}

#Without itertools
# for i in range(len(l)):
#     for j in range(i+1, len(l)):
#         if(len(l[i].intersection(l[j]))) >= 3:
#             print(f"{lMap[i]} and {lMap[j]} share at least 30 percent of their respective artists.\n")
#             DJ_Dict.update({f'{lMap[i]} and {lMap[j]}': len(l[i].intersection(l[j])) })
# print(DJ_Dict)

# maxDJ = max(zip(DJ_Dict.values(), DJ_Dict.keys()))[1]
# print(maxDJ)
#Output
# Kevin and Bob share at least 30 percent of their respective artists.

# Stuart and Bob share at least 30 percent of their respective artists.

# Stuart and Edith share at least 30 percent of their respective artists.

# Bob and Edith share at least 30 percent of their respective artists.

# {'Kevin and Bob': 4, 'Stuart and Bob': 4, 'Stuart and Edith': 3, 'Bob and Edith': 3}
# Stuart and Bob

# With itertools
pairs  = com(zip(lMap,l),2)
for (name1,set1),(name2,set2) in pairs:
    art = set1.intersection(set2)
    if len(art) >=3:
        print(f'The DJs {name1} and {name2} have {len(art)} artists common between them.\n')
# Output
# The DJs Kevin and Bob have 4 artists common between them.

# The DJs Stuart and Bob have 4 artists common between them.

# The DJs Stuart and Edith have 3 artists common between them.

# The DJs Bob and Edith have 3 artists common between them.
