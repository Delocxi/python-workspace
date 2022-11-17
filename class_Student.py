class Student():
    def __init__(self, name,score):
        self.name = name
        self.score = score

    def compare(self,b):
        battle = sum(self.score.values()) - sum(b.score.values())
        if battle > 0 :
            print(self.name+"贏了")
        elif battle == 0:
            print("什麼?竟然平手!?")
        elif battle < 0:
            print("可...可惡，難道，這就是" + b.name + "真正的實力嗎？")


ming = Student('阿明',{"數學":55,"英文":70,"物理":55})
mei = Student('小美',{"數學":90,"英文":88,"物理":100})
howhow = Student('HowHow',{"數學":80,"英文":60,"物理":40})

print(ming.name,ming.score)
print(mei.name,mei.score)
print(howhow.name,howhow.score)
print('\n小明 vs HowHow')
ming.compare(howhow)
print("\n小明 vs 小美")
ming.compare(mei)
print('\n小美 vs HowHow')
mei.compare(howhow)