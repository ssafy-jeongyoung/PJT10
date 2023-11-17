<template>
  <div>
    <nav class="box">
      <div class="box2">
        <RouterLink to="/" class="space"><img class="imgsize" src="@/assets/logo.png" alt=""> </RouterLink>
        <RouterLink to="/deposit" class="space"> <h1>예적금 </h1> </RouterLink>
        <RouterLink :to="{name:'exchange'}" class="space"> <h1>환율 </h1> </RouterLink>
        <RouterLink to="/" class="space"> <h1>은행지도 </h1> </RouterLink>
        <RouterLink to="/" class="space"> <h1>커뮤니티 </h1> </RouterLink>

      </div>

    </nav>
  </div>
  <RouterView />
</template>

<script setup>
  import { RouterLink, RouterView } from 'vue-router'

</script>

<style scoped>
  .box {
    display: flex;
    justify-content: center;
  }
  .box2 {
    display: flex;
    width: 100%;
    max-width: 1080px;
    min-width: 1080px;
    height: 90px;
    margin: auto;
    padding-top: 20px;
  }

  .space {
    color: black;
    margin-right: 50px;
    text-decoration: none;
  }
  .imgsize{
    width: 160px;
    height: 60px;
  }
</style>