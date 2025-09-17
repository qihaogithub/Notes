要使用Pinia管理上传的图片，你需要首先确保你已经在你的Vue项目中安装并设置了Pinia。Pinia是一个Vue的状态管理库，它允许你以一种更结构化和可扩展的方式来管理状态。

以下是如何使用Pinia来管理上传的图片的步骤：

1. **创建一个Pinia store**：首先，你需要创建一个Pinia store来存储上传的图片状态。

```javascript
// store.js
import { defineStore } from 'pinia';

export const useUploadStore = defineStore('upload', {
  state: () => ({
    image: null,
  }),
  actions: {
    setImage(file) {
      this.image = file;
    },
  },
});
```

2. **在组件中使用store**：在你的上传按钮组件中，使用`useUploadStore`来管理图片状态。

```javascript
<script>
import { useUploadStore } from './store'; // 确保路径正确

export default {
  props: {
    ResourcesName: {
      type: String,
      default: "资源名称",
    },
    ResourcesLink: {
      type: String,
      default: "",
    },
    id: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    const uploadStore = useUploadStore();

    function uploadButton() {
      this.$refs.fileInput.click();
    }

    function handleFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        uploadStore.setImage(file); // 将图片存储到Pinia store中
        this.$emit("upload", { id: props.id, file: file }); // 触发上传事件
      }
    }

    return {
      uploadButton,
      handleFileChange,
    };
  },
};
</script>
```

3. **在需要的地方访问图片**：在任何需要访问上传图片的地方，你可以通过`useUploadStore`来获取图片状态。

```javascript
// 其他组件中
import { useUploadStore } from '@/store';

const uploadStore = useUploadStore();
const uploadedImage = uploadStore.image;
```

4. **样式调整**：如果你需要对上传按钮的样式进行调整，可以在`<style>`标签中继续添加CSS规则。

确保你已经按照Pinia的文档正确地在你的Vue应用中设置了Pinia，并且在你的组件中正确地导入了`useUploadStore`。

通过这种方式，你可以将上传的图片状态集中管理在Pinia store中，这有助于你的应用更好地维护状态，并且使得状态在不同组件之间的共享变得更加容易。