<template>
  <h1 class="mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-900 md:text-5xl lg:text-6xl dark:text-white">
    Kalendar događanja
  </h1>
  <EventForm/>
  <div>

    <div id="calendar" class="transform w-[420px] h-[570px] mx-auto overflow-hidden">
      <div class="header h-[50px] w-[420px] bg-gray-800 text-center relative z-10">
        <h1 class="m-0 p-0 text-lg leading-[50px] font-extralight tracking-wider">{{ month }}</h1>
        <div
            class="left absolute w-0 h-0 border-solid border-transparent border-t-0 border-b-[15px] border-r-[20px] top-1/2 -mt-[7.5px] cursor-pointer left-5"
            @click="prevMonth">
          <FontAwesomeIcon :icon="faArrowLeft()"/>
        </div>
        <div
            class="right absolute w-0 h-0 border-solid border-transparent border-t-0 border-b-[15px] border-l-[20px] top-1/2 -mt-[7.5px] cursor-pointer right-5"
            @click="nextMonth">
          <FontAwesomeIcon :icon="faArrowRight()"/>
        </div>
      </div>

      <div class="week bg-gray-700 flex justify-between">
        <div v-for="day in weekDays" :key="day"
             class="day-name text-[9px] uppercase mb-1 text-white opacity-50 tracking-[.7px]">{{ day }}
        </div>
      </div>

      <div class="month opacity-100 transition-opacity duration-1000">
        <div
            v-for="(day, index) in days"
            :key="day.date || Math.random()"
            :class="[
            'day inline-block w-[60px] p-[10px] text-center align-top cursor-pointer relative',
            day.isOtherMonth ? 'text-gray-400' : 'text-white',
            day.isToday ? 'text-blue-400' : ''
          ]"
            @click="selectDay(day, index)"
        >
          <div class="day-number text-[24px] tracking-[1.5px]">{{ day.number }}</div>
          <ul class="day-events list-none mt-[3px] text-center h-[12px] leading-[6px] overflow-hidden">
            <li
                v-for="event in day.events"
                :key="event.id"
                :class="['inline-block p-0 m-0 w-[5px] h-[5px] leading-[5px] mx-1', event.color]"
            ></li>
          </ul>
        </div>

        <!-- Event pop-up -->
        <div v-if="selectedDay" :style="popupStyle" class="details bg-gray-600 text-white rounded-md p-3 mt-2 relative">
          <div :style="arrowStyle"
               class="arrow absolute w-0 h-0 border-solid border-transparent border-b-gray-600"></div>
          <ul class="events">
            <li v-for="event in selectedDay.events" :key="event.id" @click="openEvent(event.id)" class="event">
              {{ event.label }}
            </li>
            <li v-if="!selectedDay.events.length" class="event empty">No events</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <EventInfo
      v-if="selectedEvent"
      :is-modal-open="isEventModalOpen"
      :title="selectedEvent.title"
      :description="selectedEvent.description"
      :start_time="selectedEvent.start_time"
      :end_time="selectedEvent.end_time"
      :location="selectedEvent.location"
      @close-modal="closeEventModal"
  />


</template>

<script>
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'
import {faArrowLeft} from "@fortawesome/free-solid-svg-icons/faArrowLeft";
import {faArrowRight} from "@fortawesome/free-solid-svg-icons";
import AddEventButton from "@/components/CalendarComponents/AddEventButton.vue";
import EventForm from "@/components/CalendarComponents/EventForm.vue";
import EventInfo from "@/components/CalendarComponents/EventInfo.vue";

