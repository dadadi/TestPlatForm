import axios from 'axios'

var instance = axios.create({
    headers:{
        'Content-Type':'application/json'
    },
    baseUrl:'http://127.0.0.1:8080'
})

// 如果要在别的地方使用，还需要加export default
export default instance