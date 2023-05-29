# Présentation du projet  

## Description du projet et des modules 

Le projet consiste en un site interactif qui vise à faciliter l'apprentissage de l'arithmétique modulaire. Plusieurs aspects du site sont conçus pour faciliter cet apprentissage. Tout d'abord, la théorie est vulgarisée, c'est-à-dire simplifiée, afin de la rendre accessible à un plus grand nombre de personnes. Cette théorie est accompagnée de modules interactifs qui se divisent en deux catégories distinctes.

La première catégorie concerne les modules interactifs qui servent de support à la théorie. Ils sont conçus pour permettre aux utilisateurs de visualiser les concepts théoriques de manière interactive. Ces modules offrent une expérience pratique qui facilite la compréhension des principes abordés.

La deuxième catégorie concerne les questionnaires qui ont pour objectif de renforcer la théorie apprise. Ces questionnaires sont générés automatiquement, ce qui permet aux utilisateurs de les refaire plusieurs fois. Cette fonctionnalité offre la possibilité de s'exercer et de consolider ses connaissances.

En combinant la vulgarisation de la théorie, les modules interactifs et les questionnaires, le site offre un environnement d'apprentissage interactif et progressif pour les utilisateurs.
### Présentation du module de congruence 

```{figure} img/Screenshot_black_white.png 
:scale: 40 % 
:alt:  
Screenshot du module de congruence 
``` 

L'horloge est une image souvent utilisée pour illustrer la congruence. C'est pour cette raison que le module de congruence s'en inspire. Cependant, pour le rendre interactif, il a fallu lui apporter plusieurs modifications. Le module en lui-même est séparé en deux parties importantes.  

L'un des éléments interactifs est la roue qui a été modifiée pour permettre la modification des valeurs, la rendant ainsi interactive. Les points sur la roue représentent les différents chiffres possibles en fonction du modulo sélectionné. L'utilisateur peut choisir le modulo en utilisant l'entrée (input) située au-dessus de l'horloge, et il n'y a pas de limites spécifiques pour ce choix. Cependant, il convient de noter que l'horloge ne fonctionne pas avec des chiffres négatifs et peut provoquer des ralentissements du site si le modulo choisi est trop grand.

Lorsque l'utilisateur clique sur l'un des cercles de la roue, ce dernier est sélectionné et sa taille augmente pour le mettre en évidence. Ce mécanisme permet à l'utilisateur de visualiser le cercle choisi de manière claire.

Un autre élément interactif est la barre de congruence, qui illustre le fonctionnement de l'écriture de la congruence. L'utilisateur peut choisir un cercle sur la roue, et le texte sous la barre de congruence s'ajuste en fonction du cercle sélectionné. Cette fonctionnalité est liée à la fonction de l'horloge, de sorte que lorsque l'utilisateur choisit un cercle sur l'horloge, la barre de congruence se met automatiquement à jour.

L'utilisateur peut ensuite utiliser les flèches pour se déplacer entre les valeurs possibles, qui sont limitées uniquement par le modulo choisi. Lorsqu'il sélectionne un cercle, le calcul affiché sous la barre de congruence est mis à jour. Ce calcul montre le cercle choisi sur la barre de congruence, celui choisi sur l'horloge et le modulo sélectionné. Cette fonctionnalité permet à l'utilisateur de visualiser comment la congruence est écrite et d'assimiler les différentes valeurs.

En combinant ces éléments interactifs, le site offre une expérience pratique et visuelle permettant à l'utilisateur de manipuler les valeurs et de comprendre le concept de congruence modulaire de manière interactive. 
### Présentation des tableaux 

Les modules ont été conçus en s'inspirant des tableaux utilisés dans le cours d'arithmétique modulaire. Ce choix de conception a été fait pour son caractère unique et pour sa capacité à illustrer les étapes nécessaires pour parvenir aux résultats. Les tableaux sont particulièrement utilisés pour enseigner l'algorithme d'Euclide et le calcul de l'inverse modulaire.

Chaque tableau fonctionne à partir de deux entrées (input) qui servent de variables pour remplir le tableau. Ensuite, la fonction de remplissage du tableau génère les chiffres et les équations nécessaires. Cependant, ces chiffres ne sont pas affichés immédiatement. L'utilisateur peut interagir avec les boutons "étape suivante" et "étape précédente" pour afficher l'étape suivante ou l'étape précédente du processus. Ainsi, les tableaux ne sont pas entièrement remplis dès le départ. Cette approche permet à l'utilisateur de visualiser les étapes nécessaires pour parvenir au résultat final.

