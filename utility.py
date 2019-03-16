import random
import qrcode
from captcha.image import ImageCaptcha


number_list = ['0','1','2','3','4','5','6','7','8','9']
alphabet_lowercase = ['a','b','d','e','f','g','h','q','r','t']
alphabet_uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def createTextForCaptcha(captcha_string_size = 6):
    """ creating random characters for captcha """
    
    charList = []
    allChars = number_list  + alphabet_lowercase + alphabet_uppercase

    for i in range(captcha_string_size):
      #select one character randomly from all chars we have
        char = random.choice(allChars)
      # append the selected char to a list of size we provided
        charList.append(char)

    captcha_string = ""
 
    for ch in charList:
        captcha_string +=  str(ch)
    
    return captcha_string

def createCaptchaImage(text):
    """ creating the captcha as per the given text """
    
    imageCaptcha = ImageCaptcha(width=300, height=100)
    captcha_text = text
    image = imageCaptcha.generate_image(captcha_text)
    imageCaptcha.create_noise_dots(image, image.getcolors())
    imageCaptcha.create_noise_curve(image, image.getcolors())

    image_file = captcha_text + ".png"
    imageCaptcha.write(captcha_text, image_file)

    return image_file

def createQrCode(id):
    qr = qrcode.make(str(id))
    qr.save(str(id) + '.bmp')
    
    return qr
