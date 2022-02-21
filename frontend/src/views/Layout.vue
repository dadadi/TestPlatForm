<template>
<!-- App.vue -->
<v-app>
    <v-navigation-drawer app>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            测试平台
          </v-list-item-title>
          <v-list-item-subtitle>
            HXY
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title @click='switchTab(item)'>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  <v-app-bar app>
    <div>v-app-bar</div>
  </v-app-bar>

  <!-- 根据应用组件来调整你的内容 -->
  <v-main>
      <!-- 如果使用 vue-router -->
      <router-view></router-view>
  </v-main>

    <v-footer app>
        <div>footer</div>
    </v-footer>
</v-app>
</template>
<script>
export default {
    data () {
      return {
        items: [
          { title: '测试用例', icon: 'mdi-view-dashboard',router:'testcase' },
          { title: '测试报告', icon: 'mdi-image',router:'task' }
        ],
        right: null,
      }
    },
    methods:{
        switchTab(item){
            this.$router.push({name: item.router})
        }
    }
  }
</script>