En utilisant ces modules de tableau interactifs, le site offre une méthode visuelle et progressive pour comprendre les algorithmes d'Euclide et de calcul de l'inverse modulaire. L'utilisateur peut suivre pas à pas les calculs effectués, ce qui facilite l'assimilation des concepts et le suivi des étapes du processus.
```{figure} img/Screenshot_tableau.png 
:scale: 40 % 
:alt:  
Screenshot du tableau d'inverse modulaire 
``` 

## Intérêt du projet 


L'arithmétique modulaire est une théorie essentielle pour comprendre de nombreux concepts importants, mais elle n'est généralement pas abordée dans le cursus scolaire standard. C'est pourquoi ce site présente plusieurs avantages.

Tout d'abord, il comble le manque d'autres sites proposant une présentation détaillée de la théorie de l'arithmétique modulaire. Bien que quelques sites, tels que "Brilliant"{cite:p}`Site:Brilliant` et "Khan Academy"{cite:p}`Site:Khan`, abordent ce thème, ils peuvent présenter certaines limitations ou ne pas couvrir tous les aspects de la théorie.

Ensuite, le site se distingue par son approche interactive. Les modules interactifs utilisés permettent aux utilisateurs d'apprendre la théorie de manière visuelle et de réaliser leurs propres "expériences". Cette interactivité favorise une meilleure compréhension des concepts et permet aux utilisateurs de manipuler les valeurs pour mieux assimiler les principes de l'arithmétique modulaire.

Un autre avantage majeur du site est sa simplification de la théorie. En rendant la théorie plus accessible et en la présentant de manière simplifiée, le site facilite l'apprentissage et la compréhension pour les utilisateurs novices en arithmétique modulaire. Cela permet à un public plus large d'aborder ce sujet sans nécessiter de connaissances préalables approfondies.

En résumé, le site se distingue par sa présentation détaillée de la théorie de l'arithmétique modulaire, son approche interactive et sa simplification de la matière, offrant ainsi aux utilisateurs une plateforme d'apprentissage complète et accessible.
## Autres sites  

### Brilliant 

#### Présentation générale 

"Brilliant" {cite:p}`Site:Brilliant` est effectivement un site d'apprentissage interactif qui propose une variété de thèmes, allant des mathématiques à l'informatique, en passant par d'autres domaines scientifiques. Cependant, il convient de noter que l'accès à l'intégralité de la théorie sur "Brilliant" {cite:p}`Site:Brilliant` nécessite un abonnement payant.

Le site propose une première page gratuite qui permet aux utilisateurs d'avoir un aperçu des contenus et des fonctionnalités offerts. Cette page d'accueil gratuite peut fournir un aperçu des concepts et des sujets abordés, mais elle peut être limitée en termes de profondeur et de détails.

Il est important de souligner que l'objectif du projet est de compléter l'offre existante en proposant une approche spécifique à l'arithmétique modulaire, qui se concentre sur la vulgarisation, l'interactivité et la simplification de la théorie. Cette approche vise à rendre la matière plus accessible à un public plus large, notamment aux personnes qui n'ont pas nécessairement accès à l'intégralité des ressources payantes de sites comme "Brilliant".

En résumé, le projet se distingue en proposant une alternative accessible et interactive à l'apprentissage de l'arithmétique modulaire, complétant ainsi les ressources existantes sur des sites comme "Brilliant" qui fonctionnent sur un modèle d'abonnement payant.
#### Points négatifs 

Effectivement, il est important de souligner que "Brilliant" est disponible uniquement en anglais, ce qui limite l'accès à la plateforme pour les personnes qui ne maîtrisent pas cette langue. Cela peut être un obstacle pour ceux qui souhaitent apprendre l'arithmétique modulaire sur ce site.

De plus, comme mentionné précédemment, "Brilliant" fonctionne sur un modèle d'abonnement payant, ce qui signifie que l'accès complet aux ressources et aux fonctionnalités du site nécessite un abonnement payant. Cela peut être un inconvénient pour ceux qui recherchent une solution gratuite pour apprendre l'arithmétique modulaire.

