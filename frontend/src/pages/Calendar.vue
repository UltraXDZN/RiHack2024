<template>
  <div id="calendar" class="w-[420px] mx-auto h-[570px] overflow-hidden">
    <!-- Header -->
    <div class="header h-[50px] w-full bg-gray-700 text-center relative z-10">
      <h1 class="m-0 p-0 text-xl leading-[50px] font-thin tracking-wide">{{ currentMonth.format('MMMM YYYY') }}</h1>
      <div @click="prevMonth" class="left absolute w-0 h-0 border-solid top-1/2 -mt-[7.5px] cursor-pointer border-y-[7.5px] border-r-[10px] border-l-0 border-transparent border-r-gray-400 left-5"></div>
      <div @click="nextMonth" class="right absolute w-0 h-0 border-solid top-1/2 -mt-[7.5px] cursor-pointer border-y-[7.5px] border-l-[10px] border-r-0 border-transparent border-l-gray-400 right-5"></div>
    </div>
    <!-- Month -->
    <div class="month">
      <div v-for="(week, weekIndex) in monthWeeks" :key="weekIndex" class="week bg-gray-700">
        <div v-for="day in week" :key="day.format('YYYY-MM-DD')" class="day inline-block w-[60px] p-2 text-center align-top cursor-pointer relative z-10"
             :class="getDayClass(day)"
             @click="openDay(day)">
          <div class="day-name text-xs uppercase mb-1 text-gray-500 tracking-wide">{{ day.format('ddd') }}</div>
          <div class="day-number text-2xl tracking-wide">{{ day.format('DD') }}</div>
          <div class="day-events mt-1 text-center h-3 leading-[6px] overflow-hidden">
            <span v-for="event in getEventsForDay(day)" :key="event.eventName" class="inline-block w-[5px] h-[5px] leading-[5px] mx-[1px]" :class="getColorClass(event.color)"></span>
          </div>
        </div>
        <!-- Details -->
        <div v-if="currentDayDetails && weekContainsDay(week, currentDayDetails)" class="details relative w-full h-[75px] bg-gray-400 mt-1 rounded">
          <div class="arrow absolute -top-1 left-1/2 -ml-[2px] w-0 h-0 border-solid border-t-0 border-b-[5px] border-x-[5px] border-transparent border-b-gray-400 transition-all duration-700"></div>
          <div class="events h-[75px] py-2 overflow-y-auto overflow-x-hidden">
            <div v-for="event in getEventsForDay(currentDayDetails)" :key="event.eventName" class="event text-lg leading-[22px] tracking-wide py-0 px-4 align-top">
              <div class="event-category inline-block w-[10px] h-[10px] mt-1" :class="getColorClass(event.color)"></div>
              <span class="inline-block pl-2">{{ event.eventName }}</span>
            </div>
            <div v-if="getEventsForDay(currentDayDetails).length === 0" class="event empty text-lg leading-[22px] tracking-wide py-0 px-4 align-top text-gray-300">
              <span class="inline-block">No Events</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Legend -->
    <div class="legend absolute bottom-0 w-full h-[30px] bg-gray-600 leading-[30px]">
      <span v-for="calendar in calendars" :key="calendar.name" class="entry relative pl-[25px] text-sm inline-block leading-[30px]">
        {{ calendar.name }}
        <span class="absolute w-[5px] h-[5px] top-[12px] left-[14px]" :class="getColorClass(calendar.color)"></span>
      </span>
    </div>
  </div>
</template>

<script>
import moment from 'moment';

