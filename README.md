
# vue-client-recaptcha
Build simple recaptcha for vuejs without need server
![vue-client-recaptcha](https://i.postimg.cc/1fF5NyVV/captcha.png)
## Dependencies
- required: Vuejs >= 3.x

## Installation
```bash
npm install vue-client-recaptcha --save
```
```bash
yarn add vue-client-recaptcha
```
## Usage
1. You can import globally in your vue-3 project (main.js)

```javascript
import { createApp } from 'vue'
import VueClientRecaptcha from 'vue-client-recaptcha'

const app= createApp(App)
app.component("VueClientRecaptcha", VueClientRecaptcha);  
```
2. You can import localy in your vue-3 component
```javascript
import VueClientRecaptcha from 'vue-client-recaptcha'

<!--Optional style.css-->
import 'vue-client-recaptcha/dist/style.css';

export default {
  components: {
    VueClientRecaptcha,
  },
}
```

## Props

| Name                  | Description                                                       | Type       | Default               |
| --------------------  | -------------------------------------------------------------------------------------------------------------------- | --------   | ------------------------|
| value                   | send the value with the component and check the entered value correctly                            | `string`   | ``                                                                |
| chars               | characters that captcha should be made with.                              | `string` | `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`                                                                
| count  | number of character | `number`  | `5`   
| hideLines  | hide dirty line and make captcha simple | `boolean`  | `false`   
| customTextColor  | set text color for all characters | `string`  | ``   
| textColors  | set random text color for each character in array of list | `string[]`  | ``   
| width  | width of captcha | `any`  | `count * 30`
| height  | width of captcha | `number`  | `50`
| canvasClass  | can set custom class for canvas | `string`  | ``
                                                                                                          
## Events

| Event            | Value  | Description                                    |
| ---------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `@isValid` | Boolean | can listen to payload , if your value and captcha code same return True otherwise return False |
| `@getCode` | String | can listen to payload , get captcha value and set variable |
## Slots

| Name    | Description |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `icon`  | can set your custom template for icon  or changed to text (default icon is 'refresh' from fontawsome also you can change it with props  |     
###  Examples
```html
<template>
  <div class="sample-captcha">
    <input type="text" v-model="inputValue" />

    <VueClientRecaptcha
      :value="inputValue"
      @getCode="getCaptchaCode"
      @isValid="checkValidCaptcha"
    />
  </div>
</template>

<script>
import { ref } from "vue";
import VueClientRecaptcha from "vue-client-recaptcha";
import "vue-client-recaptcha/dist/style.css";
export default {
  components: {
    VueClientRecaptcha,
  },
  setup() {
    /* pass value to captcha  */
    const inputValue = ref(null);

    const getCaptchaCode = (value) => {
      /* you can access captcha code */
      console.log(value);
    };
    const checkValidCaptcha = (value) => {
      /* expected return boolean if your value and captcha code are same return True otherwise return False */
      console.log(value);
    };
    return {
      inputValue,
      getCaptchaCode,
      checkValidCaptcha,
    };
  },
};
</script>

```
####  SampleSimpleMode
```html
<template>
  <div class="sample-captcha">
    <input type="text" v-model="inputValue" />
    <!-- Hide Letters And Show NumbersOnly Without Lines -->
    <!-- Can Set Your Custom Icon Or Text With Slot -->
    <VueClientRecaptcha
      :value="inputValue"
      :count="4"
      chars="12345"
      :hideLines="true"
      custom-text-color="black"
      @getCode="getCaptchaCode"
      @isValid="checkValidCaptcha"
    >
      <template #icon>
       <span style="color:blue">with Custom Text Or Icon</span> 
        </template>
    </VueClientRecaptcha>
  </div>
</template>

<script>
import { ref } from "vue";
import VueClientRecaptcha from "vue-client-recaptcha";
import "vue-client-recaptcha/dist/style.css";
export default {
  components: {
    VueClientRecaptcha,
  },
  setup() {
    /* pass value to captcha  */
    const inputValue = ref(null);

    const getCaptchaCode = (value) => {
      /* you can access captcha code */
      console.log(value);
    };
    const checkValidCaptcha = (value) => {
      /* expected return boolean if your value and captcha code are same return True otherwise return False */
      console.log(value);
    };
    return {
      inputValue,
      getCaptchaCode,
      checkValidCaptcha,
    };
  },
};
</script>
```
####  SampleWithCustomLetter
```html
<template>
  <div class="sample-captcha">
    <input type="text" v-model="inputValue" />
    <!-- Hide CapitalCase And Number And Set Custom Carachters -->
    <!-- Set 10 Charachter -->
    <VueClientRecaptcha
      :value="inputValue"
      chars="!@#$%^&*"
      :count="10"
      @getCode="getCaptchaCode"
      @isValid="checkValidCaptcha"
    />
  </div>
</template>

<script>
import { ref } from "vue";
import VueClientRecaptcha from "vue-client-recaptcha";
import "vue-client-recaptcha/dist/style.css";
export default {
  components: {
    VueClientRecaptcha,
  },
  setup() {
    /* pass value to captcha  */
    const inputValue = ref(null);

    const getCaptchaCode = (value) => {
      /* you can access captcha code */
      console.log(value);
    };
    const checkValidCaptcha = (value) => {
      /* expected return boolean if your value and captcha code are same return True otherwise return False */
      console.log(value);
    };
    return {
      inputValue,
      getCaptchaCode,
      checkValidCaptcha,
    };
  },
};
</script>
```

####  SampleWithListOfColorsAndOptionAPI
```html
<template>
  <div class="sample-captcha">
    <input type="text" v-model="inputValue" />

    <!-- create list for carachters and select random color for each item -->
    <VueClientRecaptcha
      :value="inputValue"
      :textColors="[
        'blue',
        'red',
        'purple',
        'green',
        '#e83e8c',
        '#ff5578',
        '#53b29f',
        '#d64a37',
        '#094899',
        '#f64141',
        'rgb(77,190,255)',
      ]"
      @getCode="getCaptchaCode"
      @isValid="checkValidCaptcha"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import VueClientRecaptcha from "./components/vue-client-recaptcha.vue";
export default defineComponent({
  components: {
    VueClientRecaptcha,
  },

  data() {
    return {
      inputValue: null,
    };
  },
  methods: {
    getCaptchaCode(value: string) {
      /* you can access captcha code */
      console.log("captcha code", value);
    },
    checkValidCaptcha(value: string) {
      /* expected return boolean if your value and captcha code are same return True otherwise return False */
      console.log(value);
    },
  },
});
</script>

```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)