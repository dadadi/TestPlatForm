import axios from './http'
const testcase = {
    getTestcase(){
        return axios({
            method:'get',
            url:'/testcase',
        })
    },
    deleteTestcase(){
        
    },
    updateTestcase(){

    },
    postTestcase(){

    }
}
export default testcase