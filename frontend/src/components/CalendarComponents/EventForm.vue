<template>
  <div>
    <!-- Modal toggle button -->
    <AddEventButton class="absolute bottom-0 right-0 left-16 mb-4 mr-4" @click="openModal" />

    <!-- Main modal -->
    <div
        v-if="isModalOpen"
        class="fixed top-0 right-0 left-0 z-50 flex items-center justify-center w-full h-full"
        tabindex="-1"
    >
      <!-- Modal content -->
      <div class="relative p-4 w-full max-w-md bg-white rounded-lg shadow dark:bg-gray-700 z-60">
        <!-- Modal header -->
        <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
          <h3 class="text-xl font-semibold text-gray-900 dark:text-white">Add Event</h3>
          <button
              @click="closeModal"
              type="button"
              class="text-gray-400 bg-transparent hover:bg-gray-200 rounded-lg text-sm w-8 h-8 ms-auto flex justify-center items-center dark:hover:bg-gray-600"
          >
            <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M1 1l6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
            </svg>
            <span class="sr-only">Close modal</span>
          </button>
        </div>

        <!-- Modal body -->
        <div class="p-4 md:p-5">
          <form @submit.prevent="submitEvent" class="space-y-4">
            <!-- Event Title -->
            <div>
              <label for="title" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Event
                Title</label>
              <input
                  v-model="form.title"
                  type="text"
                  id="title"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                  placeholder="Enter event title"
                  required
              />
            </div>

            <!-- Event Description -->
            <div>
              <label for="description" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Event
                Description</label>
              <textarea
                  v-model="form.description"
                  id="description"
                  rows="3"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                  placeholder="Enter event description"
              ></textarea>
            </div>

            <!-- Start Time -->
            <div>
              <label for="start_time" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Start
                Time</label>
              <input
                  v-model="form.start_time"
                  type="datetime-local"
                  id="start_time"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                  required
              />
            </div>

            <!-- End Time -->
            <div>
              <label for="end_time" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">End Time
                (optional)</label>
              <input
                  v-model="form.end_time"
                  type="datetime-local"
                  id="end_time"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
              />
            </div>

            <!-- Location -->
            <div>
              <label for="location" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Location
                (optional)</label>
              <input
                  v-model="form.location"
                  type="text"
                  id="location"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                  placeholder="Enter location"
              />
            </div>

            <!-- Submit Button -->
            <button type="submit"
                    class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center">
              Add Event
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AddEventButton from "@/components/CalendarComponents/AddEventButton.vue";

export default {
  components: {AddEventButton},
  data() {
    return {
      isModalOpen: false,
      form: {
        title: '',
        description: '',
        start_time: '',
        end_time: '',
        location: '',
      },
    };
  },
  methods: {
    openModal() {
      this.isModalOpen = true;
    },
    closeModal() {
      this.isModalOpen = false;
    },
    async submitEvent() {
      try {
        const response = await fetch('/api/events/create/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.form),
        });

        if (!response.ok) {
          throw new Error('Failed to create event');
        }

        this.closeModal();
        this.getEvents(); // Refresh events after submission
      } catch (error) {
        console.error('Error creating event:', error);
      }
    },
  },
};
</script>
