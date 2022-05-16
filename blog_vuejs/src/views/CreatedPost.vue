<template>
  <div class="container">
    <div class="row">
      <div class="col-md-8 single-main">
        <div class="mb-3">
          <label for="tagline_lable" class="form-label">Заголовок поста</label>
          <input class="form-control" id="tagline_text" v-model="titletext">
        </div>
        <div class="mb-3">
          <label for="short_descripthion_lable" class="form-label">Краткое описание поста</label>
          <input class="form-control" id="short_descripthion_text" v-model="short_descripthion">
        </div>
        <div class="mb-3">
          <label for="descripthion_lable" class="form-label ">Текст поста</label>
          <textarea class="form-control text_dis" id="descripthion_text"
                    placeholder="Напишите всё о чем думаете здесь" v-model="descripthion"></textarea>
        </div>
        <div class="mb-3">
          <label for="url_lable" class="form-label">URL</label>
          <input class="form-control" id="url_text" v-model="url">
        </div>
        <div class="mb-3">
          <label for="Image_file" class="form-label">Фото к посту</label>
          <input class="form-control image_url" ref="image" type="file" id="formFile" @change="pr_image">
        </div>
        <div class="form-check">
          <input class="form-check-input" type="checkbox" value="True" id="flexCheckChecked" v-model="publish">
          <label class="form-check-label" for="flexCheckChecked">
            Опубликовать
          </label>
        </div>
        <div class="input-group mb-3">
          <label class="input-group-text" for="inputGroupSelect01">Выберите категорию</label>
          <select class="form-select" id="inputGroupSelect01" v-model="category">
            <option :value="cat.name" v-for="cat in $store.getters.get_category">{{ cat.name }}</option>
          </select>
        </div>
        <label class="form-label" for="inputGroupSelect01">Выберите теги</label>
        <select class="form-select" multiple aria-label="Выберите теги" v-model="tag">
          <option v-for="tag in $store.getters.get_tags">{{ tag.name }}</option>
        </select>
        {{ image }}
        <button @click="send_foto" type="button" class="btn btn-primary btn-lg">Создать</button>
      </div>
      <SideBar/>
    </div>
  </div>
</template>

<script>
import SideBar from "@/components/SideBar";

export default {
  name: "CreatedPost",
  components: {SideBar},
  data() {
    return {
      tag: null
    }
  },
  methods: {
    pr_image() {
      this.image = this.$refs.image.files[0]
    },
    async send_foto() {

      let data_post = {
        title: this.titletext,
        short_descripthion: this.short_descripthion,
        descripthion: this.descripthion,
        url: this.url,
        publish: this.publish,
        image: this.image,
        tag: this.tag,
        category: this.category
      }

      let formData = new FormData()
      for (let [key, value] of Object.entries(data_post)) {
        formData.append(key, value)
      }
      console.log(formData)
      let response = await fetch(`${this.$store.getters.getServerUrl}/post/created/`, {
        method: 'POST',
        headers: {
              'Authorization': `Token ${this.$store.getters.get_token}`
            },
        body: formData,
      });

      // сервер ответит подтверждением и размером изображения
      let result = await response.json();
      console.log(result)
    }
  }
}
</script>

<style scoped>
.container {
  padding: 1rem;
}

.text_dis {
  height: 200px;
}

.input-group {
  padding: 0.5rem;
}

.btn-lg {
  margin-top: 2rem;
}

</style>