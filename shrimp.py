shrimp = {"炸鳳尾蝦":["蝦子","核果","油"],"雲龍炸蝦":["蝦子","核果","油","醬汁","豆皮"]}
print(list(shrimp.items()))

lee = set(list(shrimp["炸鳳尾蝦"]))
liu = set(list(shrimp["雲龍炸蝦"]))

print("劉昴星的作品中比李嚴的作品多用了",liu - lee)
print("李嚴的作品中比劉昴星的作品多用了",lee - liu)

lee.update(["蘋果","洋蔥","醬汁"])
print("現在李嚴的作品中比劉昴星的作品多用了",lee-liu)

shrimp["炸鳳尾蝦"] = list(lee)
print(list(shrimp.items()))