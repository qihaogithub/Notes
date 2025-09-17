### Vue 3中使用IconPark图标库的完整指南

#### 1. 安装IconPark图标库

首先，使用npm或yarn安装`@icon-park/vue-next`包：

```bash
npm install @icon-park/vue-next --save
```

或者

```bash
yarn add @icon-park/vue-next
```

#### 2. 引入IconPark样式

在`src/main.js`文件中引入IconPark的默认样式：

```javascript
import { createApp } from 'vue';
import App from './App.vue';
// 引入IconPark默认样式
import '@icon-park/vue-next/styles/index.css';

const app = createApp(App);

app.mount('#app');
```

#### 3. 配置按需加载

为了实现按需加载图标，需要安装`unplugin-vue-components`（这是一个 Vite 插件，用于自动按需导入 Vue 组件）：

```bash
npm install unplugin-vue-components --save-dev
```

或者

```bash
yarn add unplugin-vue-components --dev
```

### 步骤 2: 配置 Vite 插件

在 Vite 项目中，你需要在 `vite.config.js` 文件中配置 `unplugin-vue-components` 插件。如果你的项目中还没有这个文件，你可以创建它。

在 `vite.config.js` 文件中添加如下配置：

```JavaScript
// vite.config.js
import vue from '@vitejs/plugin-vue';
import vueComponents from 'unplugin-vue-components/vite';
import { VueIconResolver } from 'unplugin-vue-components/resolvers';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueComponents({
      resolvers: [
        VueIconResolver({
          importStyle: 'scoped',
          customResolvers: [
            // 这里可以添加其他自定义解析器
          ],
        }),
      ],
    }),
  ],
});
```

这段配置告诉 Vite 如何解析 IconPark 图标库中的组件，使得你可以在项目中按需导入图标。
#### 4.使用图标

在组件中，你可以直接使用IconPark的图标，而无需手动导入。

```vue
<template>
  <div>
    <IconParkIconName />
  </div>
</template>

<script setup>
</script>
```


应该替换为你想要使用的IconPark图标的组件名。

#### 6. 自定义图标样式

IconPark图标库允许你通过属性来自定义图标的样式：

```html
<icon-folder-open theme="outline" size="24" fill="#f5a623" strokeLinejoin="bevel"></icon-folder-open>
```

#### 7. 注意事项

- 确保在模板中使用图标时，名称是小写且用连字符分隔的。
- 如果图标名称包含连字符，导入时应使用驼峰命名法。
- 全局注册后，使用图标时不需要前缀；否则，使用自定义前缀或默认的`icon`前缀。

#### 8. 维护与更新

- 定期检查`@icon-park/vue-next`包的更新，以获得新图标和性能改进。
- 如果有新版本的Babel或相关插件发布，也应考虑更新以保持构建性能和语法支持的最新状态。

这份笔记涵盖了Vue 3项目中使用IconPark图标库的完整流程，从安装到配置再到实际使用，适用于希望在项目中集成IconPark图标库的开发者。

#### 9 . 卸载
`npm uninstall @icon-park/vue-next`