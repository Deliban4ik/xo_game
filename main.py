def xo():
    '''Осторожно говнокод
    мб в будущем будет оптимизирован и станет более читабельным'''
    team1=str(input("Choose your team\n"))
    def check_input(slots,input, count, field):
        match count:
            case 2:
                sym="o"
                if slots[input]==" " and input in slots.keys():
                    slots[input]=sym
                    print(field.format(c1=slots["1"],c2=slots["2"],c3=slots["3"],c4=slots["4"],c5=slots["5"],c6=slots["6"],c7=slots["7"],c8=slots["8"],c9=slots["9"]))
                    if slots["1"]==slots["2"]==slots["3"]==sym:
                        print(f"o win")
                    elif slots["4"]==slots["5"]==slots["6"]==sym:
                        print(f"o win")
                    elif slots["7"]==slots["8"]==slots["9"]==sym:
                        print(f"o win")
                    elif slots["1"]==slots["4"]==slots["7"]==sym:
                        print(f"o win")
                    elif slots["2"]==slots["5"]==slots["8"]==sym:
                        print(f"o win")
                    elif slots["3"]==slots["6"]==slots["9"]==sym:
                        print(f"o win")
                    elif slots["1"]==slots["5"]==slots["9"]==sym:
                        print(f"o win")
                    elif slots["7"]==slots["5"]==slots["3"]==sym:
                        print(f"o win")
                else:
                    pass
            case 1:
                sym="x"
                if slots[input]==" " and input in slots.keys():
                    slots[input]=sym
                    print(field.format(c1=slots["1"],c2=slots["2"],c3=slots["3"],c4=slots["4"],c5=slots["5"],c6=slots["6"],c7=slots["7"],c8=slots["8"],c9=slots["9"]))
                    if slots["1"]==slots["2"]==slots["3"]==sym:
                        print(f"x win")
                    elif slots["4"]==slots["5"]==slots["6"]==sym:
                        print(f"x win")
                    elif slots["7"]==slots["8"]==slots["9"]==sym:
                        print(f"x win")
                    elif slots["1"]==slots["4"]==slots["7"]==sym:
                        print(f"x win")
                    elif slots["2"]==slots["5"]==slots["8"]==sym:
                        print(f"x win")
                    elif slots["3"]==slots["6"]==slots["9"]==sym:
                        print(f"x win")
                    elif slots["1"]==slots["5"]==slots["9"]==sym:
                        print(f"x win")
                    elif slots["7"]==slots["5"]==slots["3"]==sym:
                        print(f"x win")
                else:
                    pass
    slots={
        "1": " ",
        "2": " ",
        "3": " ",
        "4": " ",
        "5": " ",
        "6": " ",
        "7": " ",
        "8": " ",
        "9": " ",}
    field="|---|---|---|\n| {c1} | {c2} | {c3} |\n|---|---|---|\n| {c4} | {c5} | {c6} |\n|---|---|---|\n| {c7} | {c8} | {c9} |\n|---|---|---|"
    while True:
        if team1=="x":
            x=str(input())
            count=1
            if x=="quit" or x=="":
                break
            check_input(slots, x, count, field)
            o=str(input())
            count+=1
            if o=="quit" or o=="":
                break
            check_input(slots, o, count, field)
            count=0  
        elif team1=="o":
            o=str(input())
            count=2
            if o=="quit" or o=="":
                break
            check_input(slots, o, count, field)
            
            x=str(input())
            count-=1
            if x=="quit" or x=="":
                break
            check_input(slots, x, count, field)
            count=0  
        else:
            break
xo()

    
