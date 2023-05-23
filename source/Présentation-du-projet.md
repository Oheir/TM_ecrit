# Présentation du projet  

## Description du projet et des modules 

Le projet est un site interactif visant à faire apprendre l’arithmétique modulaire. L’apprentissage est facilité grâce à plusieurs aspects du site. Premièrement, la théorie est vulgarisée. C’est-à-dire qu’elle est simplifiée. Cela permet d’expliquer le sujet à un plus grand nombre de personnes. Cette théorie est accompagnée par des modules. Ces modules sont séparés en deux classes. La première, les modules interactifs, servent de support à la théorie. Dans ce but, ils sont utilisés pour permettre aux utilisateurs de visualiser la théorie. La deuxième catégorie, les questionnaires, permet de renforcer la théorie apprise. Les questionnaires ont plusieurs caractéristiques ; la première étant d’être générée automatiquement. Cela permet à l’utilisateur de le refaire plusieurs fois.  
### Présentation du module de congruence 

```{figure} img/Screenshot_black_white.png 
:scale: 25 % 
:alt:  
Screenshot du module de congruence 
``` 

L'horloge est une image souvent utilisée pour illustrer la congruence. C'est pour cette raison que le module de congruence s'en inspire. Cependant, pour le rendre interactif, il a fallu lui apporter plusieurs modifications. Le module en lui-même est séparé en deux parties importantes.  

La première est la roue en elle-même. Elle a été changée pour permettre de modifier les valeurs et ainsi de la rendre interactive. Les points représentent les différents chiffres possibles avec le modulo sélectionné. Le modulo est choisi grâce à l'`input` au-dessus de l'horloge et ne possède pas de limites. Cependant, l'horloge ne marche pas avec des chiffres négatifs et à tendance à stopper les services du site si le modulo est trop grand. Ensuite, l'utilisateur peut cliquer sur un cercle pour le sélectionner. Quand il est sélectionné, le cercle grandit. Ce qui permet de le mettre en évidence. Le deuxième, la barre de congruence, permet de montrer comment l'écriture marche. L'utilisateur peut choisir un cercle. Ensuite, le texte en dessous de la barre s'ajustera en fonction du cercle choisi. Cette fonction est liée à la fonction de l'horloge. Quand l'utilisateur choisi un cercle sur l'horloge, la barre se met à jour automatiquement. L'utilisateur peut ensuite utiliser les flèches pour se déplacer entre les valeurs possibles. Ces valeurs ne sont limitées que par le modulo choisi. Ensuite, une fois qu'il choisit un cercle, le calcul situé en dessous de la barre se met à jour. Ce calcul montre le cercle de la barre choisi, celui de l'horloge et le modulo choisi. Cela permet à l'utilisateur de visualiser comment la congruence s'écrit et d'assimiler les valeurs.  
### Présentation des tableaux 

Les modules ont été inspirés par les tableaux du cours d'AM. Ce design a été choisi car il est unique. Il permet de voir les étapes qui permettent d'arriver aux résultats. Ces tableaux sont utilisés pour enseigner l'algorithme d'Euclide et l'inverse modulaire.

Les tableaux fonctionnent grâce à deux `input` qui servent comme variables pour remplir le tableau. Ensuite, la fonction de remplissage de chaque tableau va générer les chiffres et équations nécessaires. Ces chiffres ne seront pas affichés tout de suite. L'utilisateur peut cliquer sur les boutons "étape suivante" et "étape précédente". Ces boutons permettent d'afficher la prochaine étape ou l'étape précédente. Ainsi, les tableaux ne sont pas remplis au début. Cela, permet de voir les étapes nécessaires pour arriver au résultat final. 
```{figure} img/Screenshot_tableau.png 
:scale: 40 % 
:alt:  
Screenshot du tableau d'inverse modulaire 
``` 

## Intérêt du projet 

La théorie de l’arithmétique modulaire est vitale pour comprendre plusieurs concepts importants. Cependant, elle n’est pas vue dans le cursus standard. Ainsi, le site à plusieurs intérêts. Le premier est le manque d’autre site présentant la théorie. Le thème de l’arithmétique modulaire est principalement présenté par deux sites, "Brilliant {cite:p}`Site:Brilliant`" et "Khan Academy {cite:p}`Site:Khan`"[^myref]. Un autre avantage est l’interactivité du site. En effet, le site utilise des modules interactifs. Ces modules permettent à l’utilisateur d’apprendre la théorie visuellement et de faire leurs propres « expériences ». Ensuite, la théorie est simplifiée. Cela permet de faciliter l’apprentissage.  
## Autres sites  

