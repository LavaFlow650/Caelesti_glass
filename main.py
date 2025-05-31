import copy
import png
import os

BLOCK_DIMENTIONS = 16

COLORS_PATH = 'colors'
REF_IMAGE = 'ref_images/ref_image.png'
# REF_IMAGE = 'output.png'
REF_KEY_PATH = 'list of ref colors.txt'

def get_color_map(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            assert line[0] == '#'
            assert len(line) == 9

            r = int(line[1:3], 16)
            g = int(line[3:5], 16)
            b = int(line[5:7], 16)
            a = int(line[7:9], 16)

            yield (r, g, b, a)
        
REF_KEY = list(get_color_map(REF_KEY_PATH))

def recolor_list(temp, color_filepath):
    l = temp.copy()
    #print(l)
    re_color = list(get_color_map(color_filepath))
    for row in range(len(l)):
        for col in range(int(len(l[0])/4)):
            # get the color at a pixel
            color = []
            for i in range(4):
                color.append(l[row][col*4+i])
            
            # see if the color matches a referance color
            for color_index in range(len(REF_KEY)):
                if REF_KEY[color_index] == tuple(color):
                    for i in range(4):
                        l[row][col*4+i] = re_color[color_index][i]
    return l

def export_icon(x,y,n,l,name):
    icon = [[0 for col in range(BLOCK_DIMENTIONS*4)] for row in range(BLOCK_DIMENTIONS)]
    for dx in range(BLOCK_DIMENTIONS):
        for dy in range(BLOCK_DIMENTIONS):
            for num in range(4):
                icon[dy][(dx)*4+num] = l[y+dy][(x+dx)*4+num]
    writer = png.Writer(width=BLOCK_DIMENTIONS, height=BLOCK_DIMENTIONS, bitdepth=8, greyscale=False, alpha=True)
    with open('texture_export/{}/{}.png'.format(name,n), 'wb') as f:
        writer.write(f, icon)

def main():
    # get the pixel data of the refrance img
    reader = png.Reader(filename=REF_IMAGE)
    width, height, pixels, metadata = reader.read()

    pixels_list = list(pixels)
    #print(pixels_list)

    # recolor the image list for each color in COLORS_PATH
    for file in os.listdir(COLORS_PATH):
        filename = os.fsdecode(file)
        try:
            os.mkdir('texture_export/{}'.format(filename[:-4]))
        except FileExistsError:
            pass
        print(pixels_list)
        recolored = recolor_list(copy.deepcopy(pixels_list),'{}/{}'.format(COLORS_PATH,filename))
        for h in range(int(height/BLOCK_DIMENTIONS)):
            for w in range(int(width/BLOCK_DIMENTIONS)):
                export_icon(w*BLOCK_DIMENTIONS,h*BLOCK_DIMENTIONS,h*int(width/BLOCK_DIMENTIONS)+w,recolored,'{}'.format(filename[:-4]))
    # export_icon(16*2,16,0,recolored,'testing')
    
    # writer = png.Writer(width=width, height=height, bitdepth=8, greyscale=False, alpha=True)
    # with open('recolored.png', 'wb') as f:
    #     writer.write(f, recolored)

if __name__ == "__main__":
    main()
    
