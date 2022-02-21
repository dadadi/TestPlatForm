import axios from './http'
const task = {
    getTask(){
        return axios({
            method:'get',
            url:'/task',
        })
    },
    deleteTask(){
        
    },
    updateTask(){

    },
    postTask(){

    }
}
export default task