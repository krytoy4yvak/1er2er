<template>
  <div class="container">
    <div class="alert alert-warning alert-dismissible fade show" role="alert">
      <strong>Ошибка 520</strong> Ошибка сделано специально и без вреда для приложения, закройте алерт :)
      <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    <form class="pt-3">
      <div class="form-group">
        <label for ="User name">User Name</label>
        <input
          type="name"
          id="User name"
          class="form-control is"
          :class="{'is-invalid': $v.name.$error} "
          @input="$v.name.$touch()"
          v-model="name"
        >
        <div class="invalid-feedback" v-if="!$v.name.minLength">Имя студента должно быть больше четырёх символов</div>
        <button class="btn btn-primary" type="submit">Найти</button>
      </div>
      <div class="form-group">
      <label for ="mag">mag</label>
      <input
        type="mag"
        id="mag"
        class="form-control is"
        :class="{'is-invalid': $v.mag.$error} "
        @input="$v.mag.$touch()"
        v-model="mag"
      >
      <div class="invalid-feedback" v-if="!$v.mag.minLength">Имя университета должно быть больше четырёх символов</div>
        <button class="btn btn-primary" type="submit">Найти</button>

        <div class="form-group">
        <label for ="prod">prod</label>
        <input
          type="searchprod"
          id="prod"
          class="form-control is"
          :class="{'is-invalid': $v.prod.$error} "
          @input="$v.prod.$touch()"
          v-model="prod"
        >
          <div class="invalid-feedback" v-if="!$v.prod.minLength">Имя универа должно быть больше четырёх символа</div>

      <button class="btn btn-primary" type="submit">Найти</button>
      <table class="table">
        <thead class="thead-dark">
        <tr>
          <th scope="col">#</th>
          <th scope="col">Имя</th>
          <th scope="col">Фамилия</th>
        </tr>
        </thead>
        <tbody>
        <tr>
          <th scope="row">1</th>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <th scope="row">3</th>
          <td></td>
          <td></td>
        </tr>
        </tbody>
      </table>

      <table class="table">
        <thead class="thead-dark">
        <tr>
          <th scope="col">#</th>
          <th scope="col">Университет</th>
        </tr>
        </thead>
        <tbody>
        <tr>
          <th scope="row">1</th>
          <td></td>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td></td>
        </tr>
        <tr>
          <th scope="row">3</th>
          <td></td>
        </tr>
        </tbody>
      </table>
          <table class="table">
            <thead class="thead-dark">
            <tr>
              <th scope="col">#</th>
              <th scope="col">Факультет</th>
            </tr>
            </thead>
            <tbody>
            <tr>
              <th scope="row">1</th>
              <td></td>
            </tr>
            <tr>
              <th scope="row">2</th>
              <td></td>
            </tr>
            <tr>
              <th scope="row">3</th>
              <td></td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
  import { required, minLength } from 'vuelidate/lib/validators'

  export default {
    data() {
      return {
        name: '',
        mag: '',
        prod: ''
      }
    },
    validations:{
      name: {
        required:required,
        minLength: minLength(4)
      },
      mag: {
        required:required,
        minLength: minLength(4)
      },
      prod: {
        required:required,
        minLength: minLength(1)
      },
    }
  }
</script>

<!-- CSS libraries -->
<style src="normalize.css/normalize.css"></style>

<!-- Global CSS -->
<style>
  code {
    font-family: Menlo, Monaco, Lucida Console, Liberation Mono, DejaVu Sans Mono, Bitstream Vera Sans Mono, Courier New, monospace, serif;
    font-size: 0.9em;
    white-space: pre-wrap;
    color: #2c3e50;
  }

  code::before, code::after {
    content: '`';
  }
</style>

<!-- Scoped component css -->
<!-- It only affect current component -->
<style scoped>
  #app {
    text-align: center;
  }

  #app h1 {
    color: #2c3e50;
    font-weight: 300;
    margin: 0;
  }

  .banner {
    height: 200px;
    background-color: #f6f6f6;
    padding: 50px 10px;
  }

  .bottom {
    padding: 80px 10px;
    font-size: 24px;
    font-weight: 300;
  }

  .fade {
    font-size: 14px;
  }

  .logo {
    animation: spin 4s 1s infinite linear
  }

  @keyframes spin {
    from {transform:rotate(0deg);}
    to {transform:rotate(360deg);}
  }
</style>
