[原文地址](https://www.cnblogs.com/nanke-dream/p/16451155.html)

vscode扩展商店Path Intellisense为我们提供了使用./的方式拥有路径提示

[![](https://img2022.cnblogs.com/blog/2023663/202207/2023663-20220706155112325-1178860210.png)
](https://img2022.cnblogs.com/blog/2023663/202207/2023663-20220706155112325-1178860210.png)

而vue项目使用@符号时候就需要在配置一次

打开设置 \- 首选项 \- 搜索 Path Intellisense - 打开 settings.json ，添加

"path-intellisense.mappings": { "@": "${workspaceRoot}/src" }

我们都知道@代表src下的文件

在vue项目 package.json 所在同级目录下创建文件 jsconfig.json，添加以下内容：

[![](https://assets.cnblogs.com/images/copycode.gif)
](https://assets.cnblogs.com/images/copycode.gif)

{ "compilerOptions": { "target": "ES6", "module": "commonjs", "allowSyntheticDefaultImports": true, "baseUrl": "./", "paths": { "@/*": \["src/*"\]
       }
   }, "exclude": \[ "node_modules" \]
}

[![](https://assets.cnblogs.com/images/copycode.gif)
](https://assets.cnblogs.com/images/copycode.gif)

\_\_EOF\_\_

[![](https://s3.uuu.ovh/imgs/2023/09/26/95e9b8ca4d2975c4.jpg)
](https://s3.uuu.ovh/imgs/2023/09/26/95e9b8ca4d2975c4.jpg)

*   **本文作者：**  [南柯Dream丶](https://www.cnblogs.com/nanke-dream)
*   **本文链接：**  [https://www.cnblogs.com/nanke-dream/p/16451155.html](https://www.cnblogs.com/nanke-dream/p/16451155.html)
*   **关于博主：**  评论和私信会在第一时间回复。或者[直接私信](https://msg.cnblogs.com/msg/send/nanke-dream)我。
*   **版权声明：**  本博客所有文章除特别声明外，均采用 [BY-NC-SA](https://creativecommons.org/licenses/by-nc-nd/4.0/ "BY-NC-SA") 许可协议。转载请注明出处！
*   **声援博主：**  如果您觉得文章对您有帮助，可以点击文章右下角**【推荐】** 一下。