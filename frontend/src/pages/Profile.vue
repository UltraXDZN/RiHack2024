<template>
    <div class="bg-zinc-900">
        <!-- Profile Header -->
        <div
            class="max-w-4xl mx-auto bg-stone-900 rounded-lg shadow-md p-6 mt-12"
        >
            <!-- Adjusted margin-top -->

            <div class="flex items-center">
                <!-- Profile Picture -->
                <img
                    class="w-24 h-24 rounded-full object-cover border-4 border-gray-300"
                    src="https://via.placeholder.com/150"
                    alt="Profile Picture"
                />

                <!-- User Info -->
                <div class="ml-6">
                    <p v-if="user">
                    <h2 class="text-2xl font-semibold text-slate-50">
                        {{ user.username }}
                    </h2>
                    </p>
                    <p v-else>
      Not logged in
    </p>
                    <p class="text-slate-100">{{ userdata.title }}</p>
                    <!--<p class="text-slate-100 text-sm mt-1">
                        Joined: {{ userdata.joinDate }}
                    </p>-->
                </div>
            </div>
        </div>

        <!-- Profile Content -->
        <div class="max-w-4xl mx-auto mt-6 space-y-6">
            <!-- About Section -->
            <div class="bg-stone-900 rounded-lg shadow-md p-6">
                <h3 class="text-xl font-semibold text-slate-100">Moje zajednice</h3>
                <p class="mt-4 text-slate-100">{{ selectedLocations }}</p>
            </div>

            <!-- Contact Info Section -->
            <div class="bg-stone-900 rounded-lg shadow-md p-6">
                <h3 class="text-xl font-semibold text-slate-100">
                    Contact Info
                </h3>
                <ul class="mt-4 space-y-2 text-slate-50">
                    <li v-if="user"><strong>Email:</strong> {{ user.email }}</li>
                </ul>
            </div>

            <!-- Recent Activity Section -->
            <!--<div class="bg-stone-900 rounded-lg shadow-md p-6">
                <h3 class="text-xl font-semibold text-slate-100">
                    Recent Activity
                </h3>
                <ul class="mt-4 space-y-2 text-slate-100">
                    <li
                        v-for="(activity, index) in userdata.recentActivities"
                        :key="index"
                    >
                        {{ activity }}
                    </li>
                </ul>
            </div>-->
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            userdata: {
                name: "John Doe",
                title: "Software Developer",
                joinDate: "January 1, 2020",
                about: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada.",
                email: "johndoe@example.com",
                phone: "(555) 123-4567",
                location: "New York, USA",
                recentActivities: [
                    "Posted a new blog article",
                    "Started following Jane Smith",
                    "Commented on 'Vue.js vs React: A Comparison'",
                    "Updated profile picture",
                ],
            },
            user: null,selectedLocations: null,
      errorMessage: null,
        };
    },methods: {
    fetchUserData() {
      axios
        .get('/api/user')
        .then((response) => {
          this.user = response.data;
        })
        .catch((error) => {
          if (error.response && error.response.status === 401) {
            this.errorMessage = error.response.data.message;
          } else {
            console.error('An error occurred:', error);
          }
        });
    },    fetchSelectedLocations() {
      axios
        .get('/api/locations/selected')
        .then((response) => {
            this.selectedLocations = response.data.selected_cities;
            this.selectedLocations=this.selectedLocations.join(', ');

        })
        .catch((error) => {
          console.error('An error occurred:', error);
        });
    
  },
  },
    mounted() {
        this.fetchUserData();
    this.fetchSelectedLocations();
    },
  
};
</script>

<style scoped>
/* Optionally, you can include any additional styling here */
</style>
