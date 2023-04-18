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
            activeTab: "1"
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
    }
}).mount("#single")

