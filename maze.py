import mcpi.minecraft as mine
import mcpi.block as block
import cv2
import numpy as np
from PIL import Image
import time



mc = mine.Minecraft.create('localhost', 4711)

    


def vect_proche(colors, vect3):
    vect3_np = np.array(vect3)
    min_dist = np.inf
    closest_color = None
    for color, rgb in colors.items():
        rgb_np = np.array(rgb)
        dist = np.linalg.norm(vect3_np - rgb_np)
        if dist < min_dist:
            min_dist = dist
            closest_color = rgb
    return closest_color
 
def bnw(h):
    px, py, pz = mc.player.getPos()
    image = cv2.imread(r'images_bnw\image.png' , 0)
    if image is None:
        print("Erreur lors du chargement de l'image.")
        return None
    
    merde, binaire = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    
    ret = np.where(binaire == 255, 1, 0)
    if ret is not None :
        
        for i in range(len(ret)):
            for j in range(len(ret[i])):
                if ret[i][j] == 0 :

                    for k in range(h):
                        mc.setBlock(px+i, py+k, pz+j, block.OBSIDIAN.id)    
    return ret

def tableau(plat):
    px, py, pz = mc.player.getPos()
    image = Image.open(r"images\morchot.jpg")
    colors = {"Noir":[0,0,0], "Blanc": [255,255,255] , "Bleu": [48,50,142], "Vert": [84,109,20], "Rouge": [151,36,31], "Violet":[112,38,157], "Marron":[107,67,39],"Cyan":[60,171,204], "Orange":[220,105,16],"Magenta":[167,56,157], "Jaune":[229,191,48],"VertC":[92,160,24],"GrisC":[132,132,126], "Gris": [61,67,70], "TC_blanc":[191,159,146], "TC_orange" : [145,75,33], "TC_magenta":[135,78,98],"TC_bleuC" : [101,97,125], "TC_jaune":[168,118,31], "TC_vertC":[91,106,46], "TC_rose":[150,73,73], "TC_gris":[52,37,32], "TC_grisC":[122,96,88], "TC_Cyan": [77,81,82] , "TC_violet": [109,64,79], "TC_bleu": [66,53,82], "TC_marron": [71,47,33], "TC_vert":[68,75,36], "TC_rouge" : [132,57,44], "TC_noir": [34,21,15]}
    texture = 251    
    image = image.convert("RGB")
    matrix = np.array(image)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = vect_proche(colors, matrix[i][j])
    if plat:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if np.array_equal(matrix[i][j], colors["Blanc"]) :  
                    mc.setBlock(px+i, py, pz+j, block.Block(texture,0))   
                elif np.array_equal(matrix[i][j], colors["Noir"]) :  
                    mc.setBlock(px+i, py, pz+j, block.Block(texture,15))                
                elif np.array_equal(matrix[i][j], colors["Bleu"]) :  
                    mc.setBlock(px+i, py, pz+j, block.Block(texture,11))
                elif np.array_equal(matrix[i][j], colors["Vert"]) :  
                    mc.setBlock(px+i, py, pz+j, block.Block(texture,13))
                elif np.array_equal(matrix[i][j], colors["Rouge"]) :  
                    mc.setBlock(px+i, py, pz+j, block.Block(texture,14))
                elif np.array_equal(matrix[i][j], colors["Violet"]) :  
                    mc.setBlock(px+i, py, pz+j, block.Block(texture,10))
                elif np.array_equal(matrix[i][j], colors["Marron"]) :  
                    mc.setBlock(px+i, py, pz+j, block.Block(texture,12))
                elif np.array_equal(matrix[i][j], colors["Cyan"]) :  
                    mc.setBlock(px+i, py, pz+j, block.Block(texture,9))
                elif np.array_equal(matrix[i][j], colors["Orange"]) :  
                    mc.setBlock(px+i, py, pz+j, block.Block(texture,1))
                elif np.array_equal(matrix[i][j], colors["Magenta"]) :  
                    mc.setBlock(px+i, py, pz+j, block.Block(texture,2)) 
                elif np.array_equal(matrix[i][j], colors["Jaune"]) :  
                    mc.setBlock(px+i, py, pz+j, block.Block(texture,4))  
                elif np.array_equal(matrix[i][j], colors["VertC"]) :  
                    mc.setBlock(px+i, py, pz+j, block.Block(texture,5))
                elif np.array_equal(matrix[i][j], colors["Gris"]) :  
                    mc.setBlock(px+i, py, pz+j, block.Block(texture,7))
                elif np.array_equal(matrix[i][j], colors["GrisC"]) :  
                    mc.setBlock(px+i, py, pz+j, block.Block(texture,8))
                elif np.array_equal(matrix[i][j], colors["TC_blanc"]) :  
                    mc.setBlock(px+i, py, pz+j, block.Block(159,0))
                elif np.array_equal(matrix[i][j], colors["TC_orange"]) :
                    mc.setBlock(px+i, py, pz+j, block.Block(159,1))
                elif np.array_equal(matrix[i][j], colors["TC_magenta"]) :
                    mc.setBlock(px+i, py, pz+j, block.Block(159,2))
                elif np.array_equal(matrix[i][j], colors["TC_bleuC"]) :
                    mc.setBlock(px+i, py, pz+j, block.Block(159,3))
                elif np.array_equal(matrix[i][j], colors["TC_jaune"]) :
                    mc.setBlock(px+i, py, pz+j, block.Block(159,4))
                elif np.array_equal(matrix[i][j], colors["TC_vertC"]) :
                    mc.setBlock(px+i, py, pz+j, block.Block(159,5))
                elif np.array_equal(matrix[i][j], colors["TC_rose"]) :
                    mc.setBlock(px+i, py, pz+j, block.Block(159,6))
                elif np.array_equal(matrix[i][j], colors["TC_gris"]) :
                    mc.setBlock(px+i, py, pz+j, block.Block(159,7))
                elif np.array_equal(matrix[i][j], colors["TC_grisC"]) :
                    mc.setBlock(px+i, py, pz+j, block.Block(159,8))
                elif np.array_equal(matrix[i][j], colors["TC_Cyan"]) :
                    mc.setBlock(px+i, py, pz+j, block.Block(159,9))
                elif np.array_equal(matrix[i][j], colors["TC_violet"]) :
                    mc.setBlock(px+i, py, pz+j, block.Block(159,10))
                elif np.array_equal(matrix[i][j], colors["TC_bleu"]) :
                    mc.setBlock(px+i, py, pz+j, block.Block(159,11))
                elif np.array_equal(matrix[i][j], colors["TC_marron"]) :
                    mc.setBlock(px+i, py, pz+j, block.Block(159,12))
                elif np.array_equal(matrix[i][j], colors["TC_vert"]) :
                    mc.setBlock(px+i, py, pz+j, block.Block(159,13))
                elif np.array_equal(matrix[i][j], colors["TC_rouge"]) :
                    mc.setBlock(px+i, py, pz+j, block.Block(159,14))
                elif np.array_equal(matrix[i][j], colors["TC_noir"]) :
                    mc.setBlock(px+i, py, pz+j, block.Block(159,15))
                else :
                    mc.setBlock(px+i, py, pz+j, block.Block(texture,15))
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if np.array_equal(matrix[len(matrix)-i][len(matrix-j)], colors["Blanc"]) :  
                    mc.setBlock(px, py+i, pz+j, block.Block(texture,0))   
                elif np.array_equal(matrix[i][j], colors["Noir"]) :  
                    mc.setBlock(px, py+i, pz+j, block.Block(texture,15))                
                elif np.array_equal(matrix[i][j], colors["Bleu"]) :  
                    mc.setBlock(px, py+i, pz+j, block.Block(texture,11))
                elif np.array_equal(matrix[i][j], colors["Vert"]) :  
                    mc.setBlock(px, py+i, pz+j, block.Block(texture,13))
                elif np.array_equal(matrix[i][j], colors["Rouge"]) :  
                    mc.setBlock(px, py+i, pz+j, block.Block(texture,14))
                elif np.array_equal(matrix[i][j], colors["Violet"]) :  
                    mc.setBlock(px, py+i, pz+j, block.Block(texture,10))
                elif np.array_equal(matrix[i][j], colors["Marron"]) :  
                    mc.setBlock(px, py+i, pz+j, block.Block(texture,12))
                elif np.array_equal(matrix[i][j], colors["Cyan"]) :  
                    mc.setBlock(px, py+i, pz+j, block.Block(texture,9))
                elif np.array_equal(matrix[i][j], colors["Orange"]) :  
                    mc.setBlock(px, py+i, pz+j, block.Block(texture,1))
                elif np.array_equal(matrix[i][j], colors["Magenta"]) :  
                    mc.setBlock(px, py+i, pz+j, block.Block(texture,2)) 
                elif np.array_equal(matrix[i][j], colors["Jaune"]) :  
                    mc.setBlock(px, py+i, pz+j, block.Block(texture,4))  
                elif np.array_equal(matrix[i][j], colors["VertC"]) :  
                    mc.setBlock(px, py+i, pz+j, block.Block(texture,5))
                elif np.array_equal(matrix[i][j], colors["Gris"]) :  
                    mc.setBlock(px, py+i, pz+j, block.Block(texture,7))
                elif np.array_equal(matrix[i][j], colors["GrisC"]) :  
                    mc.setBlock(px, py+i, pz+j, block.Block(texture,8))
                elif np.array_equal(matrix[i][j], colors["TC_blanc"]) :  
                    mc.setBlock(px, py+i, pz+j, block.Block(159,0))
                elif np.array_equal(matrix[i][j], colors["TC_orange"]) :
                    mc.setBlock(px, py+i, pz+j, block.Block(159,1))
                elif np.array_equal(matrix[i][j], colors["TC_magenta"]) :
                    mc.setBlock(px, py+i, pz+j, block.Block(159,2))
                elif np.array_equal(matrix[i][j], colors["TC_bleuC"]) :
                    mc.setBlock(px, py+i, pz+j, block.Block(159,3))
                elif np.array_equal(matrix[i][j], colors["TC_jaune"]) :
                    mc.setBlock(px, py+i, pz+j, block.Block(159,4))
                elif np.array_equal(matrix[i][j], colors["TC_vertC"]) :
                    mc.setBlock(px, py+i, pz+j, block.Block(159,5))
                elif np.array_equal(matrix[i][j], colors["TC_rose"]) :
                    mc.setBlock(px, py+i, pz+j, block.Block(159,6))
                elif np.array_equal(matrix[i][j], colors["TC_gris"]) :
                    mc.setBlock(px, py+i, pz+j, block.Block(159,7))
                elif np.array_equal(matrix[i][j], colors["TC_grisC"]) :
                    mc.setBlock(px, py+i, pz+j, block.Block(159,8))
                elif np.array_equal(matrix[i][j], colors["TC_Cyan"]) :
                    mc.setBlock(px, py+i, pz+j, block.Block(159,9))
                elif np.array_equal(matrix[i][j], colors["TC_violet"]) :
                    mc.setBlock(px, py+i, pz+j, block.Block(159,10))
                elif np.array_equal(matrix[i][j], colors["TC_bleu"]) :
                    mc.setBlock(px, py+i, pz+j, block.Block(159,11))
                elif np.array_equal(matrix[i][j], colors["TC_marron"]) :
                    mc.setBlock(px, py+i, pz+j, block.Block(159,12))
                elif np.array_equal(matrix[i][j], colors["TC_vert"]) :
                    mc.setBlock(px, py+i, pz+j, block.Block(159,13))
                elif np.array_equal(matrix[i][j], colors["TC_rouge"]) :
                    mc.setBlock(px, py+i, pz+j, block.Block(159,14))
                elif np.array_equal(matrix[i][j], colors["TC_noir"]) :
                    mc.setBlock(px, py+i, pz+j, block.Block(159,15))
                else :
                    mc.setBlock(px, py+i, pz+j, block.Block(texture,15))  


