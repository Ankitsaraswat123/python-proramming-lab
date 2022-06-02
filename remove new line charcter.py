with open("1.txt") as f, open("2.txt", 'w') as g:
    for s in f.readlines():
        g.write(s.strip()+" ")
