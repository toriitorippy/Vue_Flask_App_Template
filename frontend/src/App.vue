<template>
  <div id="app">
    <el-menu :default-active="activeIndex" mode="horizontal" router class="menuBar">
      <el-col :span="20" class="menuItemWrapper">
        <el-menu-item index="home" :route="{ name:'home' }">Home</el-menu-item>
        <el-menu-item index="random" :route="{ name:'random' }">Random</el-menu-item>
      </el-col>
    </el-menu>
    <router-view />
  </div>
</template>

<!--region script-->
<script>
export default {
  name: 'app',
  data () {
    return {
      activeIndex: this.$route.name,
    }
  }
}
</script>
<!--endregion-->

<!--region style-->
<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
}
a {
  text-decoration: none;
}
</style>

<style>
#app {
  width: 100vw;
  height: 100vh;
}
.menuBar {
  width: 100vw;
  max-height: 60px;
  padding-bottom: 1px;
}
.menuItemWrapper {
  display: flex;
}
.imageWrapper {
  width: 100%;
  text-align: right;
  pointer-events: none;
}
.imageItem {
  justify-content: flex-end;
}
img {
  width: auto;
  height: 100%;
  object-fit: contain;
}
</style>
<!--endregion-->