def image_choix(event):
    ret = ""
    if event == "image.png":
        ret = "image.png"
    elif event == "goku.png":
        ret= "goku.png"
            
    elif event == "ali.jpeg":
        ret="ali.jpeg"
            
    elif event == "joconde.png":                   
        ret = "joconde.png"
                          
    elif event == "marchetti.jpg":
        ret = "morchot.jpg"
    else:
        mc.postToChat("\nkteb mgad al 9lawi")
    return ret 
    
def event_chat(event):

                
    if event == "tableau":
        pb = False
        fin = True
        mc.postToChat("plat ou tablo ?")
        while fin:
            if event == "plat":
                pb = True
                fin = False
            elif event == "tablo":
                fin = False 


        mc.postToChat("Les images disponibles sont : \n1- image.png \ \n2- goku.png \n3- ali.jpeg \n4-joconde.png \n5- marchetti.jpg\n")
        while fin:
            if event == "image.png":
                tableau(pb, "image.png")
                fin = False
            elif event == "goku.png":
                tableau(pb, "goku.png")
                fin = False
            elif event == "ali.jpeg":
                tableau(pb, "ali.jpeg")
                fin = False
            elif event == "joconde.png":                   
                tableau(pb, "joconde.png")
                fin = False
                        
            elif event == "marchetti.jpg":
                tableau(True, "morchot.jpg")
                fin = False
            else:
                mc.postToChat("kteb mgad al 9lawi")

        
    


def main():
    # fin = True 

    # while True:
    #     time.sleep(1)
    #     chats = mc.events.pollChatPosts()  
    #     for chat in chats:
    #         if chat.message == "hoho":
    #             mc.postToChat("tableau pour afficher des images a partir des images que j'ai ajoute (y en a 5) et maze plus simple a ecrire en anglais et ca fait un laby...")
    #         if chat.message == "tableau":
    #             mc.postToChat("Les images disponibles sont : 1- image.png 2- goku.png 3- ali.jpeg 4-joconde.png 5- marchetti.jpg")
    #             while fin:
    #                 path = image_choix(chat.message)
    #                 if path != "":
    #                     tableau(True, path)
    #                     fin = False
    #                 else:
    #                     continue
    #         if chat.message =="maze":
    #             bnw()
    #         else:
    #             continue
    #     fin = True
    tableau(True)

if __name__ == '__main__':
    main()


