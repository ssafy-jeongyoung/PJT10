<template>
  <div class="row box">
    <div class="col-2">
      <h1>사진 들어갈자리</h1>
    </div>
    <div class="col-10" style="background-color: wheat;">
      <div class="row">
        <div class="col-1"></div>
        <div class="box2 col-10 ">
          정기예금 정기적금 자유적금
        </div>
        <div class="col-11 offset-1"> 은행별 탭</div>
        <div class="col-11 offset-1">각 예금리스트나올곳(예금리스트컴포넌트)</div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue';

const campus =ref("구미")
</script>

<style scoped>
  .box{
    height: 600px;
    background-color: lightblue;
  }

  .box2{
    height: 100px;
    background-color: lightgray;
  }
  .tetemp{
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;

  }

</style>