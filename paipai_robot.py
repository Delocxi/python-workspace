message = ""
dirtyword = '幹'#,'幹你娘','幹你媽','操','操你媽','靠北','靠邀','靠么','機掰','雞掰'
keyword = '謝謝'#,'謝啦','謝了'

while message != "bye":
    message = input(">> ")
    if dirtyword in message:
        print("你是在大聲什麼啦？")
        break
    elif keyword in message:
        print("小意思啦！")
    else:
        print("拍拍。")
