<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="max-w-lg w-full bg-white rounded-lg shadow-lg p-8">
      <h1 class="text-4xl font-bold text-gray-800 mb-4">{{ message }}</h1>
      <p class="text-lg text-gray-600">ID: {{ random_id }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: "",
      random_id: "",
    };
  },
  created() {
    // Fetch message from the server when the component is created
    fetch("http://localhost/message")
      .then((response) => response.json())
      .then((data) => {
        this.message = data.message;
        this.random_id = data.random_id;
      })
      .catch((error) => console.error("Error fetching data:", error));
  },
};
</script>

<style>
</style>
