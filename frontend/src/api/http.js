import axios from 'axios'

var instance = axios.create({
    headers:{
        'Content-Type':'application/json'
    },
    baseURL:'http://127.0.0.1:5000'
})

// 如果要在别的地方使用，还需要加export default
export default instance