### Brilliant 

#### Présentation générale 

"Brilliant {cite:p}`Site:Brilliant`" est un site d'apprentissage interactif. Ce site propose plusieurs thèmes. Ceux-ci vont des mathématiques à l'informatique, mais ils restent tous dans le domaine des sciences. Cependant, tout le monde n'a pas accès à toute la théorie. En effet, "Brilliant" fonctionne avec un système d’abonnement. C'est pourquoi l'analyse du site se concentra sur la première page, qui est gratuite.  

#### Points négatifs 

Pour commencer, "Brilliant" n’est disponible qu’en anglais. Cela veut dire que si une personne ne connaissant pas bien l’anglais cherche à apprendre l’arithmétique modulaire sur "Brilliant", il ne peut pas. Un autre désavantage est que, comme dit dans l’introduction, "Brilliant" est un site payant. C’est-à-dire que sans payer un abonnement, l’utilisateur n’a accès qu’à la première partie de la théorie. Cependant, cela peut aussi présenter un avantage [^myref1].

La théorie de la page d’accueil a aussi plusieurs problèmes. Pour commencer, la théorie est très concentrée. La page contient neuf sujets différents. Ces sujets vont de la congruence à la résolution de problèmes. Cela ne permet pas d’aller dans les détails, ce qui limite l’apprentissage de l’utilisateur. Ensuite, les questionnaires ne sont pas générés automatiquement. Ainsi, si un utilisateur finit tous les questionnaires, treize au total, il ne peut pas les refaire avec différentes valeurs. 

```{figure} img/Brilliant_screen.png 
:scale: 25 % 
:alt:  
Exemple de questionnaire sur "Brilliant" {cite:p}`Site:Brilliant` 
``` 

Cela limite l’apprentissage de l’utilisateur sur "Brilliant". S'il veut avoir plus d’exercices, il doit aller sur un autre site. Un autre problème avec les questionnaires est qu’il n’y en a pas assez. En effet, sur les treize, il n’y a que deux qui sont liés directement à la théorie. Les onze autres sont des exercices plus généraux qui sont à la fin des trois grandes parties. Cela rend les exercices moins intuitifs et plus compliqués. Étant donné que les exercices ne changent jamais de réponses, si une personne se trompe l’exercice est « gâché ».  

#### Points positifs 

"Brilliant" est une entreprise à but commercial. C'est-à-dire que leur but est de faire du profit. Ainsi, le site à intérêt à faire des pages de qualité. Étant donné qu'il compte plus de dix millions d'utilisateurs {cite:p}`Site:Brilliant_home`, l'utilisateur, peut être sûr de la qualité du site. Ainsi, s'il veut apprendre d'autres thèmes, il peut le faire. L'abonnement et le nombre d'utilisateurs prouvent que "Brilliant" est un site de qualité et que la théorie apprise dessus sera juste. 

### Khan Academy 

#### Présentation générale 

"Khan Academy {cite:p}`Site:Khan`" est une association non-lucrative. Son objectif est de "fournir un contenu éducatif de qualité, gratuit, accessible à tous et partout"{cite:p}`Khan:wiki`. Ainsi, le site ne nécessite pas d'abonnement pour avoir accès à toute la théorie. Comme "Brilliant {cite:p}`Site:Brilliant`" "Khan Academy" est un site interactif. La théorie sur le site va des mathématiques à l'économie en passant par l'histoire de l'art {cite:p}`Khan:wiki`. Le site contient plus de huit mille leçons différentes complètements gratuites. Cependant, les points positifs et négatifs seront seulement jugés sur la partie arithmétique modulaire.  
#### Points négatifs

"Khan Academy" n'a pas de points négatifs marquants à relever dans le cadre de ce projet.
#### Points positifs  

