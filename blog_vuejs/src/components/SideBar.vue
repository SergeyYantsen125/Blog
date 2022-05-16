<template>
  <div class="col-md-4 content-right">
    <div class="recent">
      <h3>RECENT POSTS</h3>
      <ul>
        <li><a href="#">Aliquam tincidunt mauris</a></li>
        <li><a href="#">Vestibulum auctor dapibus lipsum</a></li>
        <li><a href="#">Nunc dignissim risus consecu</a></li>
        <li><a href="#">Cras ornare tristiqu</a></li>
      </ul>
    </div>
    <div class="comments">
      <h3>RECENT COMMENTS</h3>
      <ul>
        <li><a href="#">Amada Doe </a> on <a href="#">Hello World!</a></li>
        <li><a href="#">Peter Doe </a> on <a href="#"> Photography</a></li>
        <li><a href="#">Steve Roberts </a> on <a href="#">HTML5/CSS3</a></li>
      </ul>
    </div>
    <div class="clearfix"></div>
    <div class="archives">
      <h3>ARCHIVES</h3>
      <ul>
        <li><a href="#">October 2013</a></li>
        <li><a href="#">September 2013</a></li>
        <li><a href="#">August 2013</a></li>
        <li><a href="#">July 2013</a></li>
      </ul>
    </div>
    <div class="categories">
      <h3> Категории </h3>
      <ul>
        <li v-for="category in $store.getters.get_category" :key="category.id"><a href="#">{{ category.name }}</a></li>
      </ul>
    </div>
    <div class="clearfix"></div>
  </div>
</template>

<script>
export default {
  name: "SideBar",
}
</script>

<style scoped>

</style>