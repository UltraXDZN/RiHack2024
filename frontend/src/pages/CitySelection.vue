<template>
    <div class="map-container">
        <!-- Created with Inkscape (http://www.inkscape.org/) -->

        <JebeniSvg />
        <!-- Add more counties here in the same manner -->
    </div>
</template>

<script>
import JebeniSvg from "../components/JebeniSvg.vue";
export default {
    data() {
        return {
            activeCounty: null, // Tracks which county is clicked
            hoveredCounty: null, // Tracks which county is hovered over
        };
    },
    components: {
        JebeniSvg,
    },
    methods: {
        hoverCounty(county) {
            this.hoveredCounty = county;
        },
        leaveCounty(county) {
            if (this.hoveredCounty === county) {
                this.hoveredCounty = null;
            }
        },
        toggleCounty(county) {
            if (this.activeCounty === county) {
                this.activeCounty = null;
            } else {
                this.activeCounty = county;
            }
        },
    },
};
</script>

<style scoped>
.map-container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100vh;
}

.county {
    pointer-events: all;
    fill: black;
}

.county:hover {
    fill: red;
}
</style>
