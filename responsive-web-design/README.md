# ¿Que es el responsive web design? o Diseño web responsivo

es crear tu web usando HTML y CSS de forma que automáticamete tu sitio responda bien a todas la dimensiones, que se ``rescale`` y ``adapte`` para que se vea bien en todos lados para que se vea bien en todos los dispositivos.


<img src="https://user-images.githubusercontent.com/69850751/178127634-965e1c0d-4f37-4c61-af98-3530320ae569.jpg" />


# Imagenes responsive

Las imágenes responsive se escalan de forma que sea vean bien en todos los tamañanos.

````c
<img src="fondo.jpg" style="width:100%">
````

## Evitar imagenes pixeladas en el cambio de tamaño

````c`
<img src="fondo.jpg" style="max-width:100%;height: auto;">
````

# Mostrar diferentes imagenes con variación de tamaño, segun tamaño

```<picture>``
nos permite definir diferentes imagenes para difrentes tamaños de ventanas.

````c
<picture>
    <source media="(min-width: 500px)" srcset="car.jpg">
    <source media="(min-width: 300px)" srcset="flor.jpg">
    <img src="fondo.jpg">
</picture>
````

## Texto Responsive

el texto de la página se puede hacer adaptable
con ``VIEWPORT``

1vw = 1% del viewport width

````c
<h1 style="font-size:10vw">Hola</h1>
````

## Media Queries

podemos hacer responsive textos, imagenes y entre otras cosas, directamente con el uso de mediaqueries.

````c
.content {
   float: left;
   width: 20%; 
}

@media screen and (max-width: 800px){
    .content {
        width: 100%;
    }
}
````



