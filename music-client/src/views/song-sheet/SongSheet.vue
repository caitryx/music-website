<!--
 * @Author: Mxu
 * @Date: 2022-09-12 09:52:27
 * @LastEditTime: 2022-10-02 09:59:12
 * @Description: 
-->
<template>
  <div class="play-list-container">
    <yin-nav :styleList="songStyle" :activeName="activeName" @click="handleChangeView"></yin-nav>
    <play-list :playList="data" path="song-sheet-detail"></play-list>
    <el-pagination
      class="pagination"
      background
      layout="total, prev, pager, next"
      :current-page="currentPage"
      :page-size="pageSize"
      :total="songlistTotalCount"
      @current-change="handleCurrentChange"
    >
    </el-pagination>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from "vue";
import YinNav from "@/components/layouts/YinNav.vue";
import PlayList from "@/components/PlayList.vue";
import { SONGSTYLE, PAGELIMIT_INFO } from "@/enums";
import { HttpManager } from "@/api";

export default defineComponent({
  components: {
    YinNav,
    PlayList,
  },
  setup() {
    const activeName = ref("全部歌单");
    const pageSize = ref(PAGELIMIT_INFO); // 一页的数量
    const currentPage = ref(1); // 当前页
    const songStyle = ref(SONGSTYLE); // 歌单导航栏类别
    const allPlayList = ref([]); // 歌单
    // const data = computed(() => allPlayList.value.slice((currentPage.value - 1) * pageSize.value, currentPage.value * pageSize.value));
    const data = computed(() => allPlayList.value)
    const songlistTotalCount = ref(0)

    // 获取歌单数据
    async function getSongList() {
      const resp = ((await HttpManager.getSongList({offset: (currentPage.value-1)*pageSize.value, limit: pageSize.value})) as PaginationResponseBody)
      allPlayList.value = resp.data;
      songlistTotalCount.value = resp.count
    }
    // 通过类别获取歌单
    async function getSongListOfStyle(style) {
      const param = {style: style, offset: (currentPage.value-1)*pageSize.value, limit: pageSize.value }
      const resp = ((await HttpManager.getSongListOfStyle(param)) as PaginationResponseBody)
      allPlayList.value = resp.data;
      songlistTotalCount.value = resp.count
    }

    try {
      getSongList();
    } catch (error) {
      console.error(error);
    }

    // 获取歌单
    async function handleChangeView(item) {
      activeName.value = item.name;
      allPlayList.value = [];
      // 重置页码
      currentPage.value = 1
      try {
        if (item.name === "全部歌单") {
          await getSongList();
        } else {
          await getSongListOfStyle(item.name);
        }
      } catch (error) {
        console.error(error);
      }
    }
    // 获取当前页
    async function handleCurrentChange(val) {
      currentPage.value = val;
      if (activeName.value == '全部歌单') {
        await getSongList()
      }else {
        await getSongListOfStyle(activeName.value)
      }
      
    }
    return {
      activeName,
      songStyle,
      pageSize,
      currentPage,
      allPlayList,
      data,
      songlistTotalCount,
      handleChangeView,
      handleCurrentChange,
    };
  },
});
</script>
