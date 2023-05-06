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

            // discountprice:80,
            // originalPrice: 100, // add originalPrice to data object
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
            price:300,
            discountprice:100,

            
            
        }
    },
    delimiters: ["[#", "#]"],
    
    
  


}).mount("#products")


