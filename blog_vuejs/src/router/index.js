import {createRouter, createWebHistory} from 'vue-router'
import HomePage from "@/views/HomePage";
import Postpage from "@/views/Postpage";
import Registration from "@/views/Registration";
import Login from "@/views/Login";
import CreatedPost from "@/views/CreatedPost";

const routes = [
    {
        path: '/',
        name: 'HomePage',
        component: HomePage
    },
    {
        path: '/:url',
        name: 'Postpage',
        component: Postpage,
        props: true,
    },
    {
        path: '/login',
        name: 'Login',
        component: Login,
    },
    {
        path: '/Registration',
        name: 'Registration',
        component: Registration,
    },
    {
        path: '/CreatedPost',
        name: 'CreatedPost',
        component: CreatedPost,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router