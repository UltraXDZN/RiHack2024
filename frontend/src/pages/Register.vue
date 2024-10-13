<template>
    <div>
    <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
      <div class="flex items-center mb-6 text-2xl font-semibold">
        <img class="w-8 h-8 mr-2 rounded-full" src="@/assets/logo.png" alt="logo">
        <p class="text-4xl leading-none text-white">
          Moj eGrad
        </p>
      </div>
      <div class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
          <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
            Register a new account
          </h1>
          <form class="space-y-4 md:space-y-6" @submit.prevent="register">
            <div>
              <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your email</label>
              <input v-model="email" type="email" name="email" id="email" required class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@company.com" @input="resetError">
            </div>
            <div>
              <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
              <input v-model="password" type="password" name="password" id="password" required placeholder="••••••••" class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" @input="resetError">
            </div>
            <button type="submit" class="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
              Register
            </button>
            <p class="text-sm font-light text-gray-500 dark:text-gray-400">
              Already have an account?
              <a href="/login" class="font-medium text-primary-600 hover:underline dark:text-primary-500">
                Login here
              </a>
            </p>
            <p v-if="error" class="accent-red-500">{{ error }}</p>
          </form>
        </div>
      </div>
    </div>
  </div>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <div>
        <label for="email">Email:</label>
        <input v-model="email" id="email" type="email" required @input="resetError">
      </div>
      <div>
        <label for="password">Password:</label>
        <input v-model="password" id="password" type="password" required @input="resetError">
      </div>
      <button type="submit">Register</button>
    </form>
    <p v-if="error" class="accent-red-500">{{ error }}</p>
    <p v-if="success" class="accent-green-500">{{ success }}</p>
  </div>
</template>

<script>
import { useAuthStore } from '../store/auth'; // Consider using the auth store if needed

export default {
  setup() {
    const authStore = useAuthStore(); // Optional, if you want to manage registration state in store
    return { authStore };
  },
  data() {
    return {
      email: '',
      password: '',
      error: '',
      success: ''
    }
  },
  methods: {
    async register() {
      try {
        // Use the store's register action
        const result = await this.authStore.register(this.email, this.password);
        this.success = result.message;
        this.error = '';

        // Redirect to login page after success
        setTimeout(() => {
          window.location.href = "/login";
        }, 1500);
      } catch (error) {
        this.error = error.message || 'Registration failed';
        this.success = ''; // Clear success message on error
      }
    },
    resetError() {
      this.error = ''; // Reset error message on user input
    }
  }
}
</script>
