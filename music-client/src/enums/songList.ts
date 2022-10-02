/*
 * @Author: Mxu
 * @Date: 2022-09-12 09:52:27
 * @LastEditTime: 2022-10-02 08:51:45
 * @Description: 
 */
export const SONGSTYLE = [
  {
    name: "全部歌单",
    type: "One",
  },
  {
    name: "华语",
    type: "Two",
  },
  {
    name: "粤语",
    type: "Three",
  },
  {
    name: "欧美",
    type: "Four",
  },
  {
    name: "日韩",
    type: "Five",
  },
  {
    name: "轻音乐",
    type: "Six",
  },
  {
    name: "BGM",
    type: "Seven",
  },
  {
    name: "乐器",
    type: "Eight",
  },
];


// 首页获取数据时，一次所能够获取到的最大数量
export const PAGELIMIT_HOME = 10

// 歌单、歌手页获取数据时，一次所能够获取到的最大数量
export const PAGELIMIT_INFO = 15