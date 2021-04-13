<template>
  <div>
    <v-container fluid>
      <v-layout column>
        <v-flex xs12>
          <h3 class="subject">what is your plan?</h3>
        </v-flex>
        <v-flex column>
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
              v-model="title"
              :counter="64"
              label="Title"
              required
            ></v-text-field>
            <v-text-field
              v-model="content"
              :counter="255"
              label="Content"
              required
            ></v-text-field>

            <v-btn @click="create" style="background: green">create</v-btn>
            <v-btn @click="clear" style="background: red">clear</v-btn>
          </v-form>
        </v-flex>

        <v-flex class="todoList" column>
          <v-card max-width="600" tile>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Title</v-list-item-title>
                <v-list-item-subtitle>content</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
export default {};
</script>

<style>
.subject {
  color: blue;
  font-style: oblique;
  padding: 30px;
  text-align: center;
}
.todoList {
  margin: 30px 0px 30px 0px;
}
</style>