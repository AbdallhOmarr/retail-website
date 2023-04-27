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


        }
    },
    delimiters: ["[[", "]]"],

    
    methods: {
        
        increment() {
            if (this.quantity < count) { this.quantity++; }
        },
        decrement() {
            if (this.quantity > 1) {
                this.quantity--;
            }
        },

    },

}).mount("#single")

  