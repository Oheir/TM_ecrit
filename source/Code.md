```{raw} latex
\appendix
```
# Code

## Code pour le module congruence

```{code-block} HTML
<template>
  <input v-model.number="k" placeholder="edit me" />
  
  <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <g>
      <circle cx="50" cy="20" r="10" />
    </g>
    <g fill="#D9D9D9">
      <circle cx="50" cy="20" r="9.7" />
    </g>
    <g
      v-for="i in range(k)"
      key="i"
      fill="#grey"
      :transform="`rotate(${angle_generator[i]} 50 20) translate(0 -20)`"
    >
      <circle cx="50" cy="50" :r="angle_gen[i]" @click="count=id_generator[i], mod_n=id_generator[i], rayon_spec=id_generator[i] "/>
      <text
        x="50"
        y="50"
        fill="black"
        font-size="20%"
        :transform="`rotate(0 50 50) translate(-1 5)`"
      >
        {{ id_generator[i] }}
      </text>
    </g>
  </div>
  <line x1="10" y1="50" x2="90" y2="50" stroke="darkgrey" />
  <g
      v-for="i in range(5)"
    :transform="`translate(${-30 + 15*i} 0)`"
      fill="black"
    >
      <circle cx="50" cy="50" r="2" @click="mod_n=number_gen[i]"/>
        <text
        x="50"
        y="50"
        fill="black"
        font-size="20%"
        :transform="`translate(-1 5)`"
      >
        {{ number_gen[i] }} 
      </text>
      </g>
  </svg>
  <div class="btn">
      <svg width="37" height="52" viewBox="0 0 37 52" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M0.998413 25.5965L26.5934 51.1914L36.1915 41.5933L20.1946 25.5965L36.1915 9.59963L26.5934 0.00152588L0.998413 25.5965Z" fill="#454545" @click="mod_k--"/>
      </svg>

        
      <svg width="37" height="52" viewBox="0 0 37 52" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M0.998413 41.5933L10.5965 51.1914L36.1915 25.5965L10.5965 0.00152588L0.998413 9.59963L16.9953 25.5965L0.998413 41.5933Z" fill="#454545" @click="mod_k++"/>
      </svg>

  </div>
<p id="ca">{{mod_n}} ≡ {{count}} (mod {{k}})</p>

</template>

<script>
export default {
  name: 'Cercle',
  props: {
    msg: String
  },
  data() {
    return {
      i: '',
      k: 12,
      count: 0,
      mod_k: 1,
      mod_n: 0,
      rayon_spec: 0  
    };
  },
  methods: {
    range(k) {
      let result = Array(k);
      for (let i = 0; i < k; i++) {
        result[i] = i;
      }
      return result;
    },
  },
  computed: {
    angle_generator() {
      let n = 1;
      let nbr_angle_base = 360 / this.k;
      let nbr_angle = 360 / this.k;
      let angles = [180];

      while (n < this.k) {
        angles.push(180 + nbr_angle);
        nbr_angle += nbr_angle_base;
        n++;
      }

      return angles;
    },
    id_generator() {
      let id = [0];
      let n = 1;

      while (n < this.k) {
        id.push(n);
        n++;
      }
      return id;
    },
    number_gen() {
      let mod_k = this.mod_k;
      let count = this.count;
      let k = this.k
      let nums = []
  

      for (let i = -3; i < 2; i++){
         nums.push(count + k * (mod_k + i))
      }
      
      return nums 
    },
    angle_gen() {
      let rayons = []
      let rayons_spec = this.rayon_spec
      let n = 0
      while(n < this.k){
        if(n == rayons_spec){
          rayons.push(2)
        }
        else{
          rayons.push(1.5)
        }
        n++
      }
      return rayons
    }
  },
};
</script>
```

