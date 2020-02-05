def seconds():
    a = float(input('Enter the number of seconds: '))
    d = (a // 86400)
    h = (a - d * 86400)//3600
    m = (a - d * 86400- h*3600 ) // 60
    s= a - d * 86400 - h*3600 - m*60
    print('days:',d,'hours;', h, 'min:', m,'sec:', s)
seconds()
