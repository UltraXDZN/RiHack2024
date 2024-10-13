<template>
  <div>
    <!-- Main modal -->
    <div
      v-if="isModalOpen"
      class="fixed top-0 right-0 left-0 z-50 flex items-center justify-center w-full h-full bg-black bg-opacity-50"
      tabindex="-1"
    >
      <!-- Modal content -->
      <div class="relative p-4 w-full max-w-md bg-white rounded-lg shadow-lg dark:bg-gray-700">
        <!-- Modal header -->
        <div class="flex items-center justify-between p-4 border-b rounded-t dark:border-gray-600">
          <h3 class="text-xl font-semibold text-gray-900 dark:text-white">{{ title }}</h3>
          <button
            @click="closeModal"
            type="button"
            class="text-gray-400 bg-transparent hover:bg-gray-200 rounded-lg text-sm w-8 h-8 dark:hover:bg-gray-600"
          >
            <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M1 1l6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
            </svg>
            <span class="sr-only">Close modal</span>
          </button>
        </div>

        <!-- Modal body -->
        <div class="p-4">
          <div class="mb-4">
            <label class="block mb-1 text-sm font-medium text-gray-900 dark:text-white">Description:</label>
            <p class="text-gray-700 dark:text-gray-300">{{ description || 'No description available' }}</p>
          </div>

          <div class="mb-4">
            <label class="block mb-1 text-sm font-medium text-gray-900 dark:text-white">Start Time:</label>
            <p class="text-gray-700 dark:text-gray-300">{{ formatDate(start_time) }}</p>
          </div>

          <div class="mb-4">
            <label class="block mb-1 text-sm font-medium text-gray-900 dark:text-white">End Time:</label>
            <p class="text-gray-700 dark:text-gray-300">{{ end_time ? formatDate(end_time) : 'N/A' }}</p>
          </div>

          <div class="mb-4">
            <label class="block mb-1 text-sm font-medium text-gray-900 dark:text-white">Location:</label>
            <p class="text-gray-700 dark:text-gray-300">{{ location || 'No location provided' }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    isModalOpen: {
      type: Boolean,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: false,
      default: '',
    },
    start_time: {
      type: String,
      required: true,
    },
    end_time: {
      type: String,
      required: false,
      default: '',
    },
    location: {
      type: String,
      required: false,
      default: '',
    },
  },
  methods: {
    closeModal() {
      this.$emit('close-modal');
    },
    formatDate(dateString) {
      const options = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
      };
      return new Date(dateString).toLocaleDateString(undefined, options);
    },
  },
};
</script>


<style scoped>
button {
  cursor: pointer;
}

.modal {
  background-color: white;
  border-radius: 8px;
  padding: 16px;
  max-width: 400px;
  margin: 0 auto;
}

.dark-mode .modal {
  background-color: #2d3748;
  color: white;
}
</style>

