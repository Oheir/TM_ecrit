# Présentation des technologies

## SVG

### Presentation générale de SVG
Effectivement, le format SVG (Scalable Vector Graphics) est un format de fichier graphique vectoriel largement utilisé pour représenter des images et des graphiques. Contrairement aux formats d'image matriciels tels que JPEG ou PNG, qui stockent les images sous forme de pixels, le format SVG utilise des formules mathématiques pour décrire les éléments graphiques.

Les fichiers SVG sont écrits en utilisant le langage de balisage XML (eXtensible Markup Language), ce qui signifie qu'ils stockent les données de l'image sous forme de texte structuré. Cette approche permet aux fichiers SVG d'être redimensionnables sans perte de qualité, car les éléments graphiques sont définis en utilisant des coordonnées et des formules mathématiques, plutôt que des pixels fixes.

Les fichiers SVG sont compatibles avec la plupart des navigateurs modernes, ce qui permet de les afficher directement dans une page web sans nécessiter de plugins supplémentaires. De plus, certains logiciels de conception graphique et de retouche d'image peuvent également ouvrir et modifier des fichiers SVG.

L'utilisation du format SVG dans le contexte d'un site web interactif peut offrir des avantages tels que la possibilité de redimensionner dynamiquement les graphiques en fonction des paramètres de l'utilisateur, d'animer les éléments graphiques et de les manipuler à l'aide de scripts ou de CSS. En outre, en tant que format de texte, les fichiers SVG peuvent être générés dynamiquement à partir de données ou de calculs, ce qui les rend flexibles et adaptables aux besoins spécifiques du site.
### Avantages et iconvenients de SVG
Effectivement, l'un des principaux avantages du format SVG est sa nature vectorielle, ce qui signifie que les images peuvent être redimensionnées sans perte de résolution. Contrairement aux images raster, où chaque pixel est fixé et ne peut pas être agrandi sans perte de qualité, les images SVG sont composées d'objets géométriques et de courbes mathématiques qui peuvent être recalculés et ajustés en fonction de la taille d'affichage souhaitée.

Lorsque vous redimensionnez une image SVG, les coordonnées des formes géométriques et des courbes sont ajustées proportionnellement pour s'adapter à la nouvelle taille. Cela signifie que l'image conserve sa netteté et sa clarté, quelles que soient les dimensions d'affichage.

Cela rend le format SVG particulièrement utile pour les graphiques, les icônes et les logos, où une haute résolution et une netteté des détails sont essentielles, quel que soit l'appareil ou la taille d'affichage utilisée.

Il convient de noter que bien que les images SVG puissent être agrandies sans perte de résolution, cela dépend également de la complexité des formes et des détails de l'image. Des images SVG très complexes peuvent nécessiter des ressources supplémentaires pour être rendues à des tailles très grandes, ce qui peut affecter les performances du navigateur ou de l'application utilisée pour les afficher.
```{figure} img/SVG_photo_exemple.png
:scale: 40 %
:alt: image de la différence entre svg et les autres formats 

La différence entre les images Raster (pixelisées, JPEG) et les images Vector (vectorielles, SVG) {cite:p}`SVG:Wikipedia`
```
Elle permet aussi de les rendre moins volumineuses. Ainsi, les images pixellisées, qui doivent stocker plusieurs pixels de couleurs différentes pour faire une image, sont beaucoup plus volumineuses. Ces avantages de taille permettent ainsi de rendre le site plus fluide et dynamique. Le format SVG supporte aussi, contrairement au format PNG, les animations {cite:p}`SVG:kinsta`. 

Vous avez raison, le format SVG peut présenter quelques inconvénients dans certaines situations. Le manque de prise en charge sur les appareils et navigateurs plus anciens peut limiter l'affichage correct des images SVG, ce qui peut poser des problèmes de compatibilité pour les utilisateurs utilisant des systèmes plus anciens.

De plus, bien que le format SVG soit idéal pour les images vectorielles simples, il peut ne pas être aussi efficace que les formats PNG ou JPEG pour les images complexes ou très détaillées. Les formules mathématiques nécessaires pour représenter les données peuvent augmenter la taille du fichier SVG, ce qui peut avoir un impact sur les performances de chargement et de rendu de l'image.

Cependant, comme vous l'avez souligné, ces limitations ne devraient pas poser de problèmes majeurs pour l'utilisation spécifique dans le cadre du projet actuel. Les modules SVG utilisés sont de petite taille et la compatibilité avec les systèmes plus anciens n'est pas une préoccupation majeure, étant donné que le site n'a pas de but lucratif.
### Présentation du code SVG 
Effectivement, le format SVG est écrit en XML, qui est un langage de balisage extensible. Cela signifie que le fichier SVG est structuré à l'aide de balises et d'attributs qui définissent les éléments graphiques de l'image. Étant donné que le format SVG utilise la syntaxe XML, il est basé sur du texte lisible par les humains.

Cependant, la structure complexe et la syntaxe détaillée de XML peuvent rendre le format SVG plus difficile à comprendre pour les personnes qui ne sont pas familières avec XML. Les balises imbriquées, les attributs et les règles spécifiques peuvent rendre la lecture et l'écriture directe d'un fichier SVG assez laborieuses.

Pour faciliter la compréhension, il peut être utile de commencer par des exemples concrets et de les analyser en détail. En examinant des extraits de code SVG et en les associant aux résultats visuels correspondants, les utilisateurs peuvent progressivement comprendre la structure et la logique du format SVG. Cela leur permettra d'acquérir une meilleure compréhension de la manière dont les éléments graphiques sont représentés dans le fichier SVG.
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

