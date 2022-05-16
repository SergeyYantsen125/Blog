<template>
  <div class="content">
    <div class="container">
      <div class="content-grids">
        <div class="row">
          <div class="col-md-8 content-main">
            <div class="content-grid">
              <div class="content-grid-info" v-for="post in listposts">
                <img src="../assets/images/post1.jpg" alt=""/>
                <div class="post-info">
                  <h4><a href="#"></a> {{ post.title }} July 30, 2014 / 27 Comments</h4>
                  <p>{{ post.short_descripthion }}</p>
                  <a href="#" @click="goTo(post.url)"><span></span>READ MORE </a>
                </div>
              </div>


            </div>
          </div>
          <SideBar/>
          <div class="clearfix"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SideBar from "@/components/SideBar";
export default {
  name: "HomePage",
  components: {SideBar},
  data() {
    return {
      listposts: [],
    }
  },
  created() {
    this.loadlistPost()
  },
  methods: {
    async loadlistPost() {
      this.listposts = await fetch(
          `${this.$store.getters.getServerUrl}/posts/` /*{
            headers: {
              Authorization: `Token ${this.$store.getters.get_token}`,*/
      ).then(response => response.json())
      console.log(this.listposts)
    },
    goTo(url) {
      this.$router.push({name: 'Postpage', params: {url: url}})
    },
  }
}
</script>

<style scoped>

</style>