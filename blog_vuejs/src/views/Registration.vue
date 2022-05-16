<template>
  <div class="limiter" id="login">
    <div class="container-login100"
         style="background-image:url(https://nevseoboi.com.ua/uploads/posts/2012-06/1339238297-403945-0119027_www.nevseoboi.com.ua.jpg)">
      <div class="container">
        <div class="row">
          <div class="col-md-6"></div>
          <div class="col-md-5 col-md-offset-1">
            <div class="login_topimg">
            </div>
            <div class="wrap-login100">
              <form class="login100-form validate-form"><span class="login100-form-title "> Login </span> <span
                  class="login100-form-subtitle m-b-16"> to your account </span>
                <div class="wrap-input100 validate-input m-b-16" data-validate="Valid email is required: ex@abc.xyz">
                  <input class="input100" type="text" name="Username" placeholder="Username" v-model="username">
                  <span class="focus-input100"></span> <span class="symbol-input100">
                  <span class="glyphicon glyphicon-user">
                  </span></span>
                </div>
                <div class="wrap-input100 validate-input m-b-16" data-validate="Valid email is required: ex@abc.xyz">
                  <input class="input100" type="text" name="email" placeholder="Email" v-model="email">
                  <span class="focus-input100"></span> <span class="symbol-input100">
                  <span class="glyphicon glyphicon-user">
                  </span></span>
                </div>
                <div class="wrap-input100 validate-input m-b-16" data-validate="Password is required"><input
                    class="input100" type="password" name="pass" placeholder="Password" v-model="password"> <span
                    class="focus-input100"></span> <span class="symbol-input100"> <span
                    class="glyphicon glyphicon-lock"></span> </span>
                </div>
                <div class="container-login100-form-btn p-t-25">
                  <button type="button" class="login100-form-btn" @click="send_registration">Sign up</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Registration",
  methods: {
    send_registration() {
      let data = {
        username: this.username,
        password: this.password,
        email: this.email
      }
      this.$store.dispatch('register', data)
          .then(() => this.$router.push('/'))
          .catch(err => console.log(err))
      console.log(data)
    },
  }
}
</script>

<style scoped>

</style>