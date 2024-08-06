import Vue from 'vue'

Vue.config.silent = true

app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue.js!'
    }
})

Vue.config.optionMergeStrategies._my_option = function (parent, child, vm) {
    return child + 1
}

const Profile = Vue.extend({
    _my_option: 1
})

// Porfile.options._my_option === 2