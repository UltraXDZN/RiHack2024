<script>
import { useAuthStore } from "../store/auth.js";
import NavBar from "@/components/NavBar.vue";

export default {
    components: { NavBar },
    setup() {
        const authStore = useAuthStore();

        return {
            authStore,
        };
    },
    methods: {
        async logout() {
            if (this.authStore) {
                try {
                    await this.authStore.logout();
                } catch (error) {
                    console.error(error);
                }
            } else {
                console.error("Auth store is not initialized");
            }
        },
        async goToLogin() {
            // Redirect to Django's /login page
            window.location.href = "/login";
        },
        async goToRegister() {
            window.location.href = "/register";
        },
    },
    async mounted() {
        try {
            if (this.authStore && this.authStore.fetchUser) {
                await this.authStore.fetchUser();
            } else {
                console.error("fetchUser method is undefined on authStore");
            }
        } catch (error) {
            console.error(error);
        }
    },
};
</script>

<template>
    <section
        class="bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 text-white min-h-screen flex items-center justify-center"
    >
        <div class="py-16 px-6 mx-auto max-w-screen-2xl text-center w-full">
            <!-- Increased width with max-w-screen-2xl and full width -->
            <div
                class="relative inline-flex items-center justify-between py-1 px-1 pr-4 mb-8 text-sm bg-white bg-opacity-20 rounded-full hover:bg-opacity-30 w-auto"
                role="alert"
            >
                <!-- Alert is still rounded but fits wider space -->
                <span
                    class="text-xs bg-primary-600 rounded-full text-white px-4 py-1.5 mr-3"
                    >New</span
                >
                <span class="text-sm font-medium"
                    >This is FooBar's official hackathon template!</span
                >
                <svg
                    class="ml-2 w-5 h-5"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path
                        fill-rule="evenodd"
                        d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                        clip-rule="evenodd"
                    ></path>
                </svg>
            </div>

            <h1
                class="mb-6 text-5xl font-extrabold leading-tight tracking-tight sm:text-6xl lg:text-7xl"
            >
                Welcome to FooBar!
            </h1>
            <p
                class="mb-8 text-lg font-medium lg:text-xl max-w-4xl mx-auto text-white opacity-80"
            >
                The ultimate platform for your next hackathon project.
            </p>

            <div v-if="authStore && authStore.isAuthenticated">
                <p class="text-2xl font-semibold">
                    Welcome back, {{ authStore.user?.username }}!
                </p>
                <div class="flex justify-center mt-8 space-x-4">
                    <a
                        @click="logout"
                        class="inline-flex justify-center items-center py-3 px-6 text-lg font-medium text-white bg-red-600 rounded-full shadow hover:bg-red-700 focus:ring-4 focus:ring-red-300"
                    >
                        Logout
                        <svg
                            class="ml-2 -mr-1 w-6 h-6"
                            fill="currentColor"
                            viewBox="0 0 20 20"
                            xmlns="http://www.w3.org/2000/svg"
                        >
                            <path
                                fill-rule="evenodd"
                                d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                                clip-rule="evenodd"
                            ></path>
                        </svg>
                    </a>
                </div>
            </div>

            <div v-else>
                <div
                    class="flex flex-col sm:flex-row justify-center mt-8 space-y-4 sm:space-y-0 sm:space-x-4"
                >
                    <a
                        @click="goToLogin"
                        class="inline-flex justify-center items-center py-3 px-6 text-lg font-medium bg-white text-primary-700 rounded-full shadow hover:bg-gray-100 focus:ring-4 focus:ring-primary-300"
                    >
                        Login
                        <svg
                            class="ml-2 -mr-1 w-6 h-6"
                            fill="currentColor"
                            viewBox="0 0 20 20"
                            xmlns="http://www.w3.org/2000/svg"
                        >
                            <path
                                fill-rule="evenodd"
                                d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                                clip-rule="evenodd"
                            ></path>
                        </svg>
                    </a>
                    <a
                        @click="goToRegister"
                        class="inline-flex justify-center items-center py-3 px-6 text-lg font-medium bg-primary-700 text-white rounded-full shadow hover:bg-primary-800 focus:ring-4 focus:ring-primary-300"
                    >
                        Register
                        <svg
                            class="ml-2 -mr-1 w-6 h-6"
                            fill="currentColor"
                            viewBox="0 0 20 20"
                            xmlns="http://www.w3.org/2000/svg"
                        >
                            <path
                                fill-rule="evenodd"
                                d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                                clip-rule="evenodd"
                            ></path>
                        </svg>
                    </a>
                </div>
            </div>
        </div>
    </section>
    <section class="bg-white dark:bg-gray-900">
        <div
            class="py-8 px-4 mx-auto max-w-screen-xl text-center lg:py-16 lg:px-12"
        >
            <a
                href="#"
                class="inline-flex justify-between items-center py-1 px-1 pr-4 mb-7 text-sm text-gray-700 bg-gray-100 rounded-full dark:bg-gray-800 dark:text-white hover:bg-gray-200 dark:hover:bg-gray-700"
                role="alert"
            >
                <span
                    class="text-xs bg-primary-600 rounded-full text-white px-4 py-1.5 mr-3"
                    >New</span
                >
                <span class="text-sm font-medium">
                    This is FooBar's official hackaton template!
                </span>
                <svg
                    class="ml-2 w-5 h-5"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path
                        fill-rule="evenodd"
                        d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                        clip-rule="evenodd"
                    ></path>
                </svg>
            </a>
            <h1
                class="mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-900 md:text-5xl lg:text-6xl dark:text-white"
            >
                This is the home site
            </h1>
            <div v-if="authStore && authStore.isAuthenticated">
                <p>Welcome back, {{ authStore.user?.username }}!</p>
                <div
                    class="flex flex-col mb-8 lg:mb-16 space-y-4 sm:flex-row sm:justify-center sm:space-y-0 sm:space-x-4"
                >
                    <a
                        @click="logout"
                        class="inline-flex justify-center items-center py-3 px-5 text-base font-medium text-center text-white rounded-lg bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:focus:ring-primary-900"
                    >
                        Logout
                        <svg
                            class="ml-2 -mr-1 w-5 h-5"
                            fill="currentColor"
                            viewBox="0 0 20 20"
                            xmlns="http://www.w3.org/2000/svg"
                        >
                            <path
                                fill-rule="evenodd"
                                d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                                clip-rule="evenodd"
                            ></path>
                        </svg>
                    </a>
                </div>
            </div>
            <div v-else>
                <div
                    class="flex flex-col mb-8 lg:mb-16 space-y-4 sm:flex-row sm:justify-center sm:space-y-0 sm:space-x-4"
                >
                    <a
                        @click="goToLogin"
                        class="inline-flex justify-center items-center py-3 px-5 text-base font-medium text-center text-white rounded-lg bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:focus:ring-primary-900"
                    >
                        Login
                        <svg
                            class="ml-2 -mr-1 w-5 h-5"
                            fill="currentColor"
                            viewBox="0 0 20 20"
                            xmlns="http://www.w3.org/2000/svg"
                        >
                            <path
                                fill-rule="evenodd"
                                d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                                clip-rule="evenodd"
                            ></path>
                        </svg>
                    </a>
                    <a
                        @click="goToRegister"
                        class="inline-flex justify-center items-center py-3 px-5 text-base font-medium text-center text-white rounded-lg bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:focus:ring-primary-900"
                    >
                        Register
                        <svg
                            class="ml-2 -mr-1 w-5 h-5"
                            fill="currentColor"
                            viewBox="0 0 20 20"
                            xmlns="http://www.w3.org/2000/svg"
                        >
                            <path
                                fill-rule="evenodd"
                                d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                                clip-rule="evenodd"
                            ></path>
                        </svg>
                    </a>
                </div>
            </div>
        </div>
    </section>
</template>
