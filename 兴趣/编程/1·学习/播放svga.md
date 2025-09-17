在 HTML 中播放 SVGA 资源，可以通过以下步骤实现：

1. **安装 SVGAPlayerWeb**：可以通过 npm 进行安装，使用命令 `npm install svgaplayerweb --save` 。

2. **引入 SVGAPlayerWeb 库**：在 HTML 文件中通过 `<script>` 标签引入 SVGAPlayerWeb 的预编译 JS 文件，或者在项目中通过 require 或 import 的方式引入对应的模块。

    ```html
    <!-- 使用预编译的JS文件 -->
    <script src="https://cdn.jsdelivr.net/npm/svgaplayerweb@2.3.1/build/svga.min.js"></script>
    <!-- 或者在模块化的项目中 -->
    const SVGA = require('svgaplayerweb');
    ```

3. **在 HTML 中添加容器**：创建一个 `<div>` 元素作为 SVGA 动画的容器，并为其设置相应的样式和属性。

    ```html
    <div id="demoCanvas" style="width: 375px; height: 375px;"></div>
    ```

4. **编写 JavaScript 代码**：使用 SVGA. Player 和 SVGA. Parser 类来加载和播放 SVGA 动画。

    ```javascript
    var player = new SVGA.Player('#demoCanvas');
    var parser = new SVGA.Parser('#demoCanvas');
    parser.load('your_svga_file.svga', function(videoItem) {
        player.setVideoItem(videoItem);
        player.startAnimation();
    });
    ```

5. **自动加载动画**：如果希望动画在页面加载完成后自动播放，可以为 `<div>` 元素添加 `src` 属性，指向 SVGA文件。

    ```html
    <div src="your_svga_file.svga" id="demoCanvas" style="width: 375px; height: 375px;"></div>
    ```

6. **动态图像和文本**：SVGA. Player 还支持动态替换动画中的图像和添加文本。

    ```javascript
    player.setImage('http://yourserver.com/xxx.png', 'ImageKey');
    player.setText('Your Text', 'TextKey');
    ```

7. **音频支持**：如果 SVGA 动画包含音频，需要在 HTML 中引入 `howler.js` 库来支持音频播放。

    ```html
    <script src="https://cdn.jsdelivr.net/npm/howler@2.0.15/dist/howler.core.min.js"></script>
    ```

8. **SVGA-Format 1. X 支持**：如果需要支持 SVGA-Format 1. X，需要在 HTML 页面中添加 JSZip 库。

    ```html
    <script src="//s1.yy.com/ued_web_static/lib/jszip/3.1.4/jszip.min.js" charset="utf-8"></script>
    ```

9. **注意事项**：确保 SVGA 资源的 CORS 设置正确，以避免跨域问题。对于 IE 6-9，需要使用特定的格式和方法加载 SVGA 动画。

通过上述步骤，你可以在 HTML 页面中播放 SVGA 动画资源。这些步骤基于搜索结果中的多篇文章，提供了一个全面的指南来实现 SVGA 动画的播放。