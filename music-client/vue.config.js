/*
 * @Author: Mxu
 * @Date: 2022-09-12 09:52:27
 * @LastEditTime: 2022-09-30 10:35:28
 * @Description: 
 */
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    port: 9001
  },
  chainWebpack: config => {
    config.plugin('define').tap(definitions => {
        Object.assign(definitions[0]['process.env'], {
          NODE_HOST: '"http://api.yinmusic.com"',
        });
        return definitions;
    });
  }

})
