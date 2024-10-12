<script>
export default {
  name: "NewsCard"
}
</script>

<template>
  <div class="max-w-sm mx-auto bg-gray-800 rounded-lg shadow-lg overflow-hidden">
    <!-- Image -->
    <img
      class="w-full h-48 object-cover"
      src="https://via.placeholder.com/300x200"
      alt="Boxing image"
    />

    <!-- Content -->
    <div class="p-4">
      <!-- Title -->
      <h2 class="text-white text-lg font-semibold truncate">
        The Sweet Science Unveiled: A Ringside Journey
      </h2>
      <!-- Subtitle -->
      <p class="text-gray-400 mt-2 text-sm">
        Step Into The Boxing Ring: Stories, Strategies, And The Unyielding Spirit Of Champions
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
          <p>James</p>
          <p class="text-xs">August 18, 2023</p>
        </div>
      </div>
    </div>
  </div>
</template>