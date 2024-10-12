<template>
  <div>
    <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
      <div class="flex items-center mb-6 text-2xl font-semibold">
        <img class="w-8 h-8 mr-2 rounded-full" src="https://static-cdn.jtvnw.net/jtv_user_pictures/4b51af1b-ceef-43ce-b954-33a91fd5cbb8-profile_image-70x70.png" alt="logo">
        <p class="text-4xl leading-none text-white">
          FooBar
        </p>
      </div>
      <div class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
          <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
            Login to your account
          </h1>
          <form class="space-y-4 md:space-y-6" @submit.prevent="login">
            <div>
              <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your email</label>
              <input v-model="email" type="email" name="email" id="email" required class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@company.com" @input="resetError">
            </div>
            <div>
              <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
              <input v-model="password" type="password" name="password" id="password" required placeholder="••••••••" class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" @input="resetError">
            </div>
            <button type="submit" class="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
              Login
            </button>
            <p class="text-sm font-light text-gray-500 dark:text-gray-400">
              Don’t have an account yet?
              <a href="/register" class="font-medium text-primary-600 hover:underline dark:text-primary-500">Register here</a>
            </p>
            <p v-if="error" class="text-red-500">{{ error }}</p>
            <p v-if="success" class="text-green-500">{{ success }}</p>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useAuthStore } from '../store/auth';

export default {
  setup() {
    const authStore = useAuthStore(); // Correctly initialize the auth store here
    return { authStore };
  },
  data() {
    return {
      email: "",
      password: "",
      error: "",
      success: ""
    };
  },
  methods: {
    async login() {
      try {
        const result = await this.authStore.login(this.email, this.password);
        this.success = "Login successful. Redirecting...";

        // Redirect to login page after success
        setTimeout(() => {
          window.location.href = "/";
        }, 1500);
      } catch (error) {
        this.error = "Login failed. Please check your credentials.";
        this.success = ''; // Clear success message on error
        throw error;
      }
    },
    resetError() {
      this.error = "";
    }
  }
};
</script>