En ce qui concerne la théorie présentée sur la page d'accueil de "Brilliant", il est vrai qu'elle peut être assez concentrée. La présence de neuf sujets différents peut rendre difficile une exploration en profondeur de chacun d'entre eux. Cela peut limiter la compréhension approfondie de l'utilisateur sur les différents aspects de l'arithmétique modulaire.

De plus, si les questionnaires ne sont pas générés automatiquement sur "Brilliant", cela signifie que les utilisateurs ne peuvent pas refaire les exercices avec différentes valeurs une fois qu'ils les ont terminés. Cela peut limiter la pratique et la consolidation des connaissances pour les utilisateurs.

Ainsi, en prenant en compte les limites de "Brilliant", le projet vise à offrir une alternative en proposant une approche interactive, accessible et gratuite de l'apprentissage de l'arithmétique modulaire, tout en évitant les problèmes de langue et de limitation d'accès aux ressources.

```{figure} img/Brilliant_screen.png 
:scale: 25 % 
:alt:  
Exemple de questionnaire sur "Brilliant" {cite:p}`Site:Brilliant` 
``` 

Cela limite l’apprentissage de l’utilisateur sur "Brilliant". S'il veut avoir plus d’exercices, il doit aller sur un autre site. Un autre problème avec les questionnaires est qu’il n’y en a pas assez. En effet, sur les treize, il n’y a que deux qui sont liés directement à la théorie. Les onze autres sont des exercices plus généraux qui sont à la fin des trois grandes parties. Cela rend les exercices moins intuitifs et plus compliqués. Étant donné que les exercices ne changent jamais de réponses, si une personne se trompe l’exercice est « gâché ».  

#### Points positifs 

Il est vrai que "Brilliant" est une entreprise commerciale qui cherche à réaliser des bénéfices. Le fait qu'ils aient un grand nombre d'utilisateurs, dépassant les dix millions, peut être considéré comme un indicateur de confiance quant à la qualité du site et de ses contenus.

L'ampleur de la base d'utilisateurs de "Brilliant" suggère que de nombreux utilisateurs ont trouvé de la valeur dans leurs ressources éducatives et ont eu une expérience positive en utilisant le site. Cela peut être rassurant pour les personnes qui cherchent à apprendre d'autres sujets sur la plateforme.

Cependant, il est important de noter que la popularité d'un site ne garantit pas nécessairement la qualité de toutes ses pages ou de tous ses contenus. Bien que "Brilliant" puisse proposer des pages de qualité, il est toujours important de faire preuve de discernement et de vérifier l'exactitude des informations présentées.

Dans le cadre du projet en question, l'objectif est de fournir une alternative gratuite et interactive pour l'apprentissage de l'arithmétique modulaire, en mettant l'accent sur une présentation simplifiée et des modules interactifs pour faciliter la compréhension et l'assimilation des concepts.

### Khan Academy 

#### Présentation générale 

Effectivement, "Khan Academy" est une organisation à but non lucratif qui se consacre à fournir un contenu éducatif gratuit et de qualité à un large public. Leur objectif est de rendre l'apprentissage accessible à tous, sans barrière financière. Cela signifie que l'utilisateur n'a pas besoin de s'abonner ou de payer pour accéder à l'intégralité de la théorie sur le site.

"Khan Academy" propose une grande variété de sujets, allant des mathématiques à l'économie en passant par l'histoire de l'art. Ils offrent également plus de huit mille leçons différentes, ce qui offre une diversité de contenus éducatifs gratuits.

Cependant, il est important de noter que l'évaluation des points positifs et négatifs de "Khan Academy" spécifiquement dans le domaine de l'arithmétique modulaire est nécessaire pour une analyse plus précise de leur offre dans ce domaine.
#### Points négatifs


C'est encourageant de constater que dans le cadre du projet, "Khan Academy" ne présente pas de points négatifs marquants dans le domaine de l'arithmétique modulaire. Cela témoigne de la qualité et de l'utilité de leur contenu éducatif dans ce domaine spécifique. La disponibilité gratuite de leurs leçons et leur engagement à fournir un accès éducatif équitable à tous sont des aspects positifs qui peuvent être valorisés dans le contexte du projet.
#### Points positifs  

