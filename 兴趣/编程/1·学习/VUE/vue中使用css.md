在Vue.js中，你可以通过几种不同的方法将CSS样式应用到你的组件中：

1. **内联样式**：直接在组件的模板中使用`style`属性来添加CSS样式。

    ```vue
    <template>
      <div style="color: red;">This text will be red.</div>
    </template>
    ```

2. **Scoped CSS**：在单文件组件（`.vue`文件）中，你可以在`<style>`标签中添加CSS，并使用`scoped`属性来确保样式只应用于当前组件。

    ```vue
    <style scoped>
    .red-text {
      color: red;
    }
    </style>

    <template>
      <div class="red-text">This text will be red and scoped to this component.</div>
    </template>
    ```

3. **模块化CSS**：使用CSS预处理器（如Sass或Less）时，你可以在`<style>`标签中通过相应的语言标识来编写模块化的CSS。

    ```vue
    <style lang="scss" scoped>
    $color: red;
    .red-text {
      color: $color;
    }
    </style>
    ```

4. **CSS文件引入**：你可以在组件的`<style>`标签中引入外部CSS文件。

    ```vue
    <style>
    @import './path/to/your-styles.css';
    </style>
    ```

5. **CSS预处理器**：在构建过程中，你可以使用如Webpack等构建工具来处理CSS预处理器，并将它们与Vue组件一起打包。

6. **Vue CLI**：如果你使用的是Vue CLI创建的项目，它会为你配置好Webpack和相应的CSS加载器，使得上述方法都很容易实现。

确保在实际项目中，你选择的方法符合项目的需求和团队的编码规范。使用Scoped CSS可以避免样式冲突，而引入外部CSS文件或使用CSS预处理器可以提高样式的复用性和模块化。