<script>
import NewsCard from "@/components/NewsComponents/NewsCard.vue";
import {useAuthStore} from "@/store/auth.js";

export default {
  name: "News",
  components: {NewsCard},
}
</script>

<template>
  <NewsCard />
</template>


