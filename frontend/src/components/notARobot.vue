<template>
  <div class="captcha">
    <div class="challenge"> Click the button below to verify that you are not a robot: </div>
    <button @click="verify"> Verify </button>

    <div class="modal-overlay" v-if="showFirst">
      <div class="modal">
        <div class="modal-content">
          <p><h5> Please translate the sentence accurately to Korean </h5></p>
          <p><h5> 문장을 한국어로 정확히 번역해 주세요 </h5></p> 
          <br/>
          <h2><strong> {{ firstPrompt }} </strong></h2>
          <textarea id="message" name="message" rows="4" wrap="soft"></textarea>
          <br/>
          <div v-if="this.firstError === true" class="fail-message">
            Try again!
          </div>
          <button @click="firstAuth"> Check </button>
        </div>
      </div>
    </div>

    <div class="modal-overlay" v-if="showSecond">
      <div class="modal">
        <div class="modal-content">
          <p><h5> Please translate the sentence accurately to Korean </h5></p>
          <p><h5> 문장을 한국어로 정확히 번역해 주세요 </h5></p> 
          <br/>
          <h2><strong> {{ secondPrompt }} </strong></h2>
          <textarea id="message" name="message" rows="4" wrap="soft"></textarea>
          <br/>
          <button @click="secondAuth"> Check </button>
        </div>
      </div>
    </div>

    <div v-if="verified" class="success-message">
      Verified! You are not a robot.
    </div>
  </div>
</template>

<script>
  import axios from "axios";

  const rest = axios.create({
    baseURL: "http://localhost:80/api",
  });

  export default {
    data() {
      return {
        verified: false,
        showFirst: false,
        showSecond: false,
        firstError: false,
        firstPrompt: "",
        firstPromptID: 0,
        secondPrompt: "",
        secondPromptID: 0,
      };
    },
    methods: {
      async firstAuth() {
        const messageTextarea = document.getElementById("message");
        const text = messageTextarea.value;
        const response = await rest.post("/first", {"prompt_id": this.firstPromptID, "translation": text});

        if (response.data.score >= 0.75) {
          this.firstError = false;
          this.showFirst = false;
          this.showSecond = true;
        }
        else {
          this.firstError = true;
        }
      },
      async secondAuth() {
        const messageTextarea = document.getElementById("message");
        const text = messageTextarea.value;
        const response = await rest.post("/second", {"prompt_id": this.secondPromptID, "translation": text});
        this.showSecond = false;
        setTimeout(() => {
          this.verified = true;
        }, 1000);
      },
      verify() {
        this.showFirst = true
      },
      async getFirstPrompt() {
        const response = await rest.get("/first");
        this.firstPrompt = response.data.prompt_text;
        this.firstPromptID = response.data.prompt_id;
      },
      async getSecondPrompt() {
        const response = await rest.get("/second");
        this.secondPrompt = response.data.prompt_text;
        this.secondPromptID = response.data.prompt_id;
      },
    },
    created() {
      this.getFirstPrompt();
      this.getSecondPrompt();
    },
  };
</script>

<style scoped>
  .captcha {
    text-align: center;
    margin: 50px;
  }
  .challenge {
    margin-bottom: 10px;
  }
  .success-message {
    color: green;
    margin-top: 10px;
  }
  .fail-message {
    color: red;
    margin-top: 10px;
  }
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  }
</style>
