<template>
  <button
      data-drawer-target="default-sidebar"
      data-drawer-toggle="default-sidebar"
      aria-controls="default-sidebar"
      type="button"
      class="inline-flex items-center p-2 mt-2 ml-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
  >
    <span class="sr-only">Open sidebar</span>
    <svg
        class="w-6 h-6"
        aria-hidden="true"
        fill="currentColor"
        viewBox="0 0 20 20"
        xmlns="http://www.w3.org/2000/svg"
    >
      <path
          clip-rule="evenodd"
          fill-rule="evenodd"
          d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"
      ></path>
    </svg>
  </button>

  <aside
      id="default-sidebar"
      class="fixed top-0 right-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0"
      aria-label="Sidenav"
  >
    <div
        class="overflow-y-auto py-5 px-3 h-full bg-white border-r border-gray-200 dark:bg-gray-800 dark:border-gray-700"
    >
      <ul class="space-y-2">
        <li>
          <a
              href="#"
              class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group"
          >
            <span class="ml-3 text-left text-lg">{{ croatianCounties[county] }}</span>
          </a>
        </li>
        <hr/>
        <span class="mt-20"/>
        <li v-for="city in cities" :key="city">
          <div class="flex items-center mb-4">
            <input
                id="default-checkbox"
                type="checkbox"
                :value="city"
                v-model="selectedCities"
                class="mx-4 w-6 h-6 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
            />
            <label
                for="default-checkbox"
                class="ms-4 text-sm font-medium text-gray-900 dark:text-gray-300"
            >{{ city }}</label
            >
          </div>
        </li>
      </ul>
    </div>
  </aside>
</template>

<script>
export default {
  props: {
    county: { type: String, required: true },
    cities: { type: Array, required: true },
  },
  data() {
    return {
      selectedCities: [],  // Array to hold selected cities
      croatianCounties: {
        "bjelovarsko-bilogorska": "Bjelovarsko-bilogorska županija",
        "brodsko-posavska": "Brodsko-posavska županija",
        "dubrovacko-neretvanska": "Dubrovačko-neretvanska županija",
        istarska: "Istarska županija",
        karlovacka: "Karlovačka županija",
        "koprivnicko-krizevacka": "Koprivničko-križevačka županija",
        "krapinsko-zagorska": "Krapinsko-zagorska županija",
        "licko-senjska": "Ličko-senjska županija",
        medimurska: "Međimurska županija",
        "osjecko-baranjska": "Osječko-baranjska županija",
        "pozesko-slavonska": "Požeško-slavonska županija",
        "primorsko-goranska": "Primorsko-goranska županija",
        "sibensko-kninska": "Šibensko-kninska županija",
        "sisacko-moslavacka": "Sisačko-moslavačka županija",
        "splitsko-dalmatinska": "Splitsko-dalmatinska županija",
        varazdinska: "Varaždinska županija",
        "viroviticko-podravska": "Virovitičko-podravska županija",
        "vukovarsko-srijemska": "Vukovarsko-srijemska županija",
        zadarska: "Zadarska županija",
        zagrebacka: "Zagrebačka županija",
        "grad-zagreb": "Grad Zagreb",
      },
    };
  },
  methods: {
    async sendSelectedCities() {
      try {
        const response = await fetch('/api/locations/set/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',  // Send as JSON
          },
          body: JSON.stringify({ selected_cities: this.selectedCities }),  // Send selectedCities
        });
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        console.log('Success:', data);
      } catch (error) {
        console.error('Error:', error);
      }
    },
  },
  watch: {
    // Watcher on selectedCities: sends data to backend whenever selectedCities changes
    selectedCities: function(newVal, oldVal) {
      this.sendSelectedCities();
    }
  }
};
</script>

<style scoped>
.sidebar {
  position: fixed;
  right: 0;
  top: 0;
  width: 250px;
  height: 100vh;
  background-color: #f8f9fa;
  padding: 20px;
  box-shadow: -2px 0 5px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
}

h2 {
  margin-bottom: 20px;
  text-align: center;
  font-size: 1.5em;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 10px;
}

label {
  display: flex;
  align-items: center;
  font-size: 1em;
}

input[type="checkbox"] {
  margin-right: 10px;
}
</style>