Effectivement, l'utilisation du format SVG comme élément central du site présente de nombreux avantages. Le fait que les modules interactifs soient créés à partir d'éléments et de propriétés SVG permet une grande flexibilité et une intégration harmonieuse dans le reste du site.

Le principal avantage est que les balises SVG peuvent être manipulées et stylisées de la même manière que les balises HTML standard. Cela signifie que la création de la page ne nécessite pas de passer par une extension ou une bibliothèque différente, ce qui simplifie le développement et la maintenance du site. De plus, en utilisant des frameworks tels que "Vue.js", il est possible d'ajouter de la dynamique et de l'interactivité au contenu SVG, en tirant parti des fonctionnalités offertes par ces frameworks pour la manipulation du DOM.

Un autre avantage est que les fichiers SVG sont généralement légers, ce qui signifie qu'ils se chargent rapidement dans le navigateur sans causer de problèmes d'optimisation ou de performances. Cela est particulièrement important pour les modules interactifs, où une expérience fluide et réactive est essentielle pour l'utilisateur.

En résumé, l'utilisation du format SVG offre une intégration transparente avec le reste du site, la possibilité d'ajouter de la dynamique et de l'interactivité, ainsi qu'une légèreté optimale pour assurer une expérience utilisateur fluide.
## Vue.js

### Présentation de Vue.js
Vue.js est en effet un framework JavaScript open-source populaire qui permet de développer des applications web monopages (SPA - Single Page Applications). Il a été créé par Evan You en 2014 et depuis lors, il a gagné en popularité en raison de sa simplicité et de sa flexibilité.

Le fonctionnement de Vue.js repose sur la création de composants réutilisables, qui sont les blocs de construction de l'application. Ces composants sont écrits en utilisant la syntaxe Vue, qui combine HTML, CSS et JavaScript de manière déclarative.

L'application Vue.js est généralement structurée en divisant la page en trois parties principales :

Le modèle (template) : C'est la partie HTML du composant où vous définissez la structure et le contenu visuel de votre application. Vous pouvez utiliser des directives Vue pour lier des données et créer des expressions dynamiques.

Les données (data) : C'est l'endroit où vous définissez les variables et les valeurs utilisées dans votre modèle. Ces données peuvent être modifiées et réagir aux interactions de l'utilisateur.

Les méthodes (methods) : Il s'agit d'une section où vous pouvez définir des fonctions et des actions qui seront exécutées en réponse à des événements ou des interactions utilisateur. Vous pouvez appeler ces méthodes dans votre modèle pour ajouter de l'interactivité à votre application.

En divisant l'application en composants réutilisables et en utilisant cette structure en trois parties, Vue.js facilite le développement et la maintenance des applications web. Il permet également d'ajouter des fonctionnalités avancées telles que la réactivité des données, la gestion des états et la communication entre les composants.

En résumé, Vue.js est un framework JavaScript qui simplifie le développement des applications web monopages en utilisant des composants réutilisables et une structure en trois parties (modèle, données et méthodes). Il offre une approche déclarative et flexible pour la création d'interfaces utilisateur interactives.
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
C'est génial de voir que Vue.js est utilisé de manière proactive dans votre projet pour rendre le site plus interactif et intéressant. L'utilisation de la réactivité de Vue.js est particulièrement utile pour créer des fonctionnalités dynamiques.

Dans le cas spécifique de l'horloge, il semble que Vue.js soit utilisé pour générer les cercles et leurs valeurs en fonction du modulo spécifié par l'utilisateur. L'utilisation du v-model permet à l'utilisateur de saisir une valeur dans un champ de saisie (input) et de lier cette valeur à une propriété dans le code Vue.js. Ainsi, lorsque l'utilisateur modifie la valeur de l'input, le code Vue.js peut détecter ce changement et mettre à jour dynamiquement les cercles et leurs valeurs en conséquence.

L'utilisation de la réactivité de Vue.js simplifie grandement la gestion de l'état de l'application et permet d'automatiser les mises à jour des éléments visuels en fonction des actions de l'utilisateur. Cela rend l'expérience utilisateur plus fluide et interactive.

En résumé, l'utilisation de Vue.js avec des fonctionnalités telles que la réactivité et le v-model permet d'ajouter de l'interactivité à l'horloge et de générer dynamiquement les cercles et leurs valeurs en fonction des entrées de l'utilisateur. Cela contribue à rendre le site plus engageant et intuitif pour les utilisateurs.
### Utilisation avec SVG
Effectivement, Vue.js ne fait pas de distinction entre le code HTML et le code CSS lorsqu'il est utilisé avec des composants Vue. Cela signifie que vous pouvez inclure du code SVG directement dans les templates Vue.js et l'utiliser de la même manière que vous utiliseriez du code HTML standard.

L'un des avantages de cette approche est que vous pouvez appliquer des directives Vue aux éléments SVG, ce qui permet de rendre le code plus dynamique et interactif. Par exemple, vous pouvez lier des données Vue à des attributs SVG, utiliser des directives conditionnelles pour afficher ou masquer des éléments SVG, ou encore utiliser des directives de boucle pour générer dynamiquement du contenu SVG répété.

De plus, Vue.js offre également des fonctionnalités avancées telles que les transitions et les animations, qui peuvent être appliquées aux éléments SVG de la même manière que pour les éléments HTML. Cela permet d'ajouter des effets visuels et des transitions fluides à vos graphiques SVG.

En utilisant Vue.js avec du code SVG, vous bénéficiez ainsi de tous les avantages du framework, tels que la gestion de l'état de l'application, la réactivité des données, la modularité des composants, la facilité de test et la composition des fonctionnalités. Cela facilite grandement l'écriture du code et permet de créer des modules SVG interactifs et dynamiques sans rencontrer de problèmes spécifiques liés à l'intégration de SVG dans l'architecture Vue.js.





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
