# Defaults-instafader

## Requirements

* Python
* Pillow module (```pip install pillow``` or ```python3 -m pip install Pillow``` in a terminal)


## Usage

### TLDR version

1. Download this repository
2. Place the files into your skin foler
3. Run the python file 
4. Answer the two questions: @2x files are needed for the @2x option and the HitCircleOverlap value in the skin.ini will be rewritten if you wish
5. That's it! Reload your skin/open osu! and your circles will now be instafade. The original files will be in a folder titled "old_circles"

### Detailed version

#### Python setup
1. Download [python](www.python.org) and make sure to add it to PATH in the setup wizard
2. Open a terminal and type ```python3 -m pip install Pillow```. If that doesn't work, try ```pip install Pillow```
3. Continue to Usage

#### Usage
1. Download this repository (green button towards the top right)
2. Place ALL of the files from the .zip file into the skin folder you want to alter
3. Run the file.
   * Open a terminal
   * Navigate to the folder directory (usually you can copy the directory from the top of the file explorer and remove \Users\yourname then type "cd .\TheThingYouJustCopied"
   * Type ```python3 main2.py``` in ther terminal while in that directory
