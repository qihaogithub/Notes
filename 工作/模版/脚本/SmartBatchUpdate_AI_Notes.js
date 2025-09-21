module.exports = {
  run: async function (tp) {
    // --- 配置区 ---
    const AI_MODEL = "deepseek-ai/DeepSeek-V3.1"; // 您想使用的 AI 模型
    const OPENAI_API_KEY = "ms-b92ab3ed-c924-4579-a624-7acf67ac01ac"; // ‼️ 在这里填入您的 OpenAI API Key
    const openAI_URL =
      "https://api-inference.modelscope.cn/v1/chat/completions";

    const LOOKBACK_HOURS = 24; // 巡查范围：最近 24 小时内修改过的文件
    // ?---------------

    new Notice(
      `🚀 开始巡查最近 ${LOOKBACK_HOURS} 小时内需要更新的项目...`,
      15000
    );

    // 1. 查找触发更新的文件：来自"资料"和"项目"文件夹
    const lookbackDate = new Date(Date.now() - LOOKBACK_HOURS * 60 * 60 * 1000);

    // a. 查找最近修改过的源文档 (资料/)
    const recentSourceFiles = app.vault.getMarkdownFiles().filter((f) => {
      const fm = app.metadataCache.getFileCache(f)?.frontmatter;
      return (
        f.path.startsWith("资料/") &&
        f.stat.mtime > lookbackDate.getTime() &&
        (fm?.projects || fm?.Parent_project)
      );
    });

    // b. 查找最近修改过的项目主笔记 (项目/)
    const recentProjectFiles = app.vault.getMarkdownFiles().filter(
      (f) =>
        f.path.startsWith("项目/") &&
        !f.name.endsWith("_AI.md") && // 排除 AI 笔记本身
        !f.name.includes("索引") && // 排除项目总览文件
        f.stat.mtime > lookbackDate.getTime()
    );

    if (recentSourceFiles.length === 0 && recentProjectFiles.length === 0) {
      new Notice("✅ 最近没有文档或项目笔记更新，无需操作。", 5000);
      return;
    }

    // 2. 收集所有需要更新的、不重复的项目笔记链接
    const projectsToUpdate = new Set();
    // a. 从源文档中收集
    recentSourceFiles.forEach((file) => {
      const fm = app.metadataCache.getFileCache(file)?.frontmatter;
      const projects = fm?.projects || fm?.Parent_project;
      if (Array.isArray(projects)) {
        projects.forEach((p) => {
          if (p && typeof p === "string") {
            const sourcePath = file.path;
            const linkedFile = app.metadataCache.getFirstLinkpathDest(
              p,
              sourcePath
            );
            if (linkedFile) {
              projectsToUpdate.add(linkedFile.path);
            }
          } else if (p && p.path) {
            projectsToUpdate.add(p.path);
          }
        });
      }
    });
    // b. 从项目主笔记中收集 (笔记本身就是项目)
    recentProjectFiles.forEach((file) => {
      projectsToUpdate.add(file.path);
    });

    if (projectsToUpdate.size === 0) {
      new Notice("✅ 源文档有更新，但未关联任何项目。", 5000);
      return;
    }

    // 新增：过滤掉已经处理过的项目
    const filteredProjectsToUpdate = [];
    for (const projectPath of projectsToUpdate) {
      const projectFile = app.vault.getAbstractFileByPath(projectPath);
      if (!projectFile || !projectFile.basename) continue;

      const aiNotePath = projectPath.replace(".md", "_AI.md");
      const aiNoteFile = app.vault.getAbstractFileByPath(aiNotePath);

      // 如果没有AI笔记，肯定需要处理
      if (!aiNoteFile) {
        filteredProjectsToUpdate.push(projectPath);
        continue;
      }

      // 检查AI笔记的最后处理时间
      const aiNoteCache = app.metadataCache.getFileCache(aiNoteFile);
      const lastProcessed = aiNoteCache?.frontmatter?.last_processed;

      // 如果没有last_processed字段或者源文件比最后处理时间更新，则需要处理
      const sourceFilesNeedUpdate = recentSourceFiles.some((sourceFile) => {
        const fm = app.metadataCache.getFileCache(sourceFile)?.frontmatter;
        const linkedProjects = fm?.projects || fm?.Parent_project;
        if (!Array.isArray(linkedProjects)) return false;
        
        const isLinkedToProject = linkedProjects.some((p) => {
          const linkedPath = typeof p === "string" ? p : p?.path || "";
          const linkedFile = app.metadataCache.getFirstLinkpathDest(
            linkedPath,
            sourceFile.path
          );
          return linkedFile && linkedFile.path === projectPath;
        });
        
        // 只有当源文件链接到当前项目且修改时间晚于最后处理时间时，才需要更新
        return isLinkedToProject && 
               sourceFile.stat.mtime > (lastProcessed ? new Date(lastProcessed).getTime() : 0);
      });

      const projectFileNeedUpdate = recentProjectFiles.some(
        (projFile) =>
          projFile.path === projectPath &&
          projFile.stat.mtime >
            (lastProcessed ? new Date(lastProcessed).getTime() : 0)
      );

      if (!lastProcessed || sourceFilesNeedUpdate || projectFileNeedUpdate) {
        filteredProjectsToUpdate.push(projectPath);
      }
    }

    if (filteredProjectsToUpdate.length === 0) {
      new Notice("✅ 所有项目都已是最新状态，无需更新。", 5000);
      return;
    }

    new Notice(
      `🔍 发现 ${filteredProjectsToUpdate.length} 个项目需要更新，开始处理...`,
      10000
    );

    let updatedCount = 0;
    const executionLogs = [];
    // 3. 为每一个需要更新的项目执行智能重写
    for (const projectPath of filteredProjectsToUpdate) {
      const projectFile = app.vault.getAbstractFileByPath(projectPath);
      if (!projectFile || !projectFile.basename) continue;

      const projectName = projectFile.basename;
      new Notice(`🔄 正在处理项目: ${projectName}...`);

      // 3 a. 查找该项目的所有关联源文档 (不止是近期的)
      // 注意：Dataview 查询需要通过 app.plugins.plugins.dataview.api.query 来执行
      const dv = app.plugins.plugins.dataview.api;
      const allSourceFilesQuery = `LIST FROM "资料" WHERE contains(projects, [[${projectName}]]) OR contains(Parent_project, [[${projectName}]])`;
      const queryResult = await dv.query(allSourceFilesQuery);

      let sourceDocsContent = "";
      let sourceFilePaths = [];
      if (queryResult.successful) {
        sourceFilePaths = queryResult.value.values.map((v) => v.path);
        for (const path of sourceFilePaths) {
          const file = app.vault.getAbstractFileByPath(path);
          if (file) {
            const content = await app.vault.cachedRead(file);
            sourceDocsContent += `

---

### 源文档: [[${path.split("/").pop()}]]

${content}`;
          }
        }
      }

      // 新增：将项目主笔记本身的内容也作为信息源
      const projectContent = await app.vault.cachedRead(projectFile);
      if (projectContent) {
        sourceDocsContent += `

---

### 源文档: [[${projectFile.name}]]

${projectContent}`;
      }

      // 3 b. 读取旧的 AI 笔记内容
      const aiNotePath = projectPath.replace(".md", "_AI.md");
      const aiNoteFile = app.vault.getAbstractFileByPath(aiNotePath);
      let oldAINoteContent = aiNoteFile
        ? await app.vault.read(aiNoteFile)
        : "这是第一次生成 AI 笔记。";

      // 记录本次执行的上下文用于调试
      const logEntry = {
        project: projectName,
        output: aiNotePath,
        inputs: [
          projectPath, // 项目主笔记
          ...sourceFilePaths, // 关联的源文档
        ],
      };
      if (aiNoteFile) {
        logEntry.inputs.push(aiNotePath); // 旧的AI笔记也作为输入
      }
      executionLogs.push(logEntry);

      // 3 c. 构建 Prompt
      const system_prompt = `
# AI 角色与任务

你是一个顶级的产品经理和用户体验专家。你的任务是基于一份"旧的项目笔记"和"一组项目的所有相关源文档"，生成一份全新的、内容更完整、信息无冗余的项目笔记。

你需要理解所有输入，并对信息进行"合并"、"更新"、"提炼"或"新增"，然后输出一个完整的、可直接用于覆写旧笔记的新版本。

# 内容筛选原则

**重要：智能识别与当前项目相关的内容**

在处理提供的源文档时，你必须进行智能内容筛选，而不是简单地将所有信息都包含进来：

1.  **项目相关性判断**：仔细分析每个源文档，识别出真正与当前项目"${projectName}"相关的内容。不是所有被标记为关联的文档都包含与本项目直接相关的信息。

2.  **内容类型识别**：
    - **项目专属文档**（如项目计划、需求文档、设计稿等）：通常大部分内容都与当前项目相关
    - **共享文档**（如会议记录、周报、产品文档等）：可能包含多个项目的信息，需要仔细筛选
    - **跨项目文档**：只提取其中明确提及当前项目的部分

3.  **筛选标准**：
    - 直接提及项目名称"${projectName}"的内容
    - 涉及项目相关人员、功能、需求、进度、问题等的内容
    - 对项目有决策性影响或参考价值的内容
    - 项目背景、目标、范围相关的内容

4.  **排除标准**：
    - 完全属于其他项目的内容
    - 与当前项目无关的通用信息
    - 重复或冗余的信息（保留最新或最完整的版本）

# 输出规则与指令

1.  **全局视角**：将筛选后的"来源文档"视为一个整体信息池，进行综合分析和提炼，避免简单罗列。
2.  **智能合并**：识别不同文档中关于同一主题的信息（如某个功能的多次讨论），并将其整合到一处。
3.  **保留有效信息**：旧笔记中的信息，如果在新的源文档中没有被更新或推翻，应予以保留。**绝不能无故删除旧笔记中的任何有效信息！**
4.  **结构清晰**：输出的笔记应结构化，参考以下标准结构：
    - # 项目标题
    - ## 📅 背景与目标
    - ## 👥 相关人员
    - ## 🔄 关键过程
    - ## ⚠️ 风险摘要
    - ## 📌 待办汇总
    - ## 🏁 结果与复盘
    - ## 🔗 相关文档
5.  **输出全文**：你的最终输出必须是**完整的、全新的 AI 笔记全文**，严格遵循上述结构。
6.  **信息溯源与链接使用**：在生成每一条关键信息、结论或数据时，必须使用Obsidian的链接格式引用其直接来源的文档。根据不同场景灵活使用以下链接方式：
   - **基本双链**：([[源文档名.md]]) - 最常用的链接方式，用于一般性引用
   - **标题锚点链接**：([[源文档名.md#具体标题]]) - 当需要引用文档中特定章节时使用，可以精确定位到某个标题下的内容
   - **别名链接**：([[源文档名.md|显示文本]]) - 当需要在链接中显示更友好的文本描述时使用，例如：([[会议记录.md|产品评审会议]])
   - **嵌入链接**：!([[源文档名.md]]) - 当需要直接在笔记中显示被引用文档的完整内容时使用，类似于图片嵌入效果
   - **Markdown链接**：[链接文字](源文档名.md) - 当需要自定义链接文本且不使用Obsidian双链格式时使用

   如果一条信息是综合自多个文档，请引用所有相关文档，例如：([[文档A.md]], [[文档B.md#关键结论]])。如果信息来自旧的AI笔记并且在新文档中没有提及，则无需引用。这是强制要求，目的是确保所有信息的来源都清晰可追溯。

   **链接使用原则**：
   - 优先使用双链格式 ([[ ]])，这是Obsidian的核心特性
   - 对于具体的数据、结论或特定章节，优先使用标题锚点链接 ([[#标题]])
   - 当链接文本过长或不够直观时，使用别名链接 ([[|别名]])
   - 只有在需要完整显示被引用文档内容时，才使用嵌入链接 (![[ ]])
   - 在相关文档列表中，统一使用基本双链格式
`;
      const user_prompt = `
    请根据以下信息，为项目 "${projectName}" 生成全新的项目笔记。
    ## 1. 旧的项目笔记内容：
    \


markdown
${oldAINoteContent}


    ## 2. 所有相关的源文档内容集合：
    \


markdown
${sourceDocsContent}


    `;

      // 3 d. 调用 API
      const response = await fetch(openAI_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${OPENAI_API_KEY}`,
        },
        body: JSON.stringify({
          model: AI_MODEL,
          messages: [
            { role: "system", content: system_prompt },
            { role: "user", content: user_prompt },
          ],
          temperature: 0.5,
        }),
      });

      if (response.ok) {
        const data = await response.json();
        let newAINoteContent = data.choices[0].message.content;

        // 3 e. 写入/覆写 AI 笔记, 并确保包含正确的 YAML frontmatter
        const projectCache = app.metadataCache.getFileCache(projectFile);
        const projectFrontmatter = projectCache?.frontmatter;

        const today = new Date().toISOString(); // YYYY-MM-DDTHH:mm:ss.sssZ

        let createdDate = today;
        if (aiNoteFile) {
          const aiNoteCache = app.metadataCache.getFileCache(aiNoteFile);
          if (aiNoteCache?.frontmatter?.created) {
            createdDate = aiNoteCache.frontmatter.created;
          }
        }

        const projectType =
          projectFrontmatter?.Projects || projectFrontmatter?.Projects || "";
        const parentProjectRaw =
          projectFrontmatter?.Parent_project ||
          projectFrontmatter?.parent_project;
        let parentProject = "";
        if (parentProjectRaw) {
          const parentProjectString = parentProjectRaw.toString();
          if (
            parentProjectString.startsWith("[[") &&
            parentProjectString.endsWith("]]") &&
            !parentProjectString.includes('"')
          ) {
            parentProject = `"${parentProjectString}"`;
          } else {
            parentProject = parentProjectString;
          }
        }
        const stakeholders =
          projectFrontmatter?.Stakeholders || projectFrontmatter?.stakeholders;
        let stakeholdersYaml = "";
        if (Array.isArray(stakeholders) && stakeholders.length > 0) {
          stakeholdersYaml = stakeholders.map((s) => `  - ${s}`).join("\n");
        }
        const status = projectFrontmatter?.status || "";
        const tags = projectFrontmatter?.tags || [];
        let tagsYaml = "  - AI笔记";
        if (Array.isArray(tags) && tags.length > 0) {
          // 确保不重复添加 AI笔记 标签
          const filteredTags = tags.filter((t) => t !== "AI笔记");
          if (filteredTags.length > 0) {
            tagsYaml =
              "  - AI笔记\n" + filteredTags.map((t) => `  - ${t}`).join("\n");
          }
        }

        // 新增：添加最后处理时间
        const newFrontmatter = `---
created: ${createdDate}
updated: ${today}
last_processed: ${today}
status: ${status}
Projects: ${projectType}
Parent_project: ${parentProject}
Stakeholders:${
          stakeholdersYaml
            ? `
${stakeholdersYaml}`
            : " []"
        }
tags:
${tagsYaml}
---

`;

        // 如果 AI 的响应包含了 frontmatter，则将其移除，使用我们自己生成的
        if (newAINoteContent.startsWith("---")) {
          const yamlEndIndex = newAINoteContent.indexOf("\n---", 4);
          if (yamlEndIndex !== -1) {
            newAINoteContent = newAINoteContent.substring(yamlEndIndex + 5);
          }
        }

        const finalContent = newFrontmatter + newAINoteContent;

        if (aiNoteFile) {
          await app.vault.modify(aiNoteFile, finalContent);
        } else {
          await app.vault.create(aiNotePath, finalContent);
        }
        updatedCount++;
      } else {
        new Notice(`❌ 项目 "${projectName}" 更新失败。`, 5000);
      }
    }

    new Notice(
      `✅ 全部完成！成功更新了 ${updatedCount} / ${filteredProjectsToUpdate.length} 个项目。`,
      8000
    );

    console.log("--- AI 笔记更新任务日志 ---");
    console.log(`时间: ${new Date().toLocaleString()}`);
    console.log(
      `总共发现 ${filteredProjectsToUpdate.length} 个项目需要更新，成功处理 ${updatedCount} 个。`
    );
    if (executionLogs.length > 0) {
      console.log("详细执行记录:");
      console.log(JSON.stringify(executionLogs, null, 2));
    } else {
      console.log("没有项目被实际处理。");
    }
  },
};
