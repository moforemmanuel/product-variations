def get_variations():
    colors = ['green', 'red', 'yellow', 'black']
    sizes = ['sm','md','lg']
    weights = [100, 200]
    name = 'iphone 13 pro'
    price = 2000

    
    variations = {}
    for color in colors:
        for size in sizes:
            for weight in weights:
                
                #price handler
                if color in ('green','red','yellow'):
                    price = price + 50

                #size handler
                if size == 'sm':
                    price = price - 50
                elif size == 'lg':
                    price = price + 50

                #weigth handler
                if weight == '200':
                    price = price + 50
                """
                option = {"{}g-{}-{}".format(weight, size, color):{
                    'color':color,
                    'size':size,
                    'price':price,
                    'url':"{}{}g_{}_{}_{}".format("url_to_image_of_",weight,size,color,name)
                    }}
                """
                attrib = {
                    'name':name,
                    'color':color,
                    'size':size,
                    'price':price,
                    'description':"This is an {}, coloured {}, {} size and weighs {}g. It costs ${} and is a recommended product.".format(name,color,size,weight,price),
                    'url':"{}{}g_{}_{}_{}".format("url_to_image_of_",weight,size,color,name)
                }

                variations["{}g-{}-{}".format(weight, size, color)] = attrib

    return variations
    
def get_specific(color, size, weight):
    variations = get_variations()
    
    if "{}g-{}-{}".format(weight, size, color) in variations.keys():
        return variations["{}g-{}-{}".format(weight, size, color)]

black = get_specific('black','md',100)
#print(get_variations())
print(black)
