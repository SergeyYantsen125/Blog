<template>
  <head>
    <link href='http://fonts.googleapis.com/css?family=Oswald:100,400,300,700' rel='stylesheet' type='text/css'>
    <link href='http://fonts.googleapis.com/css?family=Lato:100,300,400,700,900,300italic' rel='stylesheet'
          type='text/css'>
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"
          integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <meta name="keywords" content="Personal Blog Responsive web template, Bootstrap Web Templates, Flat Web Templates, Andriod Compatible web template,
	Smartphone Compatible web template, free webdesigns for Nokia, Samsung, LG, SonyErricsson, Motorola web design"
    />
  </head>
  <Header/>
  <router-view/>
  <Footer/>


</template>

<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";


export default {
  name: 'App',
  components: {Footer, Header},
  mounted() {
    let recaptchaScript = document.createElement('script')
    recaptchaScript.setAttribute('src', 'http://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js')
    document.head.appendChild(recaptchaScript),
    this.$store.dispatch('login_name'),
    this.$store.dispatch('load_category')
    this.$store.dispatch('load_tags')

  },
}
</script>

<style>
@import "assets/css/bootstrap.css";
@import "assets/css/style.css";
@import "assets/css/font-awesome.css";
@import "assets/css/font-awesome.min.css";
</style>


