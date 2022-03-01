import axios from './http'
const task = {
    getTask(){
        return axios({
            method:'get',
            url:'/task',
        })
    },
    postTask(){

    },
    updateTask(){

    },
    deleteTask(){
        
    },
}
export default task