## Code tableau PGDC
```{code-block} HTML
<template>
  <div class="input_layout">
    <input class="input"v-model="a" placeholder="a">
    <input class="input"v-model="b" placeholder="b"> 
  </div>
  <div id="ad">
    <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <rect x="0" y="0" width="100" height="10" 
    style="fill: #D9D9D9; stroke: black; stroke-width: 0.5"/>
    <g v-for="i in range(6)" >
     <line :x1=colonne_right[i] y1="-50" :x2=colonne_right[i] :y2=(10*(longueur+1))
     style="stroke: black; stroke-width: .3"/>     
     <text 
        x="50"
        y="50"
        fill="black"
        font-size="20%"
        :transform="`translate(${text_right[i]} -44)`"
        fill="#D9D9D9">
        {{text[i]}}
      </text>
      </g>
    <g v-for="i in range(longueur)"
        font-size="20%"
        fill="#D9D9D9">
      <text 
      x="50"
      y="50"
      :transform="`translate(${text_right[0] + 2} ${-33 + 10*i})`">
        {{i + 1}}
      </text>
      <text 
      x="50"
      y="50"
      :transform="`translate(${text_right[1] + 2} ${-33 + 10*i})`">
        {{remplissage_calcul[0][i]}}
      </text>
       <text 
      x="50"
      y="50"
      :transform="`translate(${text_right[2] + 2} ${-33 + 10*i})`">
        {{remplissage_calcul[1][i]}}
      </text>
       <text 
      x="50"
      y="50"
      font-size="70%"
      :transform="`translate(${text_right[3] - 4} ${-33 + 10*i})`">
        {{remplissage_calcul[2][i]}}
      </text>
       <text 
      x="50"
      y="50"
      :transform="`translate(${text_right[4] + 2} ${-33 + 10*i})`">
        {{remplissage_calcul[3][i]}}
      </text>
       <text 
      x="50"
      y="50"
      :transform="`translate(${text_right[5] + 2} ${-33 + 10*i})`">
        {{remplissage_calcul[4][i]}}
      </text>
    </g>
  </div>
  </svg>

  <div class="input_layout">
    <button  class="input" v-if="step < longueur" @click="step++">prochaine étape</button>
    <button  class="input" v-else>prochaine étape</button>
    <button  class="input" v-if="step > 0" @click="step--">étape précédente</button>
    <button  class="input" v-else>étape précédente</button>
  </div>
</template>

<script>
export default {
  name: 'Tableaupdgc',
  props: {
    msg: String
  },
  data() {
    return {
      a: '',
      b:'',
      step: 0,
      text: ["étape", "Dividende a", "Diviseur b", "équation", "Quotient", "Reste"],
      text_right: [-48, -37, -16, 5, 24, 40.5],
      colonne_right: ["12","32","50","72","89","101"]
    };
  },
  methods: {
    range(k) {
      let result = Array(k);
      for (let i = 0; i < k; i++) {
        result[i] = i;
      }
      return result;
    },
  },
  computed: {
    longueur() {
      let a = this.a;
      let b = this.b;
      let t = 0
      let i = 0

      while(b!=0){
        t = b
        b = a % b
        a = t
        i ++
        }
      i++
      return i
    },
    remplissage_calcul() {
      let a_arr = []
      let b_arr = []
      let equ_arr = []
      let quo_arr = []
      let res_arr = []

      let a = this.a
      let b = this.b
      let quo = 0
      let reste = 0      
      
        for (let i = 0; i < this.step; i++){
           if(b!=0){
            quo = Math.floor(a/b)
            reste = a-(b*Math.floor(a/b))

            a_arr.push(a)
            b_arr.push(b)
            quo_arr.push(quo)
            res_arr.push(reste)
            equ_arr.push(`${a} = ${b} * ${quo} + ${reste}`)

            a = b
            b = reste
            
          }
          else{
            a_arr.push(a)
            b_arr.push(b)
            equ_arr.push(`pgdc = ${a}`)
          }
        }
       return [a_arr,b_arr,equ_arr,quo_arr,res_arr]
    }
  }
}
</script>

```

