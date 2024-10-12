import { createApp } from 'vue';
import { createPinia } from 'pinia';

import Login from '@/pages/Login.vue';
import Register from '@/pages/Register.vue';
import Home from '@/pages/Home.vue';
import News from '@/pages/News.vue';
import Calendar from '@/pages/Calendar.vue';
import './style.css';
import './tailwindSetup.css';


const componentMap = {
    login: Login,
    register: Register,
    home: Home,
    news: News,
    calendar: Calendar,
};

const element = document.getElementById('app');

if (element) {
    const page = element.dataset.page;
    console.log('Page:', page);

    const appComponent = componentMap[page];

    if (appComponent) {
        const app = createApp(appComponent);
        const pinia = createPinia();

        app.use(pinia);
        app.mount('#app');
    } else {
        console.error(`Unknown page type "${page}", no component mounted.`);
    }
}
