def counter(string, leng):
    string = str(string).lower()
    count = 0
    if string == '':
        return ''
    if leng == 'en':
        for i in string:
            if i == 'a':
                count += 1
        return count
    elif leng == 'rus':
        for i in string:
            if i == 'а':
                count += 1
        return count
