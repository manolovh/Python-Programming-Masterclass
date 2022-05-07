with open('Jabberwocky.txt', encoding='utf-8') as jabber:  # default mode when not specified is read/'r'
    for line in jabber:
        print(line.rstrip())
        