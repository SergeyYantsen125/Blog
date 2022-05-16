<template>
  <!DOCTYPE html>
  <html>

  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Untitled</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,700">
    <link rel="stylesheet" href="assets/css/style.css">
  </head>

  <body>
  <div>
    <div class="header-blue">
      <nav class="navbar navbar-dark navbar-expand-md navigation-clean-search">
        <div class="container"><a class="navbar-brand" href="/">Blog</a>
          <button class="navbar-toggler" data-toggle="collapse" data-target="#navcol-1"><span class="sr-only">Toggle navigation</span><span
              class="navbar-toggler-icon"></span></button>
          <div class="collapse navbar-collapse"
               id="navcol-1">
            <ul class="nav navbar-nav">
              <router-link to="/CreatedPost">
                <li class="nav-item" role="presentation"><a class="nav-link active" href="">Создать пост</a></li>
              </router-link>
              <div class="dropdown-menu" role="menu"><a class="dropdown-item" role="presentation" href="#">First
                Item</a><a class="dropdown-item" role="presentation" href="#">Second Item</a><a class="dropdown-item"
                                                                                                role="presentation"
                                                                                                href="#">Third
                Item</a></div>
            </ul>
            <form class="form-inline mr-auto" target="_self">
              <div class="form-group"><label for="search-field"><i class="fa fa-search"></i></label><input
                  class="form-control search-field" type="search" name="search" id="search-field"></div>
            </form>
            <div v-if="isLogin != false">
              <router-link to="#">
                <span class="btn btn-light action-button"> <a href="#" class="login">{{ isLogin.username }}</a></span>
              </router-link>
              <a class="navbar-text" role="button" href="#" @click="logout">Выход</a>
            </div>
            <div v-else>
              <router-link to="/Login">
                <span class="navbar-text"> <a href="#" class="login">Вход</a></span>
              </router-link>
              <router-link to="/Registration">
                <a class="btn btn-light action-button" role="button" href="#">Зарегистрироваться</a>
              </router-link>
            </div>
          </div>
        </div>
      </nav>
    </div>
  </div>
  </body>

  </html>
</template>

<script>
export default {
  name: "Header",
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
          .then(() => {
            this.$router.push('/')
          })
    },
  }
}
</script>

<style scoped>
.header-blue {
  background: linear-gradient(135deg, #172a74, #21a9af);
  background-color: #184e8e;
  padding-bottom: 80px;
  font-family: 'Source Sans Pro', sans-serif;
  height: 20px;
}

@media (min-width: 768px) {
  .header-blue {
    padding-bottom: 75px;
  }
}

.header-blue .navbar {
  background: transparent;
  padding-top: .75rem;
  padding-bottom: .75rem;
  color: #fff;
  border-radius: 0;
  box-shadow: none;
  border: none;
}

@media (min-width: 768px) {
  .header-blue .navbar {
    padding-top: 1rem;
    padding-bottom: 1rem;
  }
}

.header-blue .navbar .navbar-brand {
  font-weight: bold;
  color: inherit;
}

.header-blue .navbar .navbar-brand:hover {
  color: #f0f0f0;
}

.header-blue .navbar .navbar-collapse {
  border-top: 1px solid rgba(255, 255, 255, 0.3);
  margin-top: .5rem;
}

@media (min-width: 768px) {
  .header-blue .navbar .navbar-collapse {
    border-color: transparent;
    margin: 0;
  }
}

.header-blue .navbar .navbar-collapse span .login {
  color: #d9d9d9;
  margin-right: .5rem;
  text-decoration: none;
}

.header-blue .navbar .navbar-collapse span .login:hover {
  color: #fff;
}

.header-blue .navbar .navbar-toggler {
  border-color: rgba(255, 255, 255, 0.3);
}

.header-blue .navbar .navbar-toggler:hover, .header-blue .navbar-toggler:focus {
  background: none;
}

.header-blue .navbar .navbar-nav a.active, .header-blue .navbar .navbar-nav > .show .dropdown-item {
  background: none;
  box-shadow: none;
}

@media (min-width: 768px) {
  .header-blue .navbar-nav .nav-link {
    padding-left: .7rem;
    padding-right: .7rem;
  }
}

@media (min-width: 992px) {
  .header-blue .navbar-nav .nav-link {
    padding-left: 1.2rem;
    padding-right: 1.2rem;
  }
}

.header-blue .navbar .navbar-nav > li > .dropdown-menu {
  margin-top: -5px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, .1);
  background-color: #fff;
  border-radius: 2px;
}

.header-blue .navbar .dropdown-menu .dropdown-item:focus, .header-blue .navbar .dropdown-menu .dropdown-item {
  line-height: 2;
  color: #37434d;
}

.header-blue .navbar .dropdown-menu .dropdown-item:focus, .header-blue .navbar .dropdown-menu .dropdown-item:hover {
  background: #ebeff1;
}

.header-blue .action-button, .header-blue .action-button:not(.disabled):active {
  border: 1px solid rgba(255, 255, 255, 0.7);
  border-radius: 40px;
  color: #ebeff1;
  box-shadow: none;
  text-shadow: none;
  padding: .3rem .8rem;
  background: transparent;
  transition: background-color 0.25s;
  outline: none;
}

.header-blue .action-button:hover {
  color: #fff;
}

.header-blue .navbar .form-inline label {
  color: #d9d9d9;
}

.header-blue .navbar .form-inline .search-field {
  display: inline-block;
  width: 80%;
  background: none;
  border: none;
  border-bottom: 1px solid transparent;
  border-radius: 0;
  color: #ccc;
  box-shadow: none;
  color: inherit;
  transition: border-bottom-color 0.3s;
}

.header-blue .navbar .form-inline .search-field:focus {
  border-bottom: 1px solid #ccc;
}

.header-blue .hero {
  margin-top: 20px;
  text-align: center;
}

@media (min-width: 768px) {
  .header-blue .hero {
    margin-top: 60px;
    text-align: left;
  }
}

.header-blue .hero h1 {
  color: #fff;
  font-size: 40px;
  margin-top: 0;
  margin-bottom: 15px;
  font-weight: 300;
  line-height: 1.4;
}

@media (min-width: 992px) {
  .header-blue .hero h1 {
    margin-top: 190px;
    margin-bottom: 24px;
    line-height: 1.2;
  }
}

.header-blue .hero p {
  color: rgba(255, 255, 255, 0.8);
  font-size: 20px;
  margin-bottom: 30px;
  font-weight: 300;
}

.header-blue .phone-holder {
  text-align: right;
}

.header-blue div.iphone-mockup {
  position: relative;
  max-width: 300px;
  margin: 20px;
  display: inline-block;
}

.header-blue .iphone-mockup img.device {
  width: 100%;
  height: auto;
}


.header-blue .iphone-mockup .screen:before {
  content: '';
  background-color: #fff;
  position: absolute;
  width: 70%;
  height: 140%;
  top: -12%;
  right: -60%;
  transform: rotate(-19deg);
  opacity: 0.2;
}


</style>