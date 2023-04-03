def return_bigger(a,b):
    try:
        if b > a:
            return b
        else:
            return a
    except Exception as e:
        print(e)
        return None