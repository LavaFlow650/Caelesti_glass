hello hopefully you find this usefull/its not too late

before you start, make sure you have python installed (version 3)
make sure you also get the png package by running "pip install pypng"

then you will have to finish adding all of you custom colors into the colors folder
-i tried to copy your light_green and red textures from ur vid but yt compression kinda messes with the exact color so you should redo them
-i also dont think that I got the opacity right

-the colors are stored in a list as hex RGBA values
-the order should match the order of the colors in "list of ref colors.txt"
-if you want to you should be able to add/remove colors but make sure that the number of colors lines up between files

then you will need to replace "ref_images/ref_image.png" with ur own texture, you can also use a differnt name, just change it in main.py

then run main.py (you might need to change REF_IMAGE to mach the name of your referance image)

then you will find all the images you need in folders in texture_export

if you wanna see the script working, you should be able to delete the contents (the folders light_green and red) of texture_export and then run main.py and they should reappear
