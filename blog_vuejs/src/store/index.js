import {createStore} from 'vuex'
import axios from 'axios'

// Create a new store instance.
const store = createStore({
    state: {
        backendURL: 'http://89.108.81.67:80/blog_api',
        token: localStorage.getItem('token') || '',
        data_user: [],
        user: localStorage.getItem('user') || '',
        category: {},
        tags: []
    },
    mutations: {
        auth_success(state, token) {
            state.status = 'success'
            state.token = token
        },
        logout(state) {
            state.status = ''
            state.token = ''
        },
        data_user(state, data_user) {
            state.data_user = data_user
        },
        mut_category(state, category) {
            state.category = category
        },
        mut_tags(state, tags) {
            state.tags = tags
        }
    },
    actions: {
        login({commit}, data) {
            return new Promise((resolve, reject) => {
                axios({url: `http://89.108.81.67:80/auth/token/login/`, data: data, method: 'POST'})
                    .then(resp => {
                        const token = resp.data.auth_token
                        /*const user = resp.data.user*/
                        localStorage.setItem('token', token)
                        /*axios.defaults.headers.common['Authorization'] = token*/
                        commit('auth_success', token)
                        console.log(resp)
                        store.dispatch('login_name')
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('auth_error')
                        localStorage.removeItem('token')
                        reject(err)
                    })
            })
        },
        login_name({commit}) {
            return new Promise((resolve) => {
                axios({
                    url: 'http://89.108.81.67:80/auth/users/me/',
                    method: 'GET',
                    headers: {'Authorization': `Token ${store.getters.get_token}`}
                })
                    .then(resp => {
                        const data_user = resp.data
                        commit('data_user', data_user)
                        localStorage.setItem('user', data_user.username)
                        console.log(resp)
                        resolve(resp)
                    })
            })
        },
        logout({commit}) {
            return new Promise((resolve, reject) => {
                commit('logout')
                localStorage.removeItem('token')
                delete axios.defaults.headers.common['Authorization']
                resolve()
            })
        },
        register({commit}, user_registr) {
            return new Promise((resolve) => {
                axios({url: 'http://89.108.81.67:80/auth/users/', data: user_registr, method: 'POST'})
                    .then(resp => {
                        console.log(resp)
                        resolve(resp)
                    })
            })
        },
        load_category({commit}) {
            return new Promise((resolve) => {
                axios({
                    url: `${this.getters.getServerUrl}/category/`,
                    method: 'GET',
                })
                    .then(resp => {
                        const categ = resp.data
                        commit('mut_category', categ)
                        console.log(resp.data)
                    })
            })
        },
        load_tags({commit}) {
            return new Promise((resolve) => {
                axios({
                    url: `${this.getters.getServerUrl}/tags/`,
                    method: 'GET',
                })
                    .then(resp => {
                        const tags = resp.data
                        commit('mut_tags', tags)
                        console.log(resp.data)
                    })
            })
        },
    },
    modules: {},
    getters: {
        getServerUrl: state => {
            return state.backendURL;
        },
        get_token: state => {
            return state.token
        },
        isLogin: state => {
            return state.data_user
        },
        get_user: state => {
            return state.user
        },
        get_category: state => {
            return state.category
        },
        get_tags: state => {
            return state.tags
        }
    },
})

export default store