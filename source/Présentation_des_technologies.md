# Présentation des technologies

## SVG

### Presentation générale de SVG
Le format SVG, une abréviation de "Scalable Vector Graphics", est un format de fichier vectoriel qui stocke des images avec des formules mathématiques. Les fichiers SVG sont écrits en format XML, ainsi, ils stockent les données en tant que texte {cite:p}`SVG:adobe`. Les fichiers au format SVG ont comme extension de fichier ".svg". Cette extension peut être lue par la plupart des navigateurs populaires et modernes, et peut être ouverte par certaines applications [^myref]. 
### Avantages et iconvenients de SVG
Grâce à la manière dont les images sont stockées dans le format SVG,[^myref1] l'image peut être agrandie et rétrécie sans perte de résolution.
```{figure} img/SVG_photo_exemple.png
:scale: 40 %
:alt: image de la différence entre svg et les autres formats 

La différence entre les images Raster (pixelisées, JPEG) et les images Vector (vectorielles, SVG) {cite:p}`SVG:Wikipedia`
```
Elle permet aussi de les rendre moins volumineuses. Ainsi, les images pixellisées, qui doivent stocker plusieurs pixels de couleurs différentes pour faire une image, sont beaucoup plus volumineuses. Ces avantages de taille permettent ainsi de rendre le site plus fluide et dynamique. Le format SVG supporte aussi, contrairement au format PNG, les animations {cite:p}`SVG:kinsta`. 

SVG a cependant plusieurs inconvénients.
Comme, par exemple, le fait que le format ne soit pas supporté sur les appareils et navigateurs plus anciens {cite:p}`SVG:kinsta`. Les formules mathématiques utilisées pour stocker les données sont bien pour les images qui ne demandent pas beaucoup de détails, mais pour des images plus précise le format PNG ou JPEG est généralement plus approprié {cite:p}`SVG:adobe`.

Cependant, cela ne devrait pas poser de problèmes pour l'utilisation qui en est fait pour le projet actuel. En effet, les modules utilisant SVG sont assez petits. Le problème de compatibilité avec les systèmes plus anciens n'est pas un problème, car le site n'est pas fait pour avoir un but lucratif.
### Présentation du code SVG 
Le format SVG est écrit en XML, abréviation de "Extensible Markup Language", ce qui lui donne son écriture sous forme de texte, mais qui le rend aussi plus dur à comprendre. C'est pour cette raison qu'il faut commencer par des exemples.
`viewbox` :
Pour lancer une "fenêtre" svg il faut utiliser l'attribut "viewbox"
```{code-block} HTML
<template>
    <svg viewBox="0 0 50 50">
        <circle cx="50%" cy="50%" r="5" fill="black" />
    </svg>
</template>
```
La syntaxe de `viewbox` est "min_x min_y width height". Cette fenêtre nous permettra par la suite d'afficher les formes SVG dans la fenêtre ouverte. Viewport est donc nécessaire pour afficher tout code SVG est et aussi pour chaque page du site.

Circle : Permet de faire un cercle
```{code-block} HTML
<circle cx="50" cy="50" r="2">
```
La syntaxe du cercle est "coordonnée_x_du_centre coordonnée_y_du_centre rayon". Le cercle est une partie importante du site car le module pour montrer la congruence est créé à partir de cet élément.

text : Permet d'écrire du texte dans la fenêtre SVG
 ```{code-block} HTML
<template>
    <svg viewbox="0 0 100 100">
        <text x="50" y="50"> Exemple </text>
    </svg>
</template>
```
La syntaxe de text est « centre_x centre_y ». L’élément text est important car dans une viewbox le text HTML ne peut pas être affiché. Il faut donc écrire ce qui normalement est écrit grâce à des balises « h1 » ou « h2 » avec l’élément text. 
### Utilisation de SVG dans le projet
SVG est la partie centrale du site. En effet les modules interactifs sont créés à partir des éléments et propriétés SVG. Les désavantages du format ne posent aucun problème pour le site. Par exemple, les modules sont légers et il n’y a donc pas de problèmes d’optimisation. Un des avantages utilisé pour le site est le fait que les balises SVG ne fonctionnent pas différemment de balises HTML. Cela permet donc de créer la page sans avoir à passer par une extension ou une librairie différente. Cela permet aussi d’utiliser tous les avantages de "Vue.js". Comme par exemple le fait que SVG est considéré comme du code HTML standard et donc donc d'ajouter de la dynamique au site.
## Vue.js

