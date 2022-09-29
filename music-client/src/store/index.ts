/*
 * @Author: Mxu
 * @Date: 2022-09-12 09:52:27
 * @LastEditTime: 2022-09-29 09:20:12
 * @Description: 
 */
import { createStore, storeKey } from "vuex";
import configure from "./configure";
import user from "./user";
import song from "./song";

const options = {
  modules: {
    configure,
    user,
    song,
  },
}

const store = createStore(options);
export default store;

// 清空vuex所有数据
export function resetStore() {
  store.replaceState(createStore(options).state)
}