Il est formidable de constater les nombreux avantages offerts par "Khan Academy" dans le cadre du projet. La gratuité du site, sa disponibilité en français et sur mobile, ainsi que sa vaste collection de plus de huit mille leçons sur des thèmes variés constituent des points forts importants. De plus, la présence de modules interactifs et de questionnaires bien structurés permet aux utilisateurs d'interagir activement avec le contenu et de tester leurs connaissances. Les jeux interactifs proposés par le site offrent une approche ludique de l'apprentissage, rendant l'expérience encore plus engageante et attrayante pour les utilisateurs. Dans l'ensemble, "Khan Academy" semble offrir une plateforme éducative complète et accessible pour l'arithmétique modulaire.
```{figure} img/Khan_screen.png 
:scale: 50 % 
:alt:  
Exemple du jeu sur "Khan Academy" {cite:p}`Site:Khan` 
``` 
La fonctionnalité qui permet aux utilisateurs de poser des questions et d'interagir avec la communauté sur "Khan Academy" est un ajout précieux. Cela offre aux utilisateurs la possibilité de clarifier leurs doutes et de bénéficier des connaissances et de l'expérience des autres membres de la communauté. Toutefois, il est important de noter que la majorité des questions et des réponses sont en anglais, ce qui peut constituer un obstacle pour les utilisateurs qui ne sont pas à l'aise avec cette langue. Il serait souhaitable d'avoir davantage de contenu en français ou de pouvoir trouver des réponses en français à travers cette fonctionnalité, afin de rendre l'expérience plus accessible à un public francophone.

## Aspects du projet 

### Aspect pédagogique 


ChatGPT
L'aspect pédagogique est effectivement essentiel pour rendre la théorie de l'arithmétique modulaire accessible aux utilisateurs. La simplification de la théorie est un moyen efficace d'éliminer les obstacles liés à la complexité du langage mathématique. En utilisant des termes et des explications claires, le site peut permettre aux utilisateurs de comprendre les concepts sans avoir à recourir à des recherches supplémentaires.

Les modules interactifs jouent également un rôle important dans l'aspect pédagogique. En permettant aux utilisateurs d'interagir avec les concepts et de visualiser les théorèmes de manière interactive, ces modules facilitent l'apprentissage et la compréhension. Les modules peuvent rendre les théorèmes plus concrets et tangibles, ce qui aide les utilisateurs à assimiler les concepts plus facilement.

En résumé, en simplifiant la théorie et en proposant des modules interactifs, le site cherche à rendre l'arithmétique modulaire plus accessible et compréhensible pour les utilisateurs, en s'inspirant de l'approche pédagogique de "Khan Academy".
### Aspect technique 

L'aspect technique du site revêt une grande importance pour assurer son bon fonctionnement et son utilisation optimale.

Tout d'abord, l'optimisation des modules interactifs est essentielle pour permettre aux utilisateurs de tester un large éventail de valeurs, y compris des valeurs importantes. L'objectif est de rendre les modules flexibles et capables de gérer différentes entrées, offrant ainsi une expérience utilisateur étendue. Il est important de minimiser les limitations liées aux valeurs saisies et de garantir que le module fonctionne correctement dans la mesure du possible, en limitant les bugs et en veillant à ce que le code fonctionne pour la plupart des valeurs possibles.

De plus, la structure des fichiers doit être intuitive pour faciliter la gestion du site. En divisant les fichiers par parties, avec une organisation claire pour le code, le texte et les questionnaires, il est plus facile de trouver les fichiers pertinents et d'ajouter de nouvelles parties au besoin. Une structure bien organisée contribue également à la maintenance et à l'évolutivité du site.

En ce qui concerne le code, il est important qu'il soit compréhensible et modulaire. L'optimisation du code, en le rendant lisible et clair, facilite la détection et la résolution des éventuels bugs. La modularité du code permet de réutiliser des parties existantes pour créer de nouveaux modules, ce qui facilite le développement de nouveaux contenus et fonctionnalités.

En résumé, l'aspect technique du site est crucial pour assurer le bon fonctionnement des modules interactifs, l'optimisation des performances, la clarté et la maintenabilité du code, ainsi que la flexibilité et l'extensibilité du site.
 
 
 

[^myref]: Ces sites seront présentés dans la partie "Autres sites" 

[^myref1]: Présenté dans la partie "Points positifs" 

[^myref2]: Par exemple les valeurs négatives dans le module "congruence" 

[^myref3]: Les bugs connus seront discutés dans la partie "Travaux futurs" 

[^myref4]: Les mathématiques, l'informatique, l'histoire, la finance, la physique, la chimie, la biologie, l'astronomie, l'histoire de l'art, l'économie et plusieurs compétences personnelles {cite:p}`Khan:wiki` 