### Présentation de Vue.js
Vue.js est un framework open-source javascript qui permet de construire des sites web monopages [Tci]. Vue.js a étécréé par “Evan You [Tci]” en 2014. Ce framework remplace les trois fichiers3et les mets sur une page. Cette page estdivisée en trois parties.
 ```{code-block} HTML
Exemple de fichier Vue.js

<template>
    <h1class="text">hello</h1>
</template>

<script>
export default{
    name: 'HelloWorld',
    props: {
        msg: String
    }
}
</script>

<style>
.text{
    color:black
    }
</style>
```
Chaque partie remplace un type de fichier différent[^myref3]. Vue.js est réactif. C’est à dire que le site peut changer selon les inputs de l’utilisateur. Cette fonctionnalité est importante pour le site.
#### v-model
 ```{code-block} HTML
<template>
    <inputclass="input" v-model="a">
</template>

<script>
export default{
    name: 'Tableauinverse',
    props: {
        msg: String}
    ,data() {
        return{
            a: 167,}
        }
    }
</script>
```
v-model permet de lier une valeur à un nom de variable. Quand l’utilisateur change l’inputla variable va aussichanger. Cette variable peut ensuite être utilisée dans une fonction.
#### v-for
 ```{code-block} HTML
Ce code va afficher "i" dix fois

<template>
    <h1 v-for="i in range(10)> i </h1>
</template>
```
v-for fait la même chose que for (let i = 0; i < 11 ; i++){}. Cela permet de faire des for loops sans avoir à faire des fonctions différentes et rendre le code moins imposant.
#### v-on
 ```{code-block} HTML
 À chaque "click" le texte va augmenter de 1

<template>
    <h1 @click="i++"> {{i}} </h1>
</template>
```
v-on peut être remplacé par@puit l’évènement que l’on veut. Pour chaque évènement javascript il existe un équivalent @ + évènement. Cette propriété est intéressante pour plusieurs raisons. Premièrement, elle permet de simplifierle code. Comme tous les évènements javascript marchent avecv-on, il est facile d’intégrer ces évènements dans “Vue.js”. Deuxièmement, elle, comme la majorité des fonctions Vue.js est interactive. Elle ré-évalue les valeurs uti-lisées dans la fonction à chaque évaluation. Cela permet de ne pas avoir à rajouter une fonction non nécessaire au code.

#### {{variable}}
 ```{code-block} HTML
Ce code va afficher la valeur de "i"

<template>
    <h1> {{i}} </h1>
</template>
```
{{}} sert  à  retourner  la  valeur  de  la  variable  utilisée.  Cette  fonction  est  très  utile.  Elle  permet,  par  exemple,  deretourner la valeur d’une fonction dans une autre fonction. Ce qui permettra ensuite de l’utiliser comme variable. Ellepeut aussi être utilisé pour faire du texte.
### Utilisation de Vue.js dans le projet
Dans le projet, Vue.js est utilisé comme Framework et ses fonctionnalités sont utilisées pour rendre le site plus interactif intéressant. La réactivité est, par exemple, utilisée dans l’horloge pour générer les cercles et leurs valeurs selon le modulo indiqué par l’utilisateur grâce à ce qu’ils appellent v-model qui donne un nom à un “input” fait par l’utilisateur et nous permet de le reprendre dans le code plus tard.
### Utilisation avec SVG
“Vue.js” ne fait aucune différence entre du code HTML et du code CSS. C’est à dire que le code SVG marche avectoute  les  fonctionnalités  Vue.js.  Cela  permet  de  faciliter  l’écriture  du  code.  Les  modules  SVG  peuvent  donc  êtreconstruits avec tous les avantages de Vue.js sans problèmes.
```{code-block} HTML
Exemple de code SVG où la propriété `{{variable}}` est utilisée

<text
x="50"
y="50"
:transform="
`translate(${text_right[1] + 2} ${-33 + 10*i})`">
    {{remplissage_calcul[1][i + 1]}}
</text>
```
[^myref]: Tel que Adobe Illustrator ou Inkscape {cite:p}`SVG:application-utilisable`
[^myref1]: sous forme de formules mathématiques
[^myref2]: "fill" permettra d'écrire le texte en blanc. "font-size" permet de changer la taille du text. "transform" permet de changer la position du texte
[^myref3]: '<template>' remplace le fichier HTML,<script>le fichier Javascript et<style>le fichier CSS
