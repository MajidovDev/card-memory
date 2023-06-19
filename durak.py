allcard = {
    'a': ['ay', 'ak', 'ach', 'aq'],
    'k': ['ky', 'kk', 'kch', 'kq'],
    'q': ['qy', 'qk', 'qch', 'qq'],
    'j': ['jy', 'jk', 'jch', 'jq'],
    '1': ['10y', '10k', '10ch', '10q'],
    '9': ['9y', '9k', '9ch', '9q']
}
trash = {
    'a': [],
    'k': [],
    'q': [],
    'j': [],
    '1': [],
    '9': []
}
shown = ''

me = {
    'a': [],
    'k': [],
    'q': [],
    'j': [],
    '1': [],
    '9': []
}

player = {
    'a': [],
    'k': [],
    'q': [],
    'j': [],
    '1': [],
    '9': []
}

shown = input('shown >>> ').lower()
# print('shown', shown[0])
# print('allcard[sh[0]]', allcard[shown[0]])
allcard[shown[0]].remove(shown)

while True:
    mc = map(str, input("ME cards >>> ").split('-'))  # my cards
    for card in mc:
        card = card.lower()
        if card in allcard[card[0]]:
            allcard[card[0]].remove(card)
        if card not in me[card[0]]:
            me[card[0]].append(card)

    ig = map(str, input('in game>>> ').split('-'))  # in game
    tort = input("trash(t) or take(p or me)>> ")
    tort = tort.lower()

    if tort == 't':
      for card in ig:
          card = card.lower()
          if card in allcard[card[0]]:
            allcard[card[0]].remove(card)
          if card in player[card[0]]:
              player[card[0]].remove(card)
          if card in me[card[0]]:
              me[card[0]].remove(card)
          trash[card[0]].append(card)
    elif tort == 'p':
        for card in ig:
            if card not in player[card[0]]:
                player[card[0]].append(card)
            if card in me[card[0]]:
                me[card[0]].remove(card)
    else:
        for card in ig:
            if card not in me[card[0]]:
              me[card[0]].append(card)
            if card in player[card[0]]:
              player[card[0]].remove(card)

    show = input("sh ? not >>> ")
    show = show.lower()
    while show == 'sh':
      see = input("trash(t) | me(me) | allcard(ac) | player(p) >>> ")
      see = see.lower()
      if see == 't':
          print(trash)
      elif see == 'me':
          print(me)
      elif see == 'p':
          print(player)
      else:
          print(allcard)
      show = input("sh ? not >>> ")
      show = show.lower()
