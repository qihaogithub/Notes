## 简介
`~/.zshrc` 文件是 Z shell（zsh）的启动文件之一，用于个性化配置用户的 zsh 环境。Zsh 是一种为交互式使用而设计的 shell，也是 Bash 的一个替代品，它提供了许多改进的命令行功能，如更强大的命令行编辑、更完整的提示符定制、更好的历史记录功能等。
以下是 `~/.zshrc` 文件的一些主要特点和用途：
1. **个性化设置**：用户可以在 `~/.zshrc` 文件中设置别名（aliases）、函数（functions）、环境变量（environment variables）等，以定制自己的命令行工作环境。
2. **启动脚本**：每次当一个新的 zsh 实例启动时（例如打开一个新的终端窗口或标签页），`~/.zshrc` 文件都会被读取，并执行其中的命令。
3. **配置选项**：可以在这里设置 zsh 的各种选项，比如开启或关闭特定的功能，例如自动补全、拼写校正等。
4. **插件管理**：如果使用 zsh 的插件系统，通常会在 `~/.zshrc` 文件中包含用于加载插件的行。
5. **主题定制**：对于使用 Oh My Zsh 等框架的用户，`~/.zshrc` 文件中可以设置主题，改变命令行的外观和感觉。
下面是一个简单的 `~/.zshrc` 文件示例：
```zsh
# 设置提示符
PROMPT='%n at %m in %~$(git_info) $ '
# 别名
alias ls='ls -G'  # macOS 系统上的彩色 ls
alias ll='ls -l'  # 显示详细列表
# 函数
function git_info() {
  if git rev-parse --is-inside-work-tree &> /dev/null; then
    echo "%{\e[0;32m%}$(git branch --show-current)%{\e[0m%}"
  fi
}
# 每次命令后更新提示符
RPROMPT='$(git_info)'
# 加载 Oh My Zsh 框架（如果安装了）
if [ -f ~/.oh-my-zsh/oh-my-zsh.sh ]; then
  source ~/.oh-my-zsh/oh-my-zsh.sh
fi
# 设置路径
PATH=$PATH:/usr/local/bin
# 启用插件
plugins=(git colored-man-pages)
# 其他设置...
```
要使更改生效，通常需要重新加载 `~/.zshrc` 文件，可以通过在终端中运行 `source ~/.zshrc` 命令来实现，或者简单地关闭并重新打开终端。


## Pip 国内镜像源配置
配置 pip 的国内镜像通常是在 `~/.zshrc` 文件中进行修改的。这是因为 `~/.zshrc` 文件是 Z shell (zsh) 的配置文件，任何你想在每次启动 zsh 时自动执行的命令或环境变量设置都可以放在这个文件中。
要配置 pip 使用国内镜像，你可以在 `~/.zshrc` 文件中添加以下内容：
```zsh
# 配置 pip 使用国内镜像源
export PIP_INDEX_URL=http://mirrors.aliyun.com/pypi/simple/
```
这里使用的是阿里云的 Python 包索引作为例子，你也可以选择其他国内的 pip 镜像源，如清华大学、豆瓣等。
在添加完上述配置后，你需要让这些更改生效。根据前面的对话内容，你有以下几种方法：
1. **重新加载配置文件**：
   ```zsh
   source ~/.zshrc
   ```
2. **关闭并重新打开终端**：
   关闭终端窗口或标签页，然后重新打开一个新的终端。
3. **使用 `exec zsh` 命令**：
   ```zsh
   exec zsh
   ```
4. **对于每个新会话自动加载**：
   保存更改后，关闭并重新打开终端，新的配置将在每个新会话中自动加载。
完成以上步骤后，pip 就会使用你设置的国内镜像源来下载 Python 包了。


## 修改


在终端执行 `open -e ~/.zshrc` 可以打开 ~/.zshrc 文件


```
alias python=/usr/bin/python3
export PATH="/usr/local/bin:$PATH"
export PATH="/usr/local/Homebrew/bin:$PATH"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/opt/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/opt/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/opt/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<


```
