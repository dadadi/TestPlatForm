import axios from './http'
const testcase = {
    getTestcase(){
        return axios({
            method:'get',
            url:'/testcase',
        })
    },
    postTestcase(params){
        return axios({
            method:'post',
            url:'/testcase',
            // 使用data参数传递请求体
            data:params,
        })
    },
    updateTestcase(params){
        return axios({
            method:'put',
            url:'/testcase',
            // 使用data参数传递请求体
            data:params,
        })
    },
    deleteTestcase(params){
        return axios({
            method:'delete',
            url:'/testcase',
            params:{
                id:params
            }
        })
    },
    
    
}
export default testcase