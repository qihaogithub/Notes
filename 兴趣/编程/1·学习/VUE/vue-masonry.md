
[官方文档](https://github.com/shershen08/vue-masonry#readme)

[《Vue插件》瀑布流插件vue-masonry的使用与踩坑记录](https://blog.csdn.net/zy21131437/article/details/127683745)

## 安装
```bash
npm install vue-masonry --save
```

## Main .js 里

```bash
import { VueMasonryPlugin } from "vue-masonry";
Vue.use(VueMasonryPlugin);
```


## Vue 组件中
首先引入
```bash
import Masonry from "masonry-layout";
```

Vue-masonry 的使用核心在于自定义指令：v-masonry 和 v-masonry-tile，这个是整个瀑布流插件的使用核心，
<div v-masonry>
    <div v-masonry-tile v-for="(item, index) in blocks">
       <!-- block item markup -->
    </div>
</div>
<div v-masonry>
    <div v-masonry-tile v-for="(item, index) in blocks">
       <!-- block item markup -->
    </div>
</div>
<div v-masonry>
    <div v-masonry-tile v-for="(item, index) in blocks">
       <!-- block item markup -->
    </div>
</div>
<div v-masonry>
    <div v-masonry-tile v-for="(item, index) in blocks">
       <!-- block item markup -->
    </div>
</div>
<div v-masonry>
    <div v-masonry-tile v-for="(item, index) in blocks">
       <!-- block item markup -->
    </div>
</div>
<div v-masonry>
    <div v-masonry-tile v-for="(item, index) in blocks">
       <!-- block item markup -->
    </div>
</div>
<div v-masonry>
    <div v-masonry-tile v-for="(item, index) in blocks">
       <!-- block item markup -->
    </div>
</div>
<div v-masonry>
    <div v-masonry-tile v-for="(item, index) in blocks">
       <!-- block item markup -->
    </div>
</div>
<div v-masonry>
    <div v-masonry-tile v-for="(item, index) in blocks">
       <!-- block item markup -->
    </div>
</div>

V-masonry: 绑定在父级容器上；
V-masonry-tile: 绑定在子级容器上；
```bash
<div class="discover" v-masonry>
       <div
         v-for="(v, ix) in discoverImg"
         :key="ix"
         class="discoveImg"
         v-masonry-tile
       >
         <img :src="v.img" alt="" />
       </div>
```

Css 部分

```bash
.discover {
    height: 100% !important;
  }
  .discoveImg {
    float: left;
    padding: 10px;

    margin-right: 20px;
    margin-bottom: 20px;
    border-radius: 15px;
    img {
      width: 200px;
    }
  }
```



## 属性

[当前可用的属性重现了原始砌体插件](http://masonry.desandro.com/options.html)中的大部分属性：

- `item-selector=".item"` - 列表元素 DOM 项目选择器；
- `transition-duration="0.3s` - 过渡的持续时间；
- `column-width="#test"` - 列宽的元素选择器。可以是选择器字符串或数字；
- `origin-left="false"` - 默认设置为将元素分组到右侧，而不是左侧；
- `origin-top="false"` - 默认将元素分组到底部而不是顶部；
- `stamp=".stamp"` - 指定布局中标记哪些元素；
- `gutter=".gutter-block-selector"` - 指定 [项目元素之间的水平空间]。可以是选择器字符串或数字。（[https://masonry.desandro.com/options.html#gutter](https://masonry.desandro.com/options.html#gutter)）。将 gutter 设置为元素或选择器字符串以使用元素的外部宽度；
- `fit-width="true"` - 设置容器的宽度以适合可用的列数；
- `horizontal-order="true"` - 布局项目以（大部分）保持水平从左到右的顺序；
- `stagger="0.03s"` - 交错项目转换，因此项目会一个接一个地逐步转换。设置为 CSS 时间格式“0.03 s”，或设置为毫秒数 30。
- `destroy-delay="0"` - 容器被销毁时卸载砌体前等待的时间（以毫秒为单位）`masonry.destroy()`。这在页面/路由转换期间很有用，可确保转换过程中布局一致。

如果您需要手动触发砌体布局重绘（例如，如果您的图块元素数量或内容已更改），您现在可以使用 `this.$redrawVueMasonry('containerId')` 方法。从 [0.11.8](https://github.com/shershen08/vue-masonry/pull/89) 开始，您可以传递要触发重绘的块的 ID。