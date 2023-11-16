<template>
  <div class="row box">
    <div class="col-1 temp"></div>
    <div class="col-5">
      <h1>사진 들어갈자리</h1>
    </div>
    <div class="col-1 temp"></div>
    <div class="col-4 tetemp">
      <form >
        <div>
          <input type="text" placeholder="ID">
        </div>
        <br>
        <div>
          <input type="text" placeholder="password">
        </div>
        <br>
        <div>
          <input type="submit" value="로그인">
        </div>
        <div>
          <a href="">회원가입</a>
        </div>
        <br>
        <div>
          <a href="">ID/password 찾기</a>
        </div>
      </form>
    </div>
    <div class="col-1 temp"></div>
  </div>
</template>

<script setup>

</script>

<style scoped>
  .box{
    height: 600px;
    background-color: lightblue;
  }
  .temp{
    background-color: white;
  }

  .tetemp{
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;

  }

</style>