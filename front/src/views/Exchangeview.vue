<template>
  <div class="makespace">
    <h1>환율 계산기</h1>
    <form>
      <div>
        원하는 나라의 금액 {{ store }}
        <input type="text" v-model="wantMount">
        <select @change="findwantDealbasr(wantMoney)" v-model="wantMoney">
          <option value="미국 달러">달러</option>
          <option value="일본 옌">엔</option>
          <option value="유로">유로</option>
          <option value="위안화">위안</option>
          <option value="한국 원">원</option>
        </select>
      </div>
      <br>
      <div>
        필요한 금액 <div>{{ resultMount }}</div>
        <select @change="findrequiredDealbasr(selectedCountry)" v-model="selectedCountry">
          <option value="미국 달러">달러</option>
          <option value="일본 옌">엔</option>
          <option value="유로">유로</option>
          <option value="위안화">위안</option>
          <option value="한국 원">원</option>
        </select>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useCounterStore } from '@/stores/counter';

const wantMount = ref('0');
const want_dela_bas_r = ref('0');
const required_dela_bas_r = ref('0');
const wantMoney = ref('달러');
const selectedCountry = ref('');
const store = useCounterStore();

onMounted(() => {
  store.getExchangeData();
});

const findwantDealbasr = function(keyNAME) {
  const temp = store.exchangeData.filter(item => item.cur_nm === keyNAME);
  want_dela_bas_r.value = temp[0].deal_bas_r.replace(/,/g, '');
};

const findrequiredDealbasr= function(keyName) {
  const temp = store.exchangeData.filter(item => item.cur_nm === keyName);
  required_dela_bas_r.value = temp[0].deal_bas_r.replace(/,/g, '');
};

const resultMount = computed(() => {
  console.log(want_dela_bas_r.value)
  console.log(required_dela_bas_r.value)
  console.log(wantMount.value)
  if (want_dela_bas_r.value>0 && required_dela_bas_r.value>0 && wantMount.value>0) {
    return (parseInt(wantMount.value) * parseFloat(want_dela_bas_r.value)) / parseFloat(required_dela_bas_r.value);
  } 
 return ''; // 결과값이 없는 경우에 대한 처리

  
});

</script>

<style scoped>
  .makespace {
    padding: 40px;
  }
</style>