export default {
  components: {EventForm, EventInfo, AddEventButton, FontAwesomeIcon},
  data() {
    return {
      currentDate: new Date(),
      month: '',
      weekDays: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
      days: [],
      selectedDay: null, // For storing the clicked day
      selectedRow: -1, // For tracking the row of the clicked day
      selectedCol: -1, // For tracking the column of the clicked day
      selectedEvent: {}, // For storing the clicked event,
      isEventModalOpen: false,

    };
  },
  computed: {
    popupStyle() {
      if (this.selectedDay) {
        const index = this.days.indexOf(this.selectedDay);
        const row = Math.floor(index / 7);
        return {
          gridRow: `${row + 2}`, // Adjust row (1 for header, 1 for day names)
        };
      }
      return {};
    },
    arrowStyle() {
      if (this.selectedDay && this.selectedCol >= 0) {
        const col = this.selectedCol; // Column index of the selected day (0 to 6)
        const leftPosition = (col * 60) + 10; // 60px per column, plus padding for positioning
        return {
          left: `${leftPosition}px`, // Move the arrow to be under the selected day
          top: '-7px', // Position the arrow above the pop-up div
        };
      }
      return {};
    },
  },
  created() {
    this.updateCalendar();
  },
  methods: {
    faArrowRight() {
      return faArrowRight
    },
    faArrowLeft() {
      return faArrowLeft
    },
    async updateCalendar() {
      const year = this.currentDate.getFullYear();
      const month = this.currentDate.getMonth();

      // Set the month label (e.g., "October 2024")
      this.month = this.currentDate.toLocaleString('default', {month: 'long', year: 'numeric'});

      // Get the first day of the month and total days in the month
      const firstDayOfMonth = new Date(year, month, 1).getDay();
      const totalDaysInMonth = new Date(year, month + 1, 0).getDate();

      // Get the total days of the previous month
      const totalDaysInPrevMonth = new Date(year, month, 0).getDate();

      this.days = [];

      // Add leading days from the previous month to align the calendar
      for (let i = firstDayOfMonth - 1; i >= 0; i--) {
        this.days.push({
          date: new Date(year, month - 1, totalDaysInPrevMonth - i).toISOString().split('T')[0],
          number: totalDaysInPrevMonth - i,
          isToday: false,
          isOtherMonth: true,
          events: [],
        });
      }

      // Loop through the days of the current month
      for (let i = 1; i <= totalDaysInMonth; i++) {
        const date = new Date(year, month, i);
        this.days.push({
          date: date.toISOString().split('T')[0],
          number: i,
          isToday: this.isToday(date),
          isOtherMonth: false,
          events: [],
        });
      }

      // Add trailing days from the next month to fill the grid
      const remainingCells = 42 - this.days.length;
      for (let i = 1; i <= remainingCells; i++) {
        this.days.push({
          date: new Date(year, month + 1, i).toISOString().split('T')[0],
          number: i,
          isToday: false,
          isOtherMonth: true,
          events: [],
        });
      }

      // Fetch events after the days are set
      await this.getEvents();
    },

    isToday(date) {
      const today = new Date();
      return (
          date.getFullYear() === today.getFullYear() &&
          date.getMonth() === today.getMonth() &&
          date.getDate() === today.getDate()
      );
    },
    async getEvents() {
      try {
        const response = await fetch('/api/events/', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        const data = await response.json();
        this.addFetchedEventsToCalendar(data.events);
      } catch (error) {
        console.error('Error fetching events:', error);
      }
    },

    addFetchedEventsToCalendar(events) {
      // Iterate over the events and assign them to the correct days
      events.forEach((event) => {
        const eventDate = event.start_time.split('T')[0]; // Extract the date part from the datetime string
        this.days.forEach((day) => {
          if (day.date === eventDate) {
            day.events.push({
              id: event.id,
              color: 'bg-blue-400', // You can customize this based on event data
              label: event.title,
            });
          }
        });
      });
    },
    selectDay(day, index) {
      if (!day.isOtherMonth) {
        const newRow = Math.floor(index / 7);
        const newCol = index % 7; // Calculate the column index (0 to 6)
        this.selectedRow = newRow;
        this.selectedCol = newCol;
        this.selectedDay = day;
      }
    },
    prevMonth() {
      this.currentDate.setMonth(this.currentDate.getMonth() - 1);
      this.updateCalendar();
      this.clearSelection();
    },
    nextMonth() {
      this.currentDate.setMonth(this.currentDate.getMonth() + 1);
      this.updateCalendar();
      this.clearSelection();
    },
    clearSelection() {
      this.selectedDay = null;
      this.selectedRow = -1;
      this.selectedCol = -1;
    },
    async openEvent(eventId) {
      try {
        const response = await fetch(`/api/events/${eventId}`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        const data = await response.json();
        this.selectedEvent = data.event; // Adjust based on your API response
        this.isEventModalOpen = true;
      } catch (error) {
        console.error('Error fetching event:', error);
      }
    },
    closeEventModal() {
      this.isEventModalOpen = false;
      this.selectedEvent = null;
    },
  },
};
</script>

<style scoped>
.arrow {
  border-width: 0 5px 5px;
  border-color: transparent transparent #ccc transparent;
  transition: left 0.3s ease; /* Smoothly move the arrow */
}

.event {
  font-size: 16px;
  line-height: 22px;
  letter-spacing: .5px;
  min-height: auto;
  overflow-y: auto;
}

.event.empty {
  color: #eee;
}
</style>
