<template>
  <v-data-table
    :headers="headers"
    :items="desserts"
    :items-per-page="5"
    class="elevation-1"
  >
  <template v-slot:item.actions="{ item }">
			<v-icon small class="mr-2" @click="showItem(item)">
				mdi-pencil
			</v-icon>
			<v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
		</template>
  </v-data-table>
</template>

<script>
  export default {
    data () {
      return {
        headers: [
          {
            text: '任务ID',
            align: 'start',
            sortable: false,
            value: 'id',
          },
          { text: '任务描述', value: 'remark' },
          { text: 'Actions', value: 'actions', sortable: false },
        ],
        desserts: [
          {
            id: '1',
            remark: '任务1',
          },
          {
            id: '2',
            remark: '任务2',
          },
        ],
      }
    },
    methods:{
        showItem(item){
            this.editedIndex = this.desserts.indexOf(item)
			this.editedItem = Object.assign({}, item)
			this.dialog = true
        },
        close() {
			this.dialog = false
			this.$nextTick(() => {
				this.editedItem = Object.assign({}, this.defaultItem)
				this.editedIndex = -1
			})
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
        closeDelete() {
			this.dialogDelete = false
			this.$nextTick(() => {
				this.editedItem = Object.assign({}, this.defaultItem)
				this.editedIndex = -1
			})
		},
    }
  }
</script>
