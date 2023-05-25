<template>
  <div>
    <input type="file" @change="uploadFile" ref="fileUploader">
    <button @click="submitFile">Submit</button>
    <p>{{ text }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      text: '',
      selectedFile: null,
    }
  },
  methods: {
    uploadFile(event) {
      this.selectedFile = event.target.files[0];
    },
    submitFile() {
      let formData = new FormData();
      formData.append('file', this.selectedFile);
      
      axios.post('http://localhost:3000/upload', formData)
        .then((res) => {
          this.text = res.data;
        })
        .catch((err) => console.log(err));
    }
  }
}
</script>
