/*
 * @Author: Mxu
 * @Date: 2022-09-12 09:52:27
 * @LastEditTime: 2022-10-01 11:56:31
 * @Description: 
 */
/* eslint-disable */
declare module "*.vue" {
  import type { DefineComponent } from "vue";
  const component: DefineComponent<{}, {}, any>;
  export default component;
}

declare module "vue/types/vue" {
  import VueRouter, { Route } from "vue-router";

  interface Vue {
    $router: VueRouter;
    $route: Route;
  }
}

interface ResponseBody {
  code: string;
  success: boolean;
  message: string;
  type: string;
  data?: any;

}

interface PaginationResponseBody {
  code: string;
  success: boolean;
  message: string;
  type: string;
  data?: any;
  count: number
}
