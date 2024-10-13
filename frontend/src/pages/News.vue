<template>
    <div>
        <h1
            class="mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-900 md:text-5xl lg:text-6xl dark:text-white"
        >
            Kalendar događanja
        </h1>

        <span
            class="bg-blue-100 text-blue-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded dark:bg-blue-900 dark:text-blue-300"
            >Sport i Zabava</span
        >
        <span
            class="bg-gray-100 text-gray-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded dark:bg-gray-700 dark:text-gray-300"
            >Moda i Umjetnost</span
        >
        <span
            class="bg-red-100 text-red-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded dark:bg-red-900 dark:text-red-300"
            >Politika i Društvo</span
        >
        <span
            class="bg-green-100 text-green-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded dark:bg-green-900 dark:text-green-300"
            >Znanost i IT</span
        >
        <span
            class="bg-yellow-100 text-yellow-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded dark:bg-yellow-900 dark:text-yellow-300"
            >Životni stil</span
        >
        <span
            class="bg-indigo-100 text-indigo-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded dark:bg-indigo-900 dark:text-indigo-300"
            >Biljke i životinje</span
        >
        <span
            class="bg-purple-100 text-purple-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded dark:bg-purple-900 dark:text-purple-300"
            >Interaktivni sadržaji</span
        >

        <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
            <NewsCard
                v-for="news in newsList"
                :key="news.id"
                :title="news.title"
                :image="'/media/' + news.banner"
                :description="news.description"
                :author="news.author__username"
                :date="news.created_at"
            />
        </div>
    </div>
</template>

<script>
import NewsCard from "@/components/NewsComponents/NewsCard.vue";

export default {
    name: "News",
    components: { NewsCard },
    data() {
        return {
            newsList: [], // Array of news articles
        };
    },
    created() {
        this.loadNews();
    },
    methods: {
        async loadNews() {
            try {
                const response = await fetch("/api/news/");
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                const data = await response.json();
                console.log(data);
                console.log("data.news", data.news);
                this.newsList = data.news; // Make sure the API response includes the necessary fields
                console.log("this.newsList", this.newsList);
            } catch (error) {
                console.error("Error loading news:", error);
            }
        },
    },
};
</script>
