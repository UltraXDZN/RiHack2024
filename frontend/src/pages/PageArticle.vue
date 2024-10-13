<template>
  <div class="max-w-5xl mx-auto mt-12 p-8 bg-white shadow-lg rounded-lg">
    <!-- News Title -->
    <h1 class="text-4xl font-bold text-center mb-6 text-gray-800">{{ article.news.title }}</h1>

    <!-- News Description -->
    <p class="text-lg italic text-center text-gray-600 mb-8">{{ article.news.description }}</p>

    <!-- News Banner (Image) -->
    <div v-if="article.banner" class="mb-8">
      <img :src="article.banner" alt="News Banner" class="w-full h-auto object-cover rounded-lg"/>
    </div>

    <!-- Rich Text Content -->
    <div class="prose prose-lg max-w-none text-black" v-html="article.news.content"></div>

    <!-- Author and Created At Information -->
    <div class="mt-8 pt-6 border-t border-gray-200 flex justify-between text-sm text-gray-500">
      <span class="font-semibold">Napisao/la: {{ article.news.author__username }}</span>
      <span>Objavljeno: {{ formatDate(article.news.created_at) }}</span>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      article: {},
    };
  },
  mounted() {
    this.fetchArticle();
  },
  methods: {
    async fetchArticle() {
      // Use `window.location.pathname` to get the ID from the current URL
      const articleId = window.location.pathname.split("/").filter(Boolean).pop(); // Get the last segment (ID)

      if (!articleId) {
        console.error('No article ID found in the URL');
        return;
      }

      try {
        const response = await fetch(`/api/news/${articleId}/`);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        this.article = data;
        console.log('Fetched article:', this.article.news)
      } catch (error) {
        console.error('Error fetching the article:', error);
      }
    },
    formatDate(dateString) {
      const options = {year: 'numeric', month: 'long', day: 'numeric'};
      return new Date(dateString).toLocaleDateString(undefined, options);
    },
  },
};

</script>
