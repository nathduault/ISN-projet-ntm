from random import randint

screenHeight = 800
screenWidth = 800


def setup():
    global ListeTaupes
    
    size(screenHeight, screenWidth)
    url_1 = "https://png.pngtree.com/element_origin_min_pic/16/10/08/1657f8a84bf3e06.jpg"
    image_1 = loadImage(url_1, "png")
    image_1.resize(screenHeight, screenWidth)
    background(image_1)
    global webImg
    webImg = loadImage("taupe2.0.png")
    webImg.resize(75, 75)
    frameRate(0.7)

    ListeTaupes = []


def draw():
    image(webImg, random(0, screenHeight - 75), random(0, screenWidth - 75), 75, 75, )


def mouseClicked():
    global ListeTaupes
    if mouseButton == LEFT:
        ListeTaupes += [(randint(0, screenHeight - 75), randint(0, screenWidth - 75))]
        ListeTaupesTemp = ListeTaupes[:]
    for taupe in ListeTaupes:
        if (mouseX, mouseY) == ListeTaupesTemp:
            ListeTaupesTemp.remove(image)
        else:
            ListeTaupesTemp = ListeTaupes
        print(ListeTaupesTemp)
        ListeTaupes = ListeTaupesTemp
    """line(mouseX - 15, mouseY, mouseX + 15, mouseY)
    line(mouseX, mouseY - 15, mouseX, mouseY + 15)
    line(s, 0, s, 0)
"""

def souris():
    if (mousePressed == True):
        remove(webImg)

    True = mouseX in size(webImg) and mouseY in size(webImg)