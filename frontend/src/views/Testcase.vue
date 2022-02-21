<template>
	<v-data-table
        v-model="selected"
		:headers="headers"
		:items="desserts"
		sort-by="id"
		item-key="id"
		show-select
		class="elevation-1"
	>
		<template v-slot:top>
			<v-toolbar flat>
				<v-toolbar-title>测试用例</v-toolbar-title>
				<v-divider class="mx-4" inset vertical></v-divider>
				<v-spacer></v-spacer>
				<template>
					<v-btn color="success" dark class="mb-2" @click="executeCase"> 执行用例 </v-btn>
				</template>
				<v-dialog v-model="dialog" max-width="500px">
					<template v-slot:activator="{ on, attrs }">
						<v-btn
							color="primary"
							dark
							class="mb-2"
							v-bind="attrs"
							v-on="on"
						>
							新建用例
						</v-btn>
					</template>
					<v-card>
						<v-card-title>
							<span class="text-h5">{{ formTitle }}</span>
						</v-card-title>

						<v-card-text>
							<v-container>
								<v-row>
									<v-col cols="12" sm="6" md="4">
										<v-text-field
											v-model="editedItem.id"
											label="用例ID"
										></v-text-field>
									</v-col>
									<v-col cols="12" sm="6" md="4">
										<v-text-field
											v-model="editedItem.nodeid"
											label="nodeId"
										></v-text-field>
									</v-col>
									<v-col cols="12" sm="6" md="4">
										<v-text-field
											v-model="editedItem.remark"
											label="用例备注"
										></v-text-field>
									</v-col>
								</v-row>
							</v-container>
						</v-card-text>

						<v-card-actions>
							<v-spacer></v-spacer>
							<v-btn color="blue darken-1" text @click="close">
								取消
							</v-btn>
							<v-btn color="blue darken-1" text @click="save">
								保存
							</v-btn>
						</v-card-actions>
					</v-card>
				</v-dialog>
				<v-dialog v-model="dialogDelete" max-width="500px">
					<v-card>
						<v-card-title class="text-h5"
							>确认是否删除该项?</v-card-title
						>
						<v-card-actions>
							<v-spacer></v-spacer>
							<v-btn
								color="blue darken-1"
								text
								@click="closeDelete"
								>取消</v-btn
							>
							<v-btn
								color="blue darken-1"
								text
								@click="deleteItemConfirm"
								>确定</v-btn
							>
							<v-spacer></v-spacer>
						</v-card-actions>
					</v-card>
				</v-dialog>
			</v-toolbar>
		</template>
		<template v-slot:item.actions="{ item }">
			<v-icon small class="mr-2" @click="editItem(item)">
				mdi-pencil
			</v-icon>
			<v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
		</template>
	</v-data-table>
</template>
<script>
export default {
	data: () => ({
		selected: [],
		dialog: false,
		dialogDelete: false,
		headers: [
			{ text: '用例ID', value: 'id' },
			{ text: 'nodeId', value: 'nodeid' },
			{ text: '用例备注', value: 'remark' },
			{ text: 'Actions', value: 'actions', sortable: false },
		],
		desserts: [],
		editedIndex: -1,
		editedItem: {
			id: '',
			nodeid: '',
			remark: '',
		},
		defaultItem: {
			id: '',
			nodeid: '',
			remark: '',
		},
	}),

	computed: {
		formTitle() {
			return this.editedIndex === -1 ? '新建用例' : '编辑用例'
		},
	},

	watch: {
		dialog(val) {
			val || this.close()
		},
		dialogDelete(val) {
			val || this.closeDelete()
		},
	},

	created() {
		this.initialize()
	},

	methods: {
		initialize() {
			this.desserts = [
				{
					id: 1,
					nodeid: 'test_nodeid1',
					remark: 'remark',
				},
				{
					id: 2,
					nodeid: 'test_nodeid3',
					remark: 'remark',
				},
				{
					id: 3,
					nodeid: 'test_nodeid2',
					remark: 'remark',
				},
			]
		},

		editItem(item) {
			this.editedIndex = this.desserts.indexOf(item)
			this.editedItem = Object.assign({}, item)
			this.dialog = true
		},

		deleteItem(item) {
			this.editedIndex = this.desserts.indexOf(item)
			this.editedItem = Object.assign({}, item)
			this.dialogDelete = true
		},

		deleteItemConfirm() {
			//TODO
			console.log('删除用例')
			this.desserts.splice(this.editedIndex, 1)
			this.closeDelete()
		},

		close() {
			this.dialog = false
			this.$nextTick(() => {
				this.editedItem = Object.assign({}, this.defaultItem)
				this.editedIndex = -1
			})
		},

		closeDelete() {
			this.dialogDelete = false
			this.$nextTick(() => {
				this.editedItem = Object.assign({}, this.defaultItem)
				this.editedIndex = -1
			})
		},

		save() {
			if (this.editedIndex > -1) {
				console.log('编辑用例')
				//   Object.assign(this.desserts[this.editedIndex], this.editedItem)
			} else {
				console.log('新建用例')
				//   this.desserts.push(this.editedItem)
			}
			this.close()
		},
        executeCase() {
            console.log(this.selected)
            console.info("执行用例")
        }
	},
}
</script>
