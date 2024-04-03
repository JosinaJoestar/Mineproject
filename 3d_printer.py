import mcpi.minecraft as mine
import mcpi.block as block
import numpy as np
import time
from functools import lru_cache
from midvoxio.voxio import vox_to_arr

mc = mine.Minecraft.create('localhost', 4711) 

colors_mapping = {
    (255, 255, 255): block.Block(251, 0),  #Blanc
    (0, 0, 0): block.Block(251, 15),  #Noir
    (48, 50, 142): block.Block(251, 11), # Bleu
    (84, 109, 20): block.Block(251, 13), # Vert
    (151, 36, 31): block.Block(251,14), # Rouge
    (112, 38, 157): block.Block(251, 10), # Violet
    (107, 67, 39): block.Block(251, 12),  # Marron
    (60, 171, 204): block.Block(251, 9),  # Cyan
    (220, 105, 16): block.Block(251, 1), # Orange
    (167, 56, 157): block.Block(251, 2),# Magenta
    (229, 191, 48): block.Block(251, 4),  # Jaune
    (92, 160, 24): block.Block(251, 5),  # VertC
    (132, 132, 126): block.Block(251, 8),  # GrisC
    (61, 67, 70): block.Block(251, 7),  # Gris
    (191, 159, 146): block.Block(159, 0),  #TCBlanc
    (145, 75, 33): block.Block(159, 1),  # TCOrange
    (135, 78, 98): block.Block(159, 2),  #TCMagenta
    (101, 97, 125): block.Block(159, 3), #TCBleuC
    (168, 118, 31): block.Block(159, 4), # TCJaune
    (91, 106, 46): block.Block(159, 5),  # TCVertC
    (150, 73, 73): block.Block(159, 6), # TCRose
    (52, 37, 32): block.Block(159, 7), # TCGris
    (122, 96, 88): block.Block(159, 8),  #TCGris
    (77, 81, 82): block.Block(159, 9), # TCCyan
    (109, 64, 79): block.Block(159, 10), # TCViolet
    (66, 53, 82): block.Block(159, 11),  # TCBleu
    (71, 47, 33): block.Block(159, 12),  # TCMarron
    (68, 75, 36): block.Block(159, 13),  # TCVert
    (132, 57, 44): block.Block(159, 14), # TCRouge
    (34, 21, 15): block.Block(159, 15),  # TCNoir

}
@lru_cache(maxsize=None)
def closest(rgb):
    rgb = tuple(rgb)
    closest_color = min(colors_mapping.keys(), key=lambda color: np.linalg.norm(np.array(color) - np.array(rgb)))
    return colors_mapping[closest_color]
               


def draw_voxel(voxel):

    voxel = vox_to_arr(voxel, -1)
    px,py,pz = mc.player.getPos()
    for i in range(voxel.shape[0]):
        for j in range(voxel.shape[1]):
            for k in range(voxel.shape[2]):
                
                if not(np.array_equal(voxel[i][j][k][:3], [0,0,0])):
                    voxel[i][j][k][:3] = [int(c * 255) for c in voxel[i, j, k][:3]]
                    cube = closest(tuple(voxel[i][j][k][:3]))
                    
                    mc.setBlock(px+i, py+k, pz+j, (cube.id, cube.data))
                else:
                    continue
                    # mc.setBlock(px+i, py+j, pz+k, 0, block.AIR.id)




def main():
    #vox = voxel_parser(r'C:\Users\kamil\OneDrive\Bureau\untitled.vox')
    draw_voxel(r'voxels\grosbatima.vox')
 
if __name__ == "__main__":
    main()

