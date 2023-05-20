console.log("Vue compoenents js file loaded")
Vue.createApp({
    data() {
        return {
            links: ["Home", "Products", "Location", "About"],
            logged: true
        }
    },
    delimiters: ["[[", "]]"]
}).mount("nav")



Vue.createApp({
    data() {
        return {
            quantity: 1,
            count: count,
            activeTab: "1",

            Rate5:rate5,
            Rate4:rate4,
            Rate3:rate3,
            Rate2:rate2,
            Rate1:rate1,

             originalPrice : price,
            discountPrice : discountprice,
        
        }
    },
    delimiters: ["[[", "]]"],

    computed: {
        discount() {
          return ((this.originalPrice - this.discountPrice) / this.originalPrice) * 100;
        }
      },

    methods: {
        
        increment() {
            if (this.quantity < count) { this.quantity++; }
        },
        decrement() {
            if (this.quantity > 1) {
                this.quantity--;
            }
        },
        formatDiscount(discount) {
            return Math.floor(discount);
          }

        

    },

}).mount("#single")



Vue.createApp({
    data() {
        return {

            name:1,
            // originalPrice :price ,
            // discountPrice :discountprice,
            // pro: pro,

            
            
        }
    },
    delimiters: ["[[", "]]"],
    // computed: {
    //     discount() {
    //     for (var i = 0; i < this.pro.length; i++) {  
    //       return ((this.pro[i].price - this.pro[i].discountprice) / this.pro[i].price) * 100;
    //       break;
    //     }
    //     }
    //   },
    //   methods: {
    //   formatDiscount(discount) {
    //     return Math.floor(discount);
    //   }

}).mount("#products")




Vue.createApp({
    data() {
        return {
          num:1,
        }
    },
    delimiters: ["[[", "]]"],

    methods: {
        addTask: function(){
          this.tasks.push({words: this.taskText, done:false});
          this.taskText='';
        },
        deleteTask: function(index){
        this.tasks.splice(index,1);
        },
        deleteAll: function(){
          this.tasks = [];
        }
      },
     

}).mount("#cart")



Vue.createApp({
    data() {
        return {
            fieldType: 'password',
            show: false,
            password:null,
        }
    },
    delimiters: ["[[", "]]"],
    methods: {
        switchField(){
          this.fieldType = this.fieldType=== 'password'?'text':'password';
        },
    }
}).mount("#register")