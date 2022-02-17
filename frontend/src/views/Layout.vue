<template>
	<!-- App.vue -->

	<v-app>
		<v-navigation-drawer app>
			<!-- 抽屉导航 -->
			<v-list-item>
				<v-list-item-content>
					<v-list-item-title class="text-h6">
						测试平台
					</v-list-item-title>
					<v-list-item-subtitle> author：HXY </v-list-item-subtitle>
				</v-list-item-content>
			</v-list-item>

			<v-divider></v-divider>

			<v-list dense nav>
				<v-list-item v-for="item in items" :key="item.title" link
                @click="swithItem(item)">
					<v-list-item-icon>
						<v-icon>{{ item.icon }}</v-icon>
					</v-list-item-icon>

					<v-list-item-content>
						<v-list-item-title>{{ item.title }}</v-list-item-title>
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
	data() {
		return {
			items: [
				{ title: '测试用例', icon: 'mdi-view-dashboard', router:'testcase' },
				{ title: '测试任务', icon: 'mdi-image', router:'task' },
			],
			right: null,
		}
	},
    methods:{
        swithItem(item){
            // 传入切换路由的名称，就会切换到对应的路由地址
            this.$router.push({name:item.router})
        }
    }
}
</script>
