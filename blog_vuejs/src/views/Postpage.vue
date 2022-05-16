<template>
  <div class="single">
    <div class="container">
      <div class="row">
        <div class="col-md-8 single-main">
          <div class="single-grid">
            <img :src=post.image alt=""/>
            <p>{{ post.descripthion }}</p>
            <div class="Like">
              <i :class="ViewLike" aria-hidden="true" @click="loadlike('LK')"> {{ post.number_likes }}</i>
              <i :class="ViewDisLike" aria-hidden="true" @click="loadlike('DLK')"> {{ post.number_dislikes }}</i>
            </div>
          </div>
          <ul class="comment-list">
            <h5 class="post-author_head">Written by <a href="#" title="Posts by admin" rel="author">{{ post.autor }}</a>
            </h5>
            <li><img src="../assets/images/avatar.png" class="img-responsive" alt="">
              <div class="desc">
                <p>View all posts by: <a href="#" title="Posts by admin" rel="author">admin</a></p>
              </div>
              <div class="clearfix"></div>
            </li>
          </ul>
          <Comments :comments="post.post_comment" :post="post.id" @RELOAD="loadpost"/>
        </div>
        <SideBar/>
      </div>
    </div>
  </div>
</template>

<script>
import Comments from "@/components/Comments";
import SideBar from "@/components/SideBar";

export default {
  name: "Postpage",
  components: {SideBar, Comments},
  props: ['url'],
  data() {
    return {
      post: {},
      user: '',
      LK: '',
    }
  },
  computed: {
    ViewLike() {
      return {
        'fa fa-thumbs-up fa-2x': this.user == this.$store.getters.get_user && this.LK == "LK",
        'fa fa-thumbs-o-up fa-2x': this.user != this.$store.getters.get_user || this.LK != "LK"
      }
    },
    ViewDisLike() {
      return {
        'fa fa-thumbs-down fa-2x': this.user == this.$store.getters.get_user && this.LK == "DLK",
        'fa fa-thumbs-o-down fa-2x': this.user != this.$store.getters.get_user || this.LK != "DLK"
      }
    },
  },
  created() {
    this.$store.dispatch('login_name')
    this.loadpost()
  },
  methods: {
    async loadpost() {
      this.post = await fetch(
          `${this.$store.getters.getServerUrl}/post/${this.url}/`,
          {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Token ${this.$store.getters.get_token}`
            },
          }
      ).then(response => response.json())
      console.log(this.post),
          this.load_like_user_post()
      console.log(this.user)
      console.log(this.LK)

    },
    async loadlike(kwarg) {
      let data = {
        coices_like_dislike: kwarg,
        post: this.post.id,
      }
      await fetch(
          `${this.$store.getters.getServerUrl}/like/`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Token ${this.$store.getters.get_token}`
            },
            body: JSON.stringify(data)
          }
      ).then(response => response.json())
      this.loadpost()
    },

    load_like_user_post() {
      if (this.post.post_like_dislike.length >= 1) {
        for (let like of this.post.post_like_dislike) {
          if (like.put == this.$store.getters.get_user) {
            this.user = like.put;
            this.LK = like.coices_like_dislike;
            break
          } else {
            this.user = '';
            this.LK = '';
          }
        }
      } else {
        this.user = '';
        this.LK = '';
      }
    }
  }
}

</script>


<style scoped>

</style>