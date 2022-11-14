def tesk1('в лесу стояли ели'):
    words = "в лесу стояли ели"
    count = 0
    for word in words.split(" "):
        if word.strip()[0] == 'е':
            count +=1
    print(count)
tesk1('в лесу стояли ели')
