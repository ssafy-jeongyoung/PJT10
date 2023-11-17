import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios';
export const useCounterStore = defineStore('counter', () => {

  const exchangeData=ref([])
  const getExchangeData=function(){
    axios({
      method: 'get',
      url: '/exchange-api?authkey=XPGg7SsCcJbK24AYwIqwaDNrcIOn3nLa&data=AP01'
    }).then((res) =>{

      exchangeData.value=res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  const getExchange = computed(()=>{
    return exchangeData.value
  })
  return { exchangeData,getExchangeData, getExchange}
})
