import pyautogui
import PIL
from PIL import Image
import blancoynegro
from blancoynegro import pasrabyn
import time


pyautogui.PAUSE = 0.00001
pyautogui.MINIMUM_DURATION = 0.00001


imagen_path = input("image path:")
umbral_input = input("Threshold for black and white conversion:")
umbral = int(umbral_input)
def encontrar_pixels_negros(ruta_imagen):
    try:

        img = Image.open(ruta_imagen)

        img_gris = blancoynegro.pasrabyn(ruta_imagen, umbral=umbral)

        # Obtener las dimensiones de la imagen
        ancho, alto = img_gris.size


        pixels_negros = []

        for x in range(ancho):
            for y in range(alto):

                valor_pixel = img_gris.getpixel((x, y))


                if valor_pixel <= 0:  
                    pixels_negros.append((x, y))

        return pixels_negros

    except FileNotFoundError:
        print(f"Error: No se encontró la imagen en la ruta '{ruta_imagen}'")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None




def hacer_clics_en_pixels_negros_en_cuadrado_centrado():
    ubicaciones_negros = encontrar_pixels_negros(imagen_path)

    if ubicaciones_negros is None:
        print("The locations of the black pixels could not be found.")
        return

    if not ubicaciones_negros:
        print("The locations of the black pixels could not be found.")
        return


    screen_width, screen_height = pyautogui.size()


    cuadrado_lado = 500
    inicio_x_cuadrado = (screen_width - cuadrado_lado) // 2
    inicio_y_cuadrado = (screen_height - cuadrado_lado) // 2

    print("Starting to draw...")
    for x_pixel, y_pixel in ubicaciones_negros:

        x_pantalla = inicio_x_cuadrado + x_pixel
        y_pantalla = inicio_y_cuadrado + y_pixel


        pyautogui.moveTo(x_pantalla, y_pantalla)


        pyautogui.click()


    print("Finish")

print("wait 10 seconds")
time.sleep(10)
hacer_clics_en_pixels_negros_en_cuadrado_centrado()
