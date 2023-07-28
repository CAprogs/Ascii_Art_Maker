"""                                                                                                                                                                             
                                                                                                                                                                             
               AAA                 SSSSSSSSSSSSSSS         CCCCCCCCCCCCCIIIIIIIIIIIIIIIIIIII                    AAA               RRRRRRRRRRRRRRRRR   TTTTTTTTTTTTTTTTTTTTTTT
              A:::A              SS:::::::::::::::S     CCC::::::::::::CI::::::::II::::::::I                   A:::A              R::::::::::::::::R  T:::::::::::::::::::::T
             A:::::A            S:::::SSSSSS::::::S   CC:::::::::::::::CI::::::::II::::::::I                  A:::::A             R::::::RRRRRR:::::R T:::::::::::::::::::::T
            A:::::::A           S:::::S     SSSSSSS  C:::::CCCCCCCC::::CII::::::IIII::::::II                 A:::::::A            RR:::::R     R:::::RT:::::TT:::::::TT:::::T
           A:::::::::A          S:::::S             C:::::C       CCCCCC  I::::I    I::::I                  A:::::::::A             R::::R     R:::::RTTTTTT  T:::::T  TTTTTT
          A:::::A:::::A         S:::::S            C:::::C                I::::I    I::::I                 A:::::A:::::A            R::::R     R:::::R        T:::::T        
         A:::::A A:::::A         S::::SSSS         C:::::C                I::::I    I::::I                A:::::A A:::::A           R::::RRRRRR:::::R         T:::::T        
        A:::::A   A:::::A         SS::::::SSSSS    C:::::C                I::::I    I::::I               A:::::A   A:::::A          R:::::::::::::RR          T:::::T        
       A:::::A     A:::::A          SSS::::::::SS  C:::::C                I::::I    I::::I              A:::::A     A:::::A         R::::RRRRRR:::::R         T:::::T        
      A:::::AAAAAAAAA:::::A            SSSSSS::::S C:::::C                I::::I    I::::I             A:::::AAAAAAAAA:::::A        R::::R     R:::::R        T:::::T        
     A:::::::::::::::::::::A                S:::::SC:::::C                I::::I    I::::I            A:::::::::::::::::::::A       R::::R     R:::::R        T:::::T        
    A:::::AAAAAAAAAAAAA:::::A               S:::::S C:::::C       CCCCCC  I::::I    I::::I           A:::::AAAAAAAAAAAAA:::::A      R::::R     R:::::R        T:::::T        
   A:::::A             A:::::A  SSSSSSS     S:::::S  C:::::CCCCCCCC::::CII::::::IIII::::::II        A:::::A             A:::::A   RR:::::R     R:::::R      TT:::::::TT      
  A:::::A               A:::::A S::::::SSSSSS:::::S   CC:::::::::::::::CI::::::::II::::::::I       A:::::A               A:::::A  R::::::R     R:::::R      T:::::::::T      
 A:::::A                 A:::::AS:::::::::::::::SS      CCC::::::::::::CI::::::::II::::::::I      A:::::A                 A:::::A R::::::R     R:::::R      T:::::::::T      
AAAAAAA                   AAAAAAASSSSSSSSSSSSSSS           CCCCCCCCCCCCCIIIIIIIIIIIIIIIIIIII     AAAAAAA                   AAAAAAARRRRRRRR     RRRRRRR      TTTTTTTTTTT      
                                                                                                                                                                             

"""
from PIL import Image

# adapter la taille de l'ascii image à la taille de l'image de base 
ASCII_CHARS = '@%#*+=-:. '

def resize_image(image, new_width):
    width, height = image.size
    ratio = height / float(width)
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale(image):
    return image.convert('L')

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ''
    for pixel_value in pixels:
        # Assurer que pixel_value est dans l'intervalle 0-255
        pixel_value = max(pixel_value, 0)
        pixel_value = min(pixel_value, 255)
        # Conversion de pixel_value en caractère ASCII
        ascii_str += ASCII_CHARS[pixel_value * (len(ASCII_CHARS) - 1) // 255]
    return ascii_str

def main(image_path, new_width=200): # taille de la sortie
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    image = grayscale(image)
    image = resize_image(image, new_width)
    ascii_str = pixels_to_ascii(image)

    # Afficher l'ASCII art
    width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ''
    for i in range(0, ascii_str_len, width):
        ascii_img += ascii_str[i:i + width] + '\n'
    
    print(ascii_img)

if __name__ == "__main__":
    image_path = "/Users/charles-albert/Desktop/ASCII ART/Bart_Simpson_.png"  # Remplacez par le chemin de votre image
    main(image_path)
