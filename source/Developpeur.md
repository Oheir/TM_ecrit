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

Les fichiers sont par parties. Chaque partie contient trois fichiers. 
Ces fichiers commencent par le fichier contenant le module interactif. Ensuite, le prochain fichier contient le texte et est le fichier principal de la partie. Le dernier fichier est celui qui contient le code pour le questionnaire. Tous ces fichiers sont liés sur le fichier texte. C'est ce fichier qui est ensuite utilisé pour le lié au site. 