## Code tableau inverse
```{code-block} HTML
<template>
  <div class="input_layout">
    <input class="input" v-model="a">
    <input class="input" v-model="b"> 
  </div>
  
  <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <rect x="0" y="0" width="100" height="10" 
    style="fill: #D9D9D9; stroke: black; stroke-width: 0.5"/>
    <g v-for="i in range(6)">
     <line :x1=colonne_right[i] y1="-50" :x2=colonne_right[i] :y2=(10*(step+1))
     style="stroke: black; stroke-width: .3"/>     
     <text 
        x="50"
        y="50"
        fill="black"
        font-size="20%"
        :transform="`translate(${text_right[i]} -44)`">
        {{text[i]}}
      </text>
      </g>
    <g v-for="i in range(step)"
        font-size="20%"
        fill=" #D9D9D9">
      <text 
      x="50"
      y="50"
      :transform="`translate(${text_right[0] + 2} ${-33 + 10*i})`">
        {{remplissage_calcul[0][i + 1]}}
      </text>
      <text 
      x="50"
      y="50"
      :transform="`translate(${text_right[1] + 2} ${-33 + 10*i})`">
        {{remplissage_calcul[1][i + 1]}}
      </text>
       <text 
      x="50"
      y="50"
      :transform="`translate(${text_right[2]} ${-33 + 10*i})`">
        {{remplissage_calcul[2][i + 1]}}
      </text>
       <text 
      x="50"
      y="50"
      font-size="70%"
      :transform="`translate(${text_right[3] - 10} ${-33 + 10*i})`">
        {{remplissage_equ[0][i + 1]}}
      </text>
       <text 
      x="50"
      y="50"
      font-size="70%"
      :transform="`translate(${text_right[4] - 10} ${-33 + 10*i})`">
        {{remplissage_equ[1][i + 1]}}
      </text>
       <text 
      x="50"
      y="50"
      :transform="`translate(${text_right[5] + 2} ${-33 + 10*i})`">
        {{remplissage_calcul[3][i + 1]}}
      </text>
    </g>
    <text v-if="remplissage_calcul[3][step] != 0 ">
    </text>
    <text
    x="25"
    y="100"
    font-size="20%"
    fill="#D9D9D9"
    v-else>
    inverse modulaire = {{remplissage_equ[2]}} + {{a}} = {{remplissage_equ[3]}}
    </text>
  </svg>

  <div class="input_layout">
    <button class="input" v-if="remplissage_calcul[3][step] != 0 " @click="step++">prochaine étape</button>
    <button class="input" v-else>prochaine étape</button>
    <button class="input" v-if="step > 0" @click="step--">étape précédente</button>
    <button class="input" v-else>étape précédente</button>
  </div>

</template>

<script>
export default {
  name: 'Tableauinverse',
  props: {
    msg: String
  },
  data() {
    return {
      a: 167,
      b:23,
      step: 0,
      text: ["modulo", "chiffre", "q", "s", "t", "Reste"],
      text_right: [-49, -37, -23.5, -5, 24, 40.5],
      colonne_right: ["12","23","32","60","89","101"]
    };
  },
  methods: {
    range(k) {
      let result = Array(k);
      for (let i = 0; i < k; i++) {
        result[i] = i;
      }
      return result;
    },
  },
  computed: {
    remplissage_calcul() {
      let a = this.a
      let b = this.b
      let reste = 0
      let quo = 0

      let quo_arr =[0]
      let reste_arr = [1]
      let a_arr = [0]
      let b_arr = [0]

      for (let i = 0; i < this.step + 1; i++){
        quo = Math.floor(a/b)
        reste = a - b * quo

        a_arr.push(a)
        b_arr.push(b)
        quo_arr.push(quo)
        reste_arr.push(reste)

        a = b
        b = reste
      }
      return [a_arr,b_arr,quo_arr,reste_arr]
    },
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
  }
}
</script>

```

