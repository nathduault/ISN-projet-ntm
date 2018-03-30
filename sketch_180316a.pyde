from random import randint

screenHeight = 800
screenWidth = 800

def setup():
    size(screenHeight,screenWidth)
    url_1 = "https://png.pngtree.com/element_origin_min_pic/16/10/08/1657f8a84bf3e06.jpg"
    image_1 = loadImage(url_1, "png")
    image_1.resize(screenHeight,screenWidth)
    background(image_1)
    url_2 = "https://tse2.mm.bing.net/th?id=OIP.rdD1nSWAxB41WBIGDHAq9gHaGM&pid=15.1"
    global webImg
    webImg = loadImage(url_2, "png")
    webImg.resize(75,75)
    frameRate(0.7)
    
def draw():
    image(webImg,random(0,screenHeight-75),random(0,screenWidth-75),75,75,)
    if mousePressed()
    #trouver comment associer le clique de la souris à la disparition des images avec mousePressed()
    #remplacer l'image par celle de Marie
    

    





    

    