<template>
  <div class="mainbox">
    <div class="row box">
      <div class="col-1 "></div>
      <div class="col-2">
        <h1>개인  사진 들어갈자리</h1>
      </div>
      <div class="col-1 "></div>
      <div class="col-7 tetemp">

          <div>
            이름
          </div>
          <br>
          <div>
            이메일
          </div>
          <br>
          <div>
            캠퍼스
          </div>
        <br>
        <div>
          기수
        </div>
        <br>
        <div>
          저축가능금액
        </div>
        <br>
        <div>
          <a href="">회원정보 수정</a>
        </div>
        <br>
    </div>
    <div class="col-1 temp"></div>
    </div>
    <div class="row tempbox">
      <div>
        <RouterLink to="/" class="space"> 내가 가입한 상품 </RouterLink>
        <RouterLink to="/" class="space">가입한 상품 비교</RouterLink>
      </div>

    </div>
    <h1>라우터뷰 들어갈 자리</h1>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const campus =ref("구미")
</script>

<style scoped>
  .box{
    height: 300px;
    background-color: lightblue;
  }

  .tempbox{
    background-color: black;
  }
  .tetemp{
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;

  }
  .mainbox{
    display: flex;
    flex-direction: column;
  }
</style>