export default {
  name: 'Calendar',
  data() {
    return {
      today: moment(),
      currentMonth: moment().startOf('month'),
      events: [
        { eventName: 'Lunch Meeting w/ Mark', calendar: 'Work', color: 'orange', date: null },
        { eventName: 'Interview - Jr. Web Developer', calendar: 'Work', color: 'orange', date: null },
        { eventName: 'Demo New App to the Board', calendar: 'Work', color: 'orange', date: null },
        { eventName: 'Dinner w/ Marketing', calendar: 'Work', color: 'orange', date: null },
        { eventName: 'Game vs Portland', calendar: 'Sports', color: 'blue', date: null },
        { eventName: 'Game vs Houston', calendar: 'Sports', color: 'blue', date: null },
        { eventName: 'Game vs Denver', calendar: 'Sports', color: 'blue', date: null },
        { eventName: 'Game vs San Diego', calendar: 'Sports', color: 'blue', date: null },
        { eventName: 'School Play', calendar: 'Kids', color: 'yellow', date: null },
        { eventName: 'Parent/Teacher Conference', calendar: 'Kids', color: 'yellow', date: null },
        { eventName: 'Pick up from Soccer Practice', calendar: 'Kids', color: 'yellow', date: null },
        { eventName: 'Ice Cream Night', calendar: 'Kids', color: 'yellow', date: null },
        { eventName: 'Free Tamale Night', calendar: 'Other', color: 'green', date: null },
        { eventName: 'Bowling Team', calendar: 'Other', color: 'green', date: null },
        { eventName: 'Teach Kids to Code', calendar: 'Other', color: 'green', date: null },
        { eventName: 'Startup Weekend', calendar: 'Other', color: 'green', date: null },
      ],
      calendars: [],
      currentDayDetails: null,
    };
  },
  computed: {
    monthDays() {
      const startOfMonth = this.currentMonth.clone().startOf('month').startOf('week');
      const endOfMonth = this.currentMonth.clone().endOf('month').endOf('week');
      const date = startOfMonth.clone().subtract(1, 'day');
      const days = [];
      while (date.isBefore(endOfMonth, 'day')) {
        days.push(date.add(1, 'day').clone());
      }
      return days;
    },
    monthWeeks() {
      const days = this.monthDays;
      const weeks = [];
      for (let i = 0; i < days.length; i += 7) {
        weeks.push(days.slice(i, i + 7));
      }
      return weeks;
    },
  },
  methods: {
    getDayClass(day) {
      const classes = [];
      if(day.month() !== this.currentMonth.month()) {
        classes.push('text-white opacity-30');
      } else if(this.today.isSame(day, 'day')) {
        classes.push('text-blue-400');
      } else {
        classes.push('text-white');
      }
      return classes.join(' ');
    },
    getEventsForDay(day) {
      return this.events.filter(ev => ev.date.isSame(day, 'day'));
    },
    getColorClass(color) {
      const colorMap = {
        'blue': 'bg-blue-500',
        'orange': 'bg-orange-500',
        'green': 'bg-green-500',
        'yellow': 'bg-yellow-500',
      };
      return colorMap[color] || 'bg-gray-500';
    },
    weekContainsDay(week, day) {
      return week.some(d => d.isSame(day, 'day'));
    },
    openDay(day) {
      if(this.currentDayDetails && this.currentDayDetails.isSame(day, 'day')) {
        this.currentDayDetails = null;
      } else {
        this.currentDayDetails = day.clone();
      }
    },
    nextMonth() {
      this.currentMonth.add(1, 'month');
      this.currentDayDetails = null;
    },
    prevMonth() {
      this.currentMonth.subtract(1, 'month');
      this.currentDayDetails = null;
    },
  },
  created() {
    // Assign random dates to events
    this.events.forEach(ev => {
      ev.date = this.currentMonth.clone().date(Math.floor(Math.random() * 28) + 1);
    });

    // Initialize calendars
    const calendarSet = new Set();
    this.events.forEach(ev => {
      calendarSet.add(ev.calendar);
    });
    this.calendars = Array.from(calendarSet).map(calendarName => {
      const color = this.events.find(ev => ev.calendar === calendarName).color;
      return { name: calendarName, color: color };
    });
  },
};
</script>