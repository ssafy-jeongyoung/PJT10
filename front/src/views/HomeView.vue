<template>
  <div class="container ">
    <div class="row box">
      <div class="col-8">
        <h1>소개내용</h1>
      </div>
      <div class="col-4">
        <h1>그림</h1>
      </div>
    </div>
  </div>
  <homeAccount  />
  <homechangeMoney />

</template>

<script setup>
  import homeAccount from '@/components/homeAccount.vue'
  import homechangeMoney from '@/components/homechangeMoney.vue'

</script>

<style  scoped>
.box{
  height: 500px;
}
</style>