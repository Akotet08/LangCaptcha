<template>
  <div class="container">
    <div class="captcha-box">
      <VueClientRecaptcha :value="inputValue" @getCode="getCaptchaCode" @isValid="checkValidCaptcha" />
      <input v-model="inputValue" placeholder="Enter the code" />
      <button @click="submitCaptcha">Submit</button>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import VueClientRecaptcha from './components/vue-client-recaptcha.vue';

// Reference for the user's input.
const inputValue = ref(null);

// Reference for the actual captcha value.
let actualCaptchaValue = ref('');

const getCaptchaCode = (value) => {
  actualCaptchaValue.value = value;
  console.log('Generated Captcha Code:', value);
};

const checkValidCaptcha = (isValid) => {
  console.log('Is Captcha Valid:', isValid);
};

const submitCaptcha = () => {
  if(inputValue.value === actualCaptchaValue.value) {
    // User input is correct
    console.log('User Input is Correct');
  } else {
    // User input is incorrect
    console.log('User Input is Incorrect');
  }
};
</script>

<style>
.container {
  display: flex;
  height: 100vh;
  align-items: center;
  justify-content: center;
}

.captcha-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  border: 1px solid #ccc;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
</style>
