<template>
  <div class="row box">
    <div class="col-1 "></div>
    <div class="col-2">
      <h1>사진 들어갈자리</h1>
    </div>
    <div class="col-1 "></div>
    <div class="col-7 tetemp">
      <form >
        <div>
          <input type="text" placeholder="이메일">
        </div>
        <br>
        <div>
          <input type="text" placeholder="이름">
        </div>
        <br>
        <div>
          <input type="text" placeholder="password">
        </div>
        <br>
        <div>
          <input type="text" placeholder="password 확인">
        </div>
        <br>
        <select v-model="campus">
          <option value="구미">구미</option>
          <option value="서울">서울</option>
          <option value="부울경">부울경</option>
          <option value="대전">대전</option>
          <option value="광주">광주</option>
        </select>
        <br>
        <br>
        <div>
          <input type="text" placeholder="기수">
        </div>
        <br>
        <div>
          <input type="text" placeholder="저축가능금액">
          <br>
        </div>
        
        <div>
          <a href="">회원가입</a>
        </div>
        <br>

      </form>
    </div>
    <div class="col-1 temp"></div>
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


  .tetemp{
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;

  }

</style>