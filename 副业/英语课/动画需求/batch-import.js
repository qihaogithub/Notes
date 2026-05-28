/**
 * 批量导入 Markdown 文件到飞书云空间
 * 使用 lark-cli drive +import 命令
 * 支持 Windows / macOS / Linux
 */

const { execSync } = require('child_process');
const path = require('path');

// 配置区 ==========================================
// 目标 wiki 节点 token
const WIKI_TOKEN = 'Pkk5wr7YjiPBtekf2b2cIhj3neb';

// 待导入的文件列表（相对于脚本所在目录）
const FILES = [
  '描红题.md',
  '情景对话.md',
  '闪卡题.md',
  '通用答题反馈.md',
  '通用loading.md',
  '涂色题答题页.md'
];
// =================================================

// 获取脚本所在目录
const SCRIPT_DIR = __dirname;

function runCommand(cmd) {
  try {
    const output = execSync(cmd, {
      cwd: SCRIPT_DIR,
      encoding: 'utf8',
      stdio: ['pipe', 'pipe', 'pipe']
    });
    return output;
  } catch (error) {
    return error.stdout || error.stderr || error.message;
  }
}

function extractJson(output) {
  const match = output.match(/\{[\s\S]*\}/);
  return match ? match[0] : null;
}

function importFile(filePath, fileName) {
  console.log(`\n[${fileName}] 开始导入...`);

  // 构建完整的文件路径
  const fullPath = path.join(SCRIPT_DIR, filePath);

  // 执行导入命令
  // drive +import 没有 --wiki-token 参数，需要先导入到根目录
  const cmd = `lark-cli drive +import --file "${fullPath}" --type docx --name "${fileName}"`;
  console.log(`执行命令: ${cmd}`);
  
  const output = runCommand(cmd);
  console.log(output);

  const jsonStr = extractJson(output);
  if (!jsonStr) {
    console.log(`[${fileName}] ❌ 导入失败：无法解析返回结果`);
    return null;
  }

  try {
    const result = JSON.parse(jsonStr);
    if (result.ok && result.data?.token) {
      console.log(`[${fileName}] ✅ 导入成功，token: ${result.data.token}`);
      return result.data.token;
    } else {
      console.log(`[${fileName}] ❌ 导入失败: ${result.error?.message || '未知错误'}`);
      return null;
    }
  } catch (e) {
    console.log(`[${fileName}] ❌ JSON 解析失败`);
    return null;
  }
}

function moveToWiki(docxToken, fileName) {
  console.log(`[${fileName}] 移动到 Wiki...`);

  const cmd = `lark-cli wiki +move --obj-type docx --obj-token ${docxToken} --target-parent-token ${WIKI_TOKEN}`;
  console.log(`执行命令: ${cmd}`);

  const output = runCommand(cmd);
  console.log(output);

  const jsonStr = extractJson(output);
  if (!jsonStr) {
    console.log(`[${fileName}] ❌ 移动失败：无法解析返回结果`);
    return null;
  }

  try {
    const result = JSON.parse(jsonStr);
    if (result.ok && result.data?.wiki_token) {
      const wikiUrl = `https://my.feishu.cn/wiki/${result.data.wiki_token}`;
      console.log(`[${fileName}] ✅ 移动成功: ${wikiUrl}`);
      return wikiUrl;
    } else {
      console.log(`[${fileName}] ❌ 移动失败: ${result.error?.message || '未知错误'}`);
      return null;
    }
  } catch (e) {
    console.log(`[${fileName}] ❌ JSON 解析失败`);
    return null;
  }
}

async function main() {
  console.log('========================================');
  console.log('批量导入 Markdown 到飞书 Wiki');
  console.log(`目标节点: ${WIKI_TOKEN}`);
  console.log(`文件数量: ${FILES.length}`);
  console.log('========================================');

  const results = [];

  for (const fileName of FILES) {
    // Step 1: 导入文件
    const docxToken = importFile(fileName, path.parse(fileName).name);

    if (!docxToken) {
      results.push({ fileName, status: 'import_failed' });
      continue;
    }

    // 添加小延迟，避免 API 限流
    await new Promise(resolve => setTimeout(resolve, 1000));

    // Step 2: 移动到 Wiki
    const wikiUrl = moveToWiki(docxToken, path.parse(fileName).name);

    if (wikiUrl) {
      results.push({ fileName, status: 'success', wikiUrl });
    } else {
      results.push({ fileName, status: 'move_failed', docxToken });
    }

    // 添加小延迟，避免 API 限流
    await new Promise(resolve => setTimeout(resolve, 1000));
  }

  // 输出汇总
  console.log('\n========================================');
  console.log('导入完成汇总');
  console.log('========================================');

  const successCount = results.filter(r => r.status === 'success').length;
  const failCount = results.length - successCount;

  results.forEach(r => {
    if (r.status === 'success') {
      console.log(`✅ ${r.fileName}: ${r.wikiUrl}`);
    } else {
      console.log(`❌ ${r.fileName}: ${r.status}`);
    }
  });

  console.log(`\n总计: ${results.length} 个文件，成功 ${successCount} 个，失败 ${failCount} 个`);
}

main().catch(console.error);
