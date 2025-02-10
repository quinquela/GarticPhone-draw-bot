from PIL import Image

def pasrabyn(path, umbral):

    imagen = Image.open(path).convert("L") 
    

    max_size = (500, 500)
    if imagen.size[0] > max_size[0] or imagen.size[1] > max_size[1]:
        imagen.thumbnail(max_size)  


    
    binaria = imagen.point(lambda x: 255 if x > umbral else 0, "1")  
    
    return binaria
