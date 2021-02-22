from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw, ImageFont
import textwrap
from PIL import Image,ImageDraw
import PIL
import card_creation

root = Tk()
root.withdraw() 

def encryptionController():
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    if(filename.endswith('.png')or filename.endswith('.jpg') or filename.endswith('.jpeg')):
        import encrypt
        base_image = Image.open(filename,'r')
        width,height=base_image.size
        text_message=input('Enter the Text Message to be hidden')
        print('Encrypting...')
        hidden_image=card_creation.generateImage(text_message,width,height)
        encrypt.encryptImage(base_image,hidden_image)
        
    #Code that is reached when the selected file is not an image
    else:
        print('Please Select a png or a jpeg file')
        
def decryptionController():
    import decrypt
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print('Decrypting...')
    if(filename.endswith('.png')):
        encrypted_image = Image.open(filename,'r')
        decrypt.decryptImage(encrypted_image)
    else:
        print('Invalid format. Please select only a .png file')
        
   

    
