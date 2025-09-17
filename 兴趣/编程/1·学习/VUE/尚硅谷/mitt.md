
### 前言

用Mitt进行组件传值几乎可以解决vue组件传值的所有问题
例如：兄弟传兄弟父传子/子传父孙子传爷爷。

### 介绍
mitt 又称事务总线，是第三方插件。 Vue 2. X 使用 EventBus 进行组件通信，而 **Vue 3. X 推荐使用 mitt. Js**。点击 [Mitt](https://www.npmjs.com/package/mitt) 了解更多

### 安装 `mitt`

```shell
npm i mitt
```

新建文件：`src\utils\emitter.ts`

```javascript
// 引入mitt 
import mitt from "mitt";

// 创建emitter
const emitter = mitt()

/*
  // 绑定事件
  emitter.on('abc',(value)=>{
    console.log('abc事件被触发',value)
  })
  emitter.on('xyz',(value)=>{
    console.log('xyz事件被触发',value)
  })

  setInterval(() => {
    // 触发事件
    emitter.emit('abc',666)
    emitter.emit('xyz',777)
  }, 1000);

  setTimeout(() => {
    // 清理事件
    emitter.all.clear()
  }, 3000); 
*/

// 创建并暴露mitt
export default emitter
```

接收数据的组件中：绑定事件、同时在销毁前解绑事件：

```typescript
import emitter from "@/utils/emitter";
import { onUnmounted } from "vue";

// 绑定send-toy事件，send-toy名称自定义
emitter.on('send-toy',(value)=>{
  console.log('send-toy事件被触发',value)
})

onUnmounted(()=>{
  // 解绑事件
  emitter.off('send-toy') 
})
```


```vue
<template>

<div class="child2">
<h3>子组件2</h3>
<h4>电脑：{{ computer }}</h4>
<h4>哥哥给的玩具：{{ toy }}</h4>
</div>
</template>

  
<script setup lang="ts" name="Child2">
import {ref,onUnmounted} from 'vue'
import emitter from '@/utils/emitter';
// 数据
let computer = ref('联想')
let toy = ref('')

// 给emitter绑定send-toy事件
emitter.on('send-toy',(value:any)=>{
toy.value = value
})

// 在组件卸载时解绑send-toy事件
onUnmounted(()=>{
emitter.off('send-toy')
})
</script>

```


提供数据的组件，在合适的时候触发事件

```javascript
import emitter from "@/utils/emitter";

function sendToy(){
  // 触发事件
  emitter.emit('send-toy',toy.value)
}
```


```vue
<template>

<div class="child1">
<h3>子组件1</h3>
<h4>玩具：{{ toy }}</h4>
<button @click="emitter.emit('send-toy', toy)">玩具给弟弟</button>
</div>
</template>

  

<script setup lang="ts" name="Child1">
import { ref } from "vue";
import emitter from "@/utils/emitter";

// 数据
let toy = ref("奥特曼");

</script>
```



**注意这个重要的内置关系，总线依赖着这个内置关系**