<script>
import { useAuthStore } from '../store/auth.js'

export default {
  setup() {
    const authStore = useAuthStore()

    return {
      authStore
    }
  },
  methods: {
    async logout() {
      if (this.authStore) {
        try {
          await this.authStore.logout()
        } catch (error) {
          console.error(error)
        }
      } else {
        console.error('Auth store is not initialized')
      }
    },
    async goToLogin() {
      // Redirect to Django's /login page
      window.location.href = '/login'
    },
    async goToRegister() {
      window.location.href = '/register'
    }
  },
  async mounted() {
    try {
      if (this.authStore && this.authStore.fetchUser) {
        await this.authStore.fetchUser()
      } else {
        console.error('fetchUser method is undefined on authStore')
      }
    }
    catch (error) {
      console.error(error)
    }
  }
}
</script>

<template>
  <div>
    <!-- Hero Section -->
    <section class="bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 text-white min-h-screen flex items-center">
      <div class="container mx-auto px-6 py-16 text-center">
        <h1 class="text-5xl md:text-6xl font-bold mb-6">Dobrodošli u Moj eGrad</h1>
        <p class="text-xl md:text-2xl mb-8">Socijalna mreža za lokalne ljude </p>
        <div class="flex justify-center space-x-4">
          <button @click="goToLogin" class="bg-transparent border border-white px-6 py-3 rounded-full font-semibold hover:bg-white hover:text-blue-600 transition duration-300">
            Ulogirajte se
          </button>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section class="py-20 bg-gray-100">
      <div class="container mx-auto px-6">
        <h2 class="text-4xl font-bold text-black text-center mb-12">Naše značajke</h2>
        <div class="flex flex-wrap -mx-4">
          <div class="w-full md:w-1/3 px-4 mb-8">
            <div class="bg-white rounded-lg shadow p-6 text-center">
              <div class="mb-4">
                <svg class="w-12 h-12 text-blue-600 mx-auto" fill="currentColor" viewBox="0 0 24 24">
                  <!-- Icon -->
                </svg>
              </div>
              <h3 class="text-2xl text-black font-semibold mb-2">E-tržnica</h3>
              <p class="text-gray-600">Kupujte od lokalnih OPG-a </p>
            </div>
          </div>
          <div class="w-full md:w-1/3 px-4 mb-8">
            <div class="bg-white rounded-lg shadow p-6 text-center">
              <div class="mb-4">
                <svg class="w-12 h-12 text-purple-600 mx-auto" fill="currentColor" viewBox="0 0 24 24">
                  <!-- Icon -->
                </svg>
              </div>
              <h3 class="text-2xl text-black font-semibold mb-2">Lokalne vjesti</h3>
              <p class="text-gray-600">Saznajte sve lokalne novosti </p>
            </div>
          </div>
          <div class="w-full md:w-1/3 px-4 mb-8">
            <div class="bg-white rounded-lg shadow p-6 text-center">
              <div class="mb-4">
                <svg class="w-12 h-12 text-pink-600 mx-auto" fill="currentColor" viewBox="0 0 24 24">
                  <!-- Icon -->
                </svg>
              </div>
              <h3 class="text-2xl text-black font-semibold mb-2">Lokalni događaji</h3>
              <p class="text-gray-600">Budite obavješteni o svim lokalnim događajima</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-800 text-gray-400 py-8">
      <div class="container mx-auto px-6 text-center">
      </div>
    </footer>
  </div>
</template>

<style scoped>
/* You can add custom styles here if needed */
</style>

