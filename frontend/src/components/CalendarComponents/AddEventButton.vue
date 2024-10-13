<template>
  <div class="relative w-16 h-16">
    <!-- Hidden Checkbox Trigger -->
    <input type="checkbox" id="toggle" class="hidden peer" />
    <!-- Main Circle Button -->
    <label for="toggle" class="block relative z-10 w-16 h-16 rounded-full bg-blue-600 shadow-lg transition duration-200 transform hover:bg-blue-500 hover:shadow-xl active:scale-90 active:shadow-md cursor-pointer">
      <!-- Plus Icon -->
      <img src="https://ssl.gstatic.com/bt/C3341AA7A1A076756462EE2E5CD71C11/2x/btw_ic_speeddial_white_24dp_2x.png" alt="plus-icon" class="absolute top-1/2 left-1/2 w-8 h-8 -mt-4 -ml-4 transition-transform transform rotate-180 peer-checked:rotate-45" />
    </label>
    <!-- Sub Buttons -->
    <div class="absolute inset-0 flex items-center justify-center">
      <template v-for="n in 8" :key="n">
        <button
          :class="[
            'absolute h-10 w-10 rounded-full bg-pink-500 shadow-lg transition-all duration-300 transform scale-50 opacity-0',
            getButtonPositionClass(n),
            getButtonTransitionDelay(n),
            'peer-checked:scale-100 peer-checked:opacity-100'
          ]"
        >
          <!-- Content for Sub Button -->
        </button>
      </template>
    </div>
  </div>
</template>

<script>
export default {
  name: "AddEventButton",
  methods: {
    // Determines the position of each sub-button
    getButtonPositionClass(n) {
      switch (n) {
        case 1:
          return '-translate-y-24';
        case 2:
          return 'translate-x-16 -translate-y-16';
        case 3:
          return 'translate-x-24';
        case 4:
          return 'translate-x-16 translate-y-16';
        case 5:
          return 'translate-y-24';
        case 6:
          return '-translate-x-16 translate-y-16';
        case 7:
          return '-translate-x-24';
        case 8:
          return '-translate-x-16 -translate-y-16';
        default:
          return '';
      }
    },
    // Adds staggered animation delays
    getButtonTransitionDelay(n) {
      return `delay-${n * 100}`;
    },
  },
};
</script>

<!-- No custom styles needed -->
