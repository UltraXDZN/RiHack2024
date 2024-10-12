<script>
export default {
  name: "NewsCard",
  props: {
    title: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
    image: {
      type: String,
      default: 'https://via.placeholder.com/300x200', // Default image if none is provided
    },
    author: {
      type: String,
      default: 'Unknown Author',
    },
    date: {
      type: String,
      default: 'Unknown Date',
    },
  },
};
</script>

<template>
  <div class="max-w-sm mx-auto bg-gray-800 rounded-lg shadow-lg overflow-hidden">
    <!-- Image -->
    <img
      alt="News image"
      class="w-full h-48 object-cover"
      :src="image"
    />

    <!-- Content -->
    <div class="p-4">
      <!-- Title -->
      <h2 class="text-white text-lg font-semibold truncate">
        {{ title }} <!-- Bind the title prop -->
      </h2>
      <!-- Description -->
      <p class="text-gray-400 mt-2 text-sm">
        {{ description }} <!-- Bind the description prop -->
      </p>
    </div>

    <!-- Footer -->
    <div class="flex items-center justify-between p-4 bg-gray-900 text-gray-400 text-sm">
      <div class="flex items-center">
        <img
          class="w-8 h-8 rounded-full"
          src="https://via.placeholder.com/50"
          alt="Author Avatar"
        />
        <div class="ml-2">
          <p>{{ author }} <!-- Bind the author prop --></p>
          <p class="text-xs">{{ date }} <!-- Bind the date prop --></p>
        </div>
      </div>
    </div>
  </div>
</template>
