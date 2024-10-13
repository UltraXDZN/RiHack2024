import { createApp, h } from 'vue';
import { createPinia } from 'pinia';

import Login from '@/pages/Login.vue';
import Register from '@/pages/Register.vue';
import Home from '@/pages/Home.vue';
import News from '@/pages/News.vue';
import Calendar from '@/pages/Calendar.vue';

import NavBar from '@/components/NavBar.vue';

import './style.css';
import './tailwindSetup.css';

import "./style.css";
import "./tailwindSetup.css";
import CitySelection from "@/pages/CitySelection.vue";

const componentMap = {
    login: Login,
    register: Register,
    home: Home,
    news: News,
    citySelection: CitySelection,
    calendar: Calendar
};

const element = document.getElementById("app");

if (element) {
    const page = element.dataset.page;
    console.log("Page:", page);

    const appComponent = componentMap[page];

    if (appComponent) {
        const app = createApp({
            render: () => h('div', [
                h(NavBar),
                h(appComponent)
            ])
        });
        const pinia = createPinia();

        app.use(pinia);
        app.mount("#app");
    } else {
        console.error(`Unknown page type "${page}", no component mounted.`);
    }
}