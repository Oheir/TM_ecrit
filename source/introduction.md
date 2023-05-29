# Introduction 

### Contexte du TM
L'arithmétique modulaire est rarement abordée dans le cursus scolaire habituel, pourtant elle revêt une grande importance pour comprendre des concepts utilisés au quotidien. Bien qu'il existe déjà des sites dédiés à l'apprentissage de l'arithmétique modulaire, ceux-ci se limitent souvent à présenter des principes spécifiques sans entrer dans les détails.

Parmi les principaux sites abordant ce sujet, on retrouve "Brilliant"{cite:p}`Site:Brilliant` et "Khan Academy"{cite:p}`Site:Khan`. Cependant, chacun présente ses propres inconvénients. Ainsi, ce projet s'inspire des avantages de ces deux sites pour offrir une meilleure expérience d'apprentissage.[^myref2]

### Objectifs du travail
L'objectif principal du site est d'enseigner les bases de l'arithmétique modulaire de manière interactive aux utilisateurs. Cet objectif est subdivisé en plusieurs sous-objectifs. Tout d'abord, il est essentiel de rendre la théorie suffisamment accessible, afin que toute personne intéressée puisse comprendre les concepts théoriques abordés. Ensuite, le site doit proposer des modules interactifs permettant aux utilisateurs de réaliser leurs propres expériences afin de mieux assimiler la théorie. Les modules interactifs offrent également l'avantage de faciliter l'apprentissage, car ils permettent aux utilisateurs de concrétiser des notions qui peuvent parfois sembler abstraites malgré leur simplification. Enfin, le dernier objectif concerne la qualité du code. Il est important d'optimiser le code pour éviter toute redondance, c'est-à-dire éviter que plusieurs fonctions servent le même objectif[^myref], et garantir que chaque fonction remplisse correctement sa tâche. Cet objectif relève principalement de la qualité technique du site et n'est pas directement lié aux objectifs pédagogiques.

### Cas d'utilisation et utilisateurs visés 
Les cas d'utilisation et les utilisateurs ciblés par le site sont similaires. L'objectif principal est d'encourager l'apprentissage à travers des cas d'utilisation centrés sur l'expérience. Un utilisateur peut, par exemple, utiliser le site pour apprendre ou réviser les concepts théoriques abordés. Étant donné que la théorie est abordée de manière superficielle et ne va pas dans les détails, les cas d'utilisation sont limités. Cependant, cela permet aux personnes sans aucune connaissance préalable d'utiliser le site. Les utilisateurs visés sont donc des débutants dans l'apprentissage de l'arithmétique modulaire, cherchant à l'appréhender de manière interactive. Il est toutefois important de noter que la portée de la théorie limite les utilisateurs potentiels. En effet, le site ne convient pas aux utilisateurs ayant déjà un niveau avancé, car il ne leur apporterait que peu d'utilité. Cela restreint donc les utilisateurs potentiels aux personnes souhaitant acquérir les bases de l'arithmétique sans aller en profondeur et possédant peu ou pas de connaissances préalables.

### Moyens utilisés pour atteindre les objectifs 

Les objectifs sont tous atteints de différentes manières. Le premier objectif est atteint grâce à la vulgarisation de la théorie. Bien que la théorie puisse sembler abstraite, la vulgarisation est réalisée de manière à éviter une surcharge de formules. Toutefois, la difficulté de la théorie reste subjective. C'est pourquoi des modules interactifs en lien avec la théorie sont ajoutés sur la page.
```{figure} img/Screenshot_black_white.png
:scale: 60 %
:alt: 
Module permettant l'apprentissage de la congruence modulaire
```
Les modules interactifs permettent aux utilisateurs d'interagir avec eux, de modifier les valeurs et d'apprendre plus facilement. Un autre type de module, non interactif cette fois, est le questionnaire. Ce questionnaire est généré automatiquement et offre aux utilisateurs la possibilité de choisir leur niveau de difficulté. Ainsi, ils peuvent répéter les exercices autant de fois que nécessaire sans avoir à quitter le site. Cela permet à tous les utilisateurs de sélectionner le niveau qui leur convient le mieux. Ils peuvent également utiliser les modules mentionnés précédemment pour compléter les exercices s'ils rencontrent des difficultés.
 
### Structure du rapport 
Le rapport est structuré en plusieurs parties. Il débute par la section "Présentation du projet", qui présente une vue d'ensemble du projet, en mettant en évidence d'autres sites similaires et en exposant les objectifs pédagogiques et techniques. Ensuite, la section "Apprentissage" explique la logique sous-jacente des modules interactifs et la démarche de vulgarisation de la théorie. La partie "Présentation des technologies" présente les technologies[^myref1] utilisées sur le site. La section "Développement" aborde le code, les concepts scientifiques impliqués et la mise en place de l'environnement. Enfin, la dernière partie intitulée "Travaux futurs et critiques" traite des problèmes actuels du site et des objectifs d'amélioration à venir.


[^myref1]: SVG et Vuejs
[^myref]: Par exemple : deux fonctions qui retournent des valeurs similaires
[^myref2]: Brilliant et Khan academy
