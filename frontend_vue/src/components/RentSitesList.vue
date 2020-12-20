<template>
  <div>
      <h4>Rent sites List from API</h4>
      <ul class="list-group">
        <li v-for="(rentsite, index) in rentsites" :key="index">
          {{ rentsite.name }}
        </li>
      </ul>
  </div>

</template>

<script>
import RentDataService from "../services/RentDataService"
export default {
    name: "rentsites-list",
    data() {
        return {
            rentsites: [],
        }
    },
    methods: {
        retriveRentSites() {
            RentDataService.getAll().then(response => {
                this.rentsites = response.data;
                console.log(response.data);
            })
            .catch(e => {
                console.log(e)
            })
        }
    },

    mounted() {
        this.retriveRentSites();
    }
}
</script>

<style>

</style>