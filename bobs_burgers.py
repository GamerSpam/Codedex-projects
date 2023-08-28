# Bob's Burgers lesson from Codedex

from Small_Modules.restaurants import Restaurant

bobs_burgers = Restaurant()
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.type = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

bjs = Restaurant()
bjs.name = 'BJ\'s Restaurant and Brewhouse'
bjs.type = 'Brewhouse'
bjs.rating = 3.9
bjs.delivery = True

mcds = Restaurant()
mcds.name = 'Mcodonald\'s'
mcds.type = 'Fast Food'
mcds.rating = 3.4
mcds.delivery = True