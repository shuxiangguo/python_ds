# 任意进制转换


def toStr(n, base):
    convertString = "0123456789"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]


def toStrWithStack(n, base):
    mylist = []
    convertString = "0123456789ABCDEF"
    if n < base:
        mylist.append(convertString[n])
    else:
        mylist.append(convertString[n//base])
        toStrWithStack(n//base, base)
    print(mylist)



def main():
    # num = toStr(10, 8)
    num = toStrWithStack(16, 16)
    print(num)


if __name__ == '__main__':
    main()
