# Enhance Net (TFG-Computadores)

For English version, look [here](https://github.com/VicDominguez/EnhanceNet-TFG/tree/91058eba0ebbcd1f126d441ec15ef3987a3caa5f).

Esta es una implementación del modelo ENet-PAT expuesto en el paper "EnhanceNet:
Single Image Super-Resolution through Automated Texture Synthesis" con un ratio de ampliación de 4; basada en la
[implementación original](https://github.com/msmsajjadi/EnhanceNet-Code), de la que recupera sus pesos.

Asi mismo trae un archivo (requisitos.txt) de dependencias para instalarlas mediante pip. 
Se aconseja usar un entorno virtual. 

Está implementación, además de presentar un código en castellano, provee una implementación más legible y utilizable
mediante una simple API creada con Flask. Por otra parte, incluye soporte para imágenes codificadas en base 64, presentes
en mi Trabajo de Fin de Grado.

# Notas

- Se ha reutilizado la implementación original debido a que me fue imposible migrar la implementación a Tensorflow 2 y 
Keras manteniendo la compatibilidad de los pesos originales. Por tanto, se usa Tensorflow 1.14 (versión CPU) y el grafo
de ejecución es creado de nuevo en cada instancia debido a que fui incapaz de solucionar 
los problemas de modificación indeseada de las variables del grafo que provoca la coexistencia de los mismos.

- Las imágenes son reescaladas mediante interpolación bicúbica y el uso de la propia red.

- La implementación no es tolerante a los errores OOM (Out Of Memory), por lo que **debe** 
usarse en un equipo con gran cantidad de ram disponible. Con 4GB de RAM la ampliación de imágenes 
con resoluciones superiores a 256x256 no está garantizanda, así mismo con 8GB de RAM e imágenes superiores a 512x512.

- La implementación, al estar basada en la original, no es significativa en tiempo de cómputo ni de memoria, por lo que 
sólo **debe** de usarse en entornos de desarrollo y nunca en entornos de ejecución y/o de benchmarks.
  
- La versión anterior (sin API y en inglés) está disponible [aqui](https://github.com/VicDominguez/EnhanceNet-Code/tree/27c7f0659befd8aacdb76f0c612332269aa5a51e).

Para otras cuestiones, no dudes en enviarme un correo a [flugplatzcode@gmail.com](mailto:flugplatzcode@gmail.com).