# Présentation des technologies

## SVG

### Presentation générale de SVG
Le format SVG, une abréviation de "Scalable Vector Graphics", est un format de fichier vectoriel qui stocke des images avec des formules mathématiques. Les fichier SVG sont écrits en format XML, ainsi ils stockent les données en tant que texte {cite:p}`SVG:adobe`. Les fichiers de format SVG ont comme extension de fichier ".svg". Cette extension peut être lue par la plupart des navigateurs populaires et modernes, et peut être ouverte par certaines applications [^myref]. 
### Avantages et iconvenients de SVG
Grâce à la manière dont les images sont stockées dans le format SVG,[^myref1] l'image peut être agrandie et rétrécie sans perte de résolution.
```{figure} img/SVG_photo_exemple.png
:scale: 40 %
:alt: image de la différence entre svg et les autres formats 

La différence entre les images Raster (pixelisées, JPEG) et les images Vector (vectorielles, SVG) {cite:p}`SVG:Wikipedia`
```
Elle permet aussi de les rendre moins volumineuses. Ainsi, les images pixellisées, qui doivent stocker plusieurs pixels de couleurs différentes pour faire une image, sont beaucoup plus volumineuses. Ces avantages de taille permettent ainsi de rendre le site plus fluide et dynamique. Le format SVG permet supporte aussi, contrairement au format PNG, les animations{cite:p}`SVG:kinsta`. 

SVG a cependant plusieurs inconvénients. 
Comme, par exemple, le fait que le format ne soit pas supporté sur les appareils et navigateurs plus anciens {cite:p}`SVG:kinsta`. Les formules mathématiques utilisées pour stocker les données sont bien pour les images qui ne demandent pas beaucoup de détails, mais pour des images plus précise le format PNG ou JPEG est généralement plus approprié {cite:p}`SVG:adobe`. 

Cependant cela ne devrait pas posé de problèmes pour l'utilisation qui en est fait pour le projet actuel. En effet les modules utilisants SVG sont assez petits. Le problème de compatibilité avec les systèmes plus anciens n'est pas un problème car le site n'est pas fait pour avoir un but lucratif.
### Présentation du code SVG 
Le format SVG est écrit en XML, abrévation de "Extensible Markup Language", ce qui lui donne son écriture sous forme de texte, mais qui le rend aussi plus dur à comprendre. C'est pour cette raison qu'il faut commencer par des exemples.

viewbox :
Pour lancer une "fenêtre" svg il faut utiliser l'attribut "viewbox"
```{figure} img/Screenshot_viewbox1.png
:scale: 60 %
:alt:  
Ce code créé une viewbox de dimensions 50x50 est y affiche un cercle [^myref2]
```
La syntaxe de viewbox est "min_x min_y width height". Cette fenêtre nous permettra par la suite d'afficher les formes SVG dans la fenêtre ouverte. Viewport est donc nécessaire pour afficher tout code SVG est et donc nécessaire pour chaque page du site.

Circle : Permet de faire un cercle
```{figure} img/Screenshot_cercle1.png
:scale: 60 %
:alt:
image du cercle créé avec la viewbox [^myref2]
```
La syntaxe du cercle est "coordonnée_x_du_centre coordonnée_y_du_centre rayon". Le cercle est une partie importante du site car le module pour montrer la congruence est créé à partir de cet élément.

text : Permet d'écrire du texte dans la fenêtre SVG
 ```{figure} img/Screenshot_text.png
:scale: 60 %
:alt:
code permettant d'écrire Example dans la viewbox
```
La syntaxe de text est "centre_x centre_y". L’élément text est important car dans une viewbox le text HTML ne peut pas être affiché. Il faut donc écrire ce qui normalement est écrit grâce à des balises "h1" ou "h2"avec l’élément text.
### Utilisation de SVG dans le projet
SVG est une partie centrale du site. En effet les modules interactifs sont créés à partir des éléments et propriétés SVG.

## Vue.js

### Présentation de Vue.js
Vue.js est un framework javascript qui permet de construire des sites web monopages, c'est à dire que le site est accesible grâce à seulement une seule page. Cela permet de rendre l'expérience de l'utilisateur plus agréable et de limité le temps de chargement nécessaire quand on change de page. Vue.js permet aussi de rendre les trois fichier, "HTML, "CSS" et "Javascript", inutiles car il permet au développeur web de mettre tout ces languages de programmation sur une page avec ses composants. Le framework ajoute aussi des fonctions qui ne sont pas dans les languages mentionnés avant, par exemple "@click" qui permet de faire changer l'objet à chaque click ,quelque chose qui n'est pas possible avec javascript, ce qui permet de rendre le code plus facile à écrire et évite de faire des fonctions trop compliqués. Ainsi un site fait avec Vue est réactif et se transforme avec les "inputs" de l'utilisateur, ce qui permet de rendre le site plus intéractif.
### Utilisation de Vue.js dans le projet
Dans le projet Vue.js est utilisé comme framework et ses fonctionnalitées sont utilisées pour rendre le site plus intéractif et intéressant. La réactivité est, par exemple, utilisée dans l'horloge pour générer les cercles et leur valeurs celon le modulu indiqué pr l'utilisateur grâce à ce qu'ils appelent "v-model" qui donnet un nom à un "input" fait par l'utilisateur et nous permet de le reprendre dans le code plus tard. 


[^myref]: Tel que Adobe Illustrator ou Inkscape {cite:p}`SVG:application-utilisable`
[^myref1]: sous forme de formules mathématiques
[^myref2]: code utilisé pour l'affichage du cercle noir,centré, et avec un rayon d'une valeur de 5 