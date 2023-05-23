# Code et Regard critique

## Code

### Tableau inverse remplissage_equ()
Cette fonction permet de remplir les parties "s" et "t" du tableau. La fonction est séparée de la fonction "remplissage_calcul()" pour la rendre plus facile à écrire. 

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
Cette fonction prend les valeurs "a" et "b" pour en trouver l'inverse modulaire. Il y a deux types d'arrays différents. Les arrays finissant par "_number" servent à stocker les nombres. Alors que les arrays finissants par "_arr" servent à stocker les équations. Les arrays de type "_number" sont nécessaires pour les calculs. Les arrays de type "_arr" ont besoin des nombres de l'étape d'avant pour calculer le nombre de cette étape. "Quo" est le quotient de "a" et "b". Il sert à trouver le reste. "Quo" et "reste" ne servent pas à remplir le tableau dans cette fonction parce qu'ils sont déjà utilisés dans la fonction "remplissage_calcul()". Cependant, ils servent à calculer les équations.
La fonction `return` les équations permettant de remplir le tableau. Ensuite, elle retourne le nombre nécessaire pour trouver l'inverse modulaire. Pour finir, elle retourne l'inverse modulaire en lui-même. 
### Rôle des fichiers  

Les fichiers sont divisés en sections. Chaque section contenant trois sous-fichiers.
Le premier contient le module interactif. Le deuxième contenant le texte et aussi le sous-fichier principal de la section. Le dernier sous-fichier est celui qui contient le code pour le questionnaire. Le sous-fichier module interactif et celui contenant le code pour le questionnaire sont reliés au fichier texte. C'est ce sous-fichier qui est ensuite utilisé sur le site. 
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
Il devait faire un rectangle comme l'image ci-dessus. Cet objectif n'a pas été atteint pour plusieurs raisons. Premièrement, coder comment trouver les valeurs des rectangles s'est avéré plus dur que prévu. Par exemple, trouver s'il fallait le mettre en hauteur, largeur, le nombre de rectangles à rajouter et la dernière étape. Faire tout cela a pris trop de temps. Il a donc été décidé de ne pas continuer dans cette direction. Il serait possible d'imaginer une version moins compliquée. C'est-à-dire sans la dernière étape ou en remplaçant le rectangle par une autre forme.

Deuxièmement, le contenu du site n'atteint pas le niveau espéré. Il n'y a pas assez de contenu comparé à l'objectif initial. Pour améliorer, il faudrait rajouter de nouveaux modules, concepts et améliorer les modules existants.

### Fonctionnalités à développer

Les fonctionnalités intéressantes à développer sont centrés autour du rajout de contenu au site. Comme ce sujet est développé dans "Travaux futurs", il n'est pas repris ici.
