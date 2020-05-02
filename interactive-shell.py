while True:
    x = input(">>>")
    if x=='exit()':
        break
    try:
        y=eval(x)
        if y: 
            print(y)
    except:
        try:
            exec(x)
        except Exception as e:
            print("error: ",e)
