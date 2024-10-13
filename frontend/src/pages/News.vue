<template>
  <div>
    <h1 class="mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-900 md:text-5xl lg:text-6xl dark:text-white">
      Kalendar događanja
    </h1>
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
  components: {NewsCard},
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
        const response = await fetch('/api/news/');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        console.log("data.news", data.news);
        this.newsList = data.news; // Make sure the API response includes the necessary fields
        console.log("this.newsList", this.newsList)
      } catch (error) {
        console.error('Error loading news:', error);
      }
    },
  },
};
</script>
