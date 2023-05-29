# Code et Regard critique

## Code

### Tableau inverse remplissage_equ()
Il est judicieux de séparer la fonction de remplissage des parties "s" et "t" du tableau de la fonction principale "remplissage_calcul()". Cela permet de diviser le code en fonctionnalités distinctes, ce qui rend le code plus modulaire et plus facile à lire, à comprendre et à maintenir.

```{code-block} javascript
remplissage_equ(){
      let a = this.a
      let b = this.b
      let quo = 0
      let reste = 0
      let longueur = 0
      let inverse = 0

      let s_arr = [0]
      let t_arr = [0]
      let s_arr_number = [0]
      let t_arr_number = [1]

      for (let i = 0; i < this.step ; i++){
        quo = Math.floor(a / b)
        reste = a - b * quo
        
        if(i == 0){
          s_arr.push(1)
          t_arr.push(-quo)
          t_arr_number.push(-quo)
          s_arr_number.push(1)
        }
        else{
          t_arr_number.push(t_arr_number[i-1] - quo * t_arr_number[i])
          s_arr_number.push(s_arr_number[i-1] - quo * s_arr_number[i])

          s_arr.push(`${s_arr_number[i-1]} - ${quo} * ${s_arr_number[i]} = ${s_arr_number[i+1]}` )
          t_arr.push(`${t_arr_number[i-1]} - ${quo} * ${t_arr_number[i]} = ${t_arr_number[i+1]}`)
        }
        a = b
        b = reste
        inverse = t_arr_number[t_arr_number.length - 2] 
        inverse += parseInt(this.a)
      }
      return [s_arr,t_arr,t_arr_number[t_arr_number.length - 2], inverse]
    }
```
La fonction trouverInverseModulaire(a, b) prend deux arguments, a et b, qui sont les valeurs pour lesquelles vous souhaitez trouver l'inverse modulaire.

La fonction initialise deux tableaux vides : equations pour stocker les équations générées lors du calcul, et numbers pour stocker les nombres nécessaires pour les calculs.

Ensuite, à l'aide d'une boucle, la fonction effectue les calculs nécessaires pour remplir le tableau. À chaque itération, elle calcule le quotient (quo) et le reste (reste) de la division de a par b, puis ajoute l'équation correspondante dans le tableau equations et les valeurs de a, b, quo et reste dans le tableau numbers.

Une fois la boucle terminée, la fonction crée un objet contenant les tableaux equations et numbers, ainsi que les valeurs nécessaires pour trouver l'inverse modulaire : le nombre nécessaire (number) pour remplir le tableau et l'inverse modulaire (inverseModulaire), qui est le dernier élément de numbers.

Enfin, la fonction retourne cet objet contenant les résultats.

J'espère que cela vous aide à comprendre la logique de la fonction pour trouver l'inverse modulaire. Si vous avez besoin d'un exemple de code spécifique, veuillez le préciser et je serai ravi de vous aider davantage.





### Rôle des fichiers  

Chaque section du site est divisée en trois sous-fichiers distincts :

Le premier sous-fichier de la section contient le module interactif correspondant à cette section. Ce module interactif peut inclure des éléments tels que des graphiques, des animations ou des fonctionnalités interactives pour aider à l'apprentissage.

Le deuxième sous-fichier de la section est le fichier texte principal qui contient le contenu et les explications associées à cette section. Il fournit le contenu théorique et conceptuel pour l'apprentissage.

Le dernier sous-fichier de la section est dédié au code du questionnaire. Il contient le code qui génère les questions et les réponses possibles pour cette section spécifique.

Ces sous-fichiers sont liés entre eux, où le sous-fichier du module interactif et celui du questionnaire sont reliés au fichier texte principal de la section. Cela permet d'intégrer les éléments interactifs et le questionnaire dans le contenu principal du site.

En fin de compte, c'est le sous-fichier texte principal qui est utilisé pour afficher le contenu de la section sur le site. Il intègre les informations du module interactif et du questionnaire pour fournir une expérience d'apprentissage interactive et complète.

J'espère que cela clarifie la structure des fichiers de chaque section du site. N'hésitez pas à me poser d'autres questions si vous en avez besoin !





## Regard critique

### Bugs

Le code ne comporte pas beaucoup de bugs. Le principal est celui du tableau d'inverse modulaire. Ce bug fait que, pour certaines valeurs, le signe du calcul est inversé. L'inverse modulaire alors trouvé est donc faux. Cependant, ce bug n'est pas réplicable. C'est-à-dire que des valeurs qui avant ne marchaient pas, marchent. Par exemple, pour une valeur de "a" de 166, le tableau va retourner une valeur pour l'inverse de 231 pour un "b" valant 23. Cette valeur n'est pas possible, car le modulo est égal à 166.

### Éléments ne répondant pas aux objectifs fixés

Pour commencer, le tableau pour trouver le pgdc ne devait pas être un tableau.
```{figure} img/Wiki_euclide.png 
:scale: 20 % 
:alt:  
Projet initial du module pgdc {cite:p}`Algo:Eucl` 
``` 

L'objectif de créer un rectangle interactif n'a pas été réalisé en raison de difficultés rencontrées lors de la détermination des valeurs nécessaires. Les aspects tels que la dimension, la position, le nombre de rectangles à ajouter et l'étape finale se sont avérés plus complexes que prévu, ce qui a pris plus de temps que prévu. Par conséquent, la décision a été prise de ne pas poursuivre dans cette direction. Une version simplifiée sans l'étape finale ou en remplaçant le rectangle par une autre forme pourrait être envisagée.

En outre, le contenu du site n'a pas atteint le niveau souhaité en termes de quantité. Il est nécessaire d'ajouter de nouveaux modules, concepts et d'améliorer les modules existants pour améliorer le contenu global du site.







### Fonctionnalités à développer

Les fonctionnalités intéressantes à développer se concentrent principalement sur l'ajout de contenu au site. Cependant, étant donné que ces idées sont abordées plus en détail dans la section "Travaux futurs", elles ne sont pas reprises ici de manière exhaustive.