Pour commencer, "Khan Academy" est gratuit. Cela veut dire que chaque utilisateur à accès à toutes les leçons présentées par le site. "Khan Academy" est aussi disponible en français et sur mobile. Cela permet de rendre la théorie accessible au plus de monde possible.
Ensuite, il a plus de huit mille leçons. Ces leçons ont des thèmes très variés [^myref4]. Ainsi, le contenu présent sur le site est énorme et varié.
"Khan Academy" contient aussi des modules interactifs.
Le site contient plusieurs pages, dix-sept au total. Chaque page présente un concept spécifique. Ces pages sont ordonnées des plus basiques au plus compliquées. Elles sont séparées par des questionnaires. Ces questionnaires ne sont pas générés automatiquement. Cependant, ils sont assez nombreux pour que cela ne pose pas de problèmes.
Un type de questionnaire interactif, très intéressant est le jeu. En tout, il y a deux versions de ce jeu différentes. Elles présentent les théories importantes de manière interactive. Ces jeux permettent d'apprendre la théorie ludiquement. 
```{figure} img/Khan_screen.png 
:scale: 30 % 
:alt:  
Exemple du jeu sur "Khan Academy" {cite:p}`Site:Khan` 
``` 
"Khan Academy" offre aussi la possibilité d'interagir avec la communauté. À la fin de chaque chapitre, il est possible de poser une question sur la théorie présentée. Cette question est ensuite répondue par la communauté. Cela permet de répondre à toute les éventuelles question qu'un utilisateur a sans devoir chercher sur internet. Cependant, la majorité des questions et des réponses sont en anglais.  

## Aspects du projet 

### Aspect pédagogique 

Le premier aspect est l'aspect pédagogique. Cet aspect est central pour rendre la théorie la plus accessible possible. L'objectif pédagogique principal est quel le site ressemble à "Khan Academy {cite:p}`Site:Khan`".

Un problème que des utilisateurs peuvent rencontrer est le langage complexe des mathématiques. En effet, la théorie est souvent écrite avec des symboles et des expressions mathématiques. L'utilisateur doit les connaître s'il veut pouvoir comprendre le texte. Ainsi, la théorie doit être simplifiée. Elle doit être compréhensible sans avoir à rechercher sur Internet. Ensuite, les modules servent à accompagner la théorie. Ils permettent d'illustrer les théorèmes de manière interactive. Ainsi, les théorèmes les plus difficiles sont encore plus simplifiés.  
### Aspect technique 

L'aspect technique du site est aussi important.

Premièrement, les modules interactifs sont optimisés et fonctionnent avec le plus de valeurs possibles. L'optimisation est importante pour permettre aux utilisateurs d'utiliser les modules même si les valeurs rentrées sont grandes. Cela leur permet de tester le plus de valeurs possibles, ainsi que d'étendre l'utilisation du module. Le deuxième aspect, le fonctionnement du module, augmente l'utilisabilité et enlève les bugs. Pour commencer, les modules peuvent prendre toutes les valeurs possibles. C'est-à-dire que l'utilisateur n'est pas limité par le module. Il peut choisir des valeurs qui l'intéresse. Cependant, certaines valeurs ne marchent pas. La plupart sont dues aux mathématiques dans le code [^myref2]. Ensuite, les bugs sont limités. Le code marche pour la majorité des valeurs [^myref3] et avec des valeurs élevées.
Deuxièmement, la structure des fichiers doit être intuitive. Pour commencer, les fichiers sont structurés par partie. Chaque partie est divisée en trois pages différentes. La première contient le code pour le module, la deuxième, le texte et la dernière le questionnaire. Cela permet de facilement trouver un fichier et de rajouter des parties si nécessaire.
Pour finir, le code doit être compréhensible. Dans un premier temps, il le code est optimisé. Cette optimisation permet de le rendre plus lisible et clair. Ainsi, s'il y a, par exemple, un bug. Il peut facilement être repéré et réparer. Ensuite, il doit être modulaire. Par exemple, si un nouveau module est créé qui ressemble à un ancien. Il est possible de prendre le code, remplacer certaines valeurs et le faire fonctionner. Cela permet de faire des modules facilement.  
 
 
 

[^myref]: Ces sites seront présentés dans la partie "Autres sites" 

[^myref1]: Présenté dans la partie "Points positifs" 

[^myref2]: Par exemple les valeurs négatives dans le module "congruence" 

[^myref3]: Les bugs connus seront discutés dans la partie "Travaux futurs" 

[^myref4]: Les mathématiques, l'informatique, l'histoire, la finance, la physique, la chimie, la biologie, l'astronomie, l'histoire de l'art, l'économie et plusieurs compétences personnelles {cite:p}`Khan:wiki` 
