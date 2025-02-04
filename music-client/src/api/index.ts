/*
 * @Author: Mxu
 * @Date: 2022-09-12 09:52:27
 * @LastEditTime: 2022-10-04 11:42:55
 * @Description: 
 */
import { getBaseURL, get, post, deletes, put, patch } from "./request";

const HttpManager = {
  // 获取图片信息(前端负责拼接url)
  // attachImageUrl: (url) => url ? `${getBaseURL()}/${url}` : "https://cube.elemecdn.com/e/fd/0fc7d20532fdaf769a25683617711png.png",
  // 获取图片信息(由后端进行拼接url，前端无需操作)
  attachImageUrl: (url) => url ? url : "https://cube.elemecdn.com/e/fd/0fc7d20532fdaf769a25683617711png.png",

  // =======================> 用户 API
  // 登录
  signIn: (params) => post(`auth/login`, params),
  // 注册
  SignUp: (params) => post(`user/`, params),
  // 删除用户
  deleteUser: (id) => get(`user/delete?id=${id}`),
  // 更新用户信息
  updateUserMsg: (params) => put(`user/`, params),
  updateUserPassword: (params) => patch(`user/`, params),
  // 获取当前用户详细信息
  getUserInfo: () => get('user/'),
  // 返回指定ID的用户
  getUserOfId: (id) => get(`user/detail?id=${id}`),
  // 更新用户头像
  uploadUrl: (userId) => `${getBaseURL()}/user/avatar/update?id=${userId}`,

  // =======================> 歌单 API
  // 获取全部歌单
  getSongList: (params={}) => get("songList", params),
  // 获取歌单类型
  getSongListOfStyle: (params) => get(`songList/style/detail`, params),
  // 返回标题包含文字的歌单
  getSongListOfLikeTitle: (keywords) => get(`songList/likeTitle/detail?title=${keywords}`),
  // 返回歌单里指定歌单ID的歌曲
  getListSongOfSongId: (songListId) => get(`listSong/detail?songListId=${songListId}`),

  // =======================> 歌手 API
  // 返回所有歌手
  getAllSinger: () => get("singer"),
  // 通过性别对歌手分类
  getSingerOfSex: (sex) => get(`singer/sex/detail?sex=${sex}`),

  // =======================> 收藏 API
  // 返回的指定用户ID的收藏列表
  getCollectionOfUser: (userId) => get(`collection/detail?userId=${userId}`),
  // 添加收藏的歌曲 type: 0 代表歌曲， 1 代表歌单
  setCollection: (params) => post(`collection/add`, params),

  deleteCollection: (userId, songId) => deletes(`collection/delete?userId=${userId}&&songId=${songId}`),

  isCollection: (params) => post(`collection/status`, params),

  // =======================> 评分 API
  // 提交评分
  setRank: (params) => post(`rankList/add`, params),
  // 获取指定歌单的评分
  getRankOfSongListId: (songListId) => get(`rankList?songListId=${songListId}`),
  // 获取指定用户的歌单评分
  getUserRank: (consumerId, songListId) => get(`/rankList/user?consumerId=${consumerId}&songListId=${songListId}`),

  // =======================> 评论 API
  // 添加评论
  setComment: (params) => post(`comment/add`, params),
  // 删除评论
  deleteComment: (id) => get(`comment/delete?id=${id}`),
  // 点赞
  setSupport: (params) => post(`comment/like`, params),
  // // 返回所有评论(后期移除)
  // getAllComment: (type, id) => {
  //   let url = "";
  //   if (type === 1) {
  //     url = `comment/songList/detail?songListId=${id}`;
  //   } else if (type === 0) {
  //     url = `comment/song/detail?songId=${id}`;
  //   }
  //   return get(url);
  // },
  // 返回评论
  getSongListComment: (type, id) => {
    let url = "";
    // type为1时获取歌单评论
    if (type === 1) {
      url = `songList/${id}/comments`;
    } else if (type === 0) {  // type为0时返回歌曲评论
      url = `song/${id}/comments`;
    }
    return get(url);
  },

  // =======================> 歌曲 API
  // 返回指定歌曲ID的歌曲
  getSongOfId: (id) => get(`song/detail?id=${id}`),
  // 返回指定歌单中的歌曲详细信息
  getSongsByListID: (songListID) => get(`songList/${songListID}/songs`),
  // 返回指定歌手ID的歌曲
  getSongOfSingerId: (id) => get(`song/singer/detail?singerId=${id}`),
  // 返回指定歌手名的歌曲
  getSongOfSingerName: (keywords) => get(`song/singerName/detail?name=${keywords}`),
  // 下载音乐
  downloadMusic: (url) => get(url, { responseType: "blob" }),
};

export { HttpManager };
