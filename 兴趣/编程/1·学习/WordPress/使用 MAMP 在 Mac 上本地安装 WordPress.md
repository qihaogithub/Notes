来源：[如何在 Mac 上本地安装 WordPress（2 种简单方法） - WordPress中文](https://wpeyes.com/wordpress/archives/6928)


## 1 安装并设置 MAMP 
MAMP 是一个流行的程序，可让您在 Mac 计算机上运行 WordPress。

首先，您需要访问 [MAMP 网站](https://www.mamp.info/en/)。在这里您应该看到最新版本的 MAMP 和 MAMP Pro。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/download-mamp-pro.png)

MAMP 为不同版本的 macOS 操作系统提供单独的下载。

不确定您的计算机上安装的是哪个版本的 macOS？要了解详情，只需单击计算机工具栏中的 Apple 图标即可。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/mac-apple-icon.png)

然后您可以单击“关于本机”。

这将打开一个弹出窗口，显示有关您的计算机的大量信息。这包括您的 macOS 版本。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/macos-mac-version.png)

您现在可以下载适合您的操作系统的正确版本的 MAMP。

下载完成后，双击 MAMP .pkg 文件。这将启动 MAMP 安装程序。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/mamp-installer-mac.png)

现在只需按照屏幕上的说明安装 MAMP。

安装此程序后，您可以通过打开计算机的“应用程序”文件夹来继续启动 MAMP。

在这里您将找到两个版本的 MAMP。MAMP Pro 是付费版本，因此请确保选择免费版本。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/mamp-free-pro.png)

在此 MAMP 文件夹中，您将找到各种文件以及 MAMP 应用程序。

双击启动 MAMP 应用程序。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/mamp-free-app.png)

在开始之前，我们建议您配置一些设置以使您的 MAMP 体验更好。

要进行这些更改，只需单击工具栏中的“MAMP”即可。然后您可以选择“首选项…”

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/mamp-preferences-settings.png)

在弹出窗口中，选择“端口”选项卡。

您现在可以检查 MAMP 正在使用哪个 Apache 端口。如果 MAMP 尚未使用此端口，我们建议切换到 Apache 端口 8888。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/mamp-apache-port.png)

下一步是设置文档根文件夹。您将在该文件夹中创建和存储所有本地 WordPress 网站。

默认情况下，MAMP 使用 /Applications/MAMP/htdocs/ 文件夹，但您可以将其更改为任何其他位置。

在“首选项…”对话框中，单击“服务器”选项卡。您现在应该看到您的文档根目录。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/mamp-document-root.png)

要将您的网站存储在任何其他文件夹中，请单击“选择…”按钮。

这将打开一个弹出窗口，您可以在其中选择一个新位置。您可能还想创建一个新文件夹来存储所有 WordPress 网站。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/mac-new-folder.png)

您可以将此文件夹命名为任何您想要的名称。

为了本文的目的，我们将把我们的网站存储在名为“allwebsites”的文件夹中。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/create-new-folder.png)

## 2、在 MAMP 上安装 WordPress**

现在您已经设置了 MAMP，让我们继续在您的 Mac 计算机上[安装 WordPress 。](https://www.wpbeginner.com/how-to-install-wordpress/)

首先，您需要访问 [WordPress.org](http://wordpress.org/download/) 网站并下载最新版本的 WordPress 核心。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/download-wordpress.png)

**注意：**  WordPress 有两个版本。[有关更多详细信息，请参阅WordPress.com 与 WordPress.org](https://www.wpbeginner.com/beginners-guide/self-hosted-wordpress-org-vs-free-wordpress-com-infograph/) 之间的比较。

从 WordPress. Org 下载文件后，只需解压缩即可。这将创建一个解压缩的“wordpress”文件夹。

现在只需将此文件夹复制到您的 MAMP 文档根文件夹中即可。

由于我们更改了文档根文件夹，因此我们需要将“wordpress”复制到 applications/MAMP/htdocs/allwebsites 中。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/wordpress-allwebsites-file.png)

WordPress 需要一个[数据库](https://www.wpbeginner.com/glossary/database/)来存储其所有内容和数据。您需要先创建此数据库，然后才能创建本地网站。

别担心，这并不像听起来那么难！

在 MAMP“首选项…”窗口中，只需单击“确定”按钮即可。这应该在新的浏览器选项卡中启动 MAMP 应用程序。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/welcome-to-mamp.png)

我们的下一个任务是启动 [phpMyAdmin](https://www.wpbeginner.com/beginners-guide/beginners-guide-to-wordpress-database-management-with-phpmyadmin/)。这是一个基于 Web 的应用程序，可用于管理网站的 MySQL 数据库。

在工具栏中，单击**工具 » phpMyAdmin**。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/tools-phpmyadmin-app.png)

这将在新选项卡中打开 phpMyAdmin。在 phpMyAdmin 仪表板中，单击数据库选项卡。

您现在可以在“数据库名称”字段中输入数据库的名称。您可以将数据库命名为任何您想要的名称。请务必记下该名称，因为我们将在下一步中使用它。

在本教程中，我们将数据库称为 test\_db。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/phpmyadmin-create-database.png)

输入数据库名称后，单击“创建”按钮。

PhpMyAdmin 现在将继续创建您的数据库。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/phpmyadmin-database-button.png)

现在是时候安装 WordPress 了。

在新的浏览器选项卡中，只需转到“如果您使用 8888 以外的任何端口，请不要忘记更改此 URL 以提及您的端口”。[ ](http://localhost:8888/) ` http://localhost:8888/`

您现在应该会看到复制到根文档文件夹中的“wordpress”文件夹的链接。

您现在可以继续并单击此链接。这将打开 WordPress 安装向导。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/wordpress-setup-wizard.png)

WordPress 安装向导首先要求您选择一种语言。继续做出选择，然后单击“继续”按钮。

在下一个屏幕上，WordPress 列出了完成安装所需的所有信息。

阅读此屏幕后，单击“让我们开始”按钮继续。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/wordpress-lets-go.png)

安装向导现在将询问您的 WordPress 数据库信息。对于数据库名称，只需键入您在上一步中创建的名称即可。

对于用户名和密码，输入“root”。然后，您可以在“数据库主机”字段中输入“localhost”。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/wordpress-database-information.png)

本地主机只是意味着数据库和网站托管在同一台服务器上。在这种情况下，服务器是您的 Mac 计算机。

输入所有这些信息后，只需单击“提交”按钮。

WordPress 现在将连接到您的数据库并为您创建一个配置文件。完成后，您将看到一条成功消息。

要继续下一步，请单击“运行安装”按钮。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/wordpress-run-installation.png)

在下一个屏幕上，WordPress 会要求您添加网站标题。大多数 WordPress 主题都会在网站的最顶部显示此标题。例如，您可以使用[您的公司名称](https://www.wpbeginner.com/tools/business-name-generator/)。

您还可以随时[更改 WordPress 仪表板中的标题。](https://www.wpbeginner.com/beginners-guide/how-to-change-the-just-another-wordpress-site-text/)

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/site-information.png)

您还需要创建用户名和密码。[这是您将用于访问 WordPress 仪表板的](https://www.wpbeginner.com/beginners-guide/how-to-find-your-wordpress-login-url/)登录信息。

您还可以在“您的电子邮件”字段中输入[您的电子邮件地址。](https://www.wpbeginner.com/beginners-guide/how-to-get-a-free-email-domain-quick-and-easy-methods/)这是 WordPress 发送所有管理电子邮件的地址。

完成此表格后，单击“安装 WordPress”按钮。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/install-wp.png)

WordPress 现在将运行安装。

几分钟后，您应该会看到“成功！” 信息。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/success.png)

要直接跳转到 WordPress 登录屏幕，请单击“登录”按钮。

您还可以使用以下 URL 登录本地 WordPress 网站： http://localhost:8888/wordpress/wp-login.php

**注意：** 如果您使用不同的 Apache 端口，则需要更改此 URL 的“8888”部分。

您现在可以通过输入您在上一步中创建的用户名和密码来登录您的 WordPress 网站。

这将带您进入 WordPress 仪表板。

![](https://www.wpbeginner.com/wp-content/uploads/2018/09/local-wordpress-dashboard.png)

## 在 Mac 上本地尝试 WordPress

本地安装非常适合在计算机上测试 WordPress 或开发网站。现在您已经在 Mac 上本地运行了 WordPress，以下是您可能想要尝试的一些操作。

*   尝试最好[的 WordPress 主题](https://www.wpbeginner.com/showcase/best-wordpress-themes/)。
*   尝试找到[适合您的完美 WordPress 主题](https://www.wpbeginner.com/wp-themes/selecting-the-perfect-theme-for-wordpress/)。
*   在本地测试[必要的 WordPress 插件](https://www.wpbeginner.com/showcase/24-must-have-wordpress-plugins-for-business-websites/)。
*   [通过创建您自己的插件](https://www.wpbeginner.com/wp-tutorials/how-to-create-a-wordpress-plugin/)和[自定义主题](https://www.wpbeginner.com/wp-themes/how-to-easily-create-a-custom-wordpress-theme/)来学习 WordPress 编程。

## 将本地 WordPress 安装移动到实时网站

在本地使用 WordPress 后，您可能希望将 WordPress 安装移动到实时网站。这是其他人能够查看您的网站的唯一方式。

为此，您需要购买[域名和网络托管](https://www.wpbeginner.com/beginners-guide/whats-the-difference-between-domain-name-and-web-hosting-explained/)。域名是您网站在互联网上的地址，网络托管是您网站文件的存储位置。您可以将网络托管视为您的网站在互联网上的家。

对于网络托管，我们建议使用 [Bluehost](https://www.wpbeginner.com/refer/bluehost/)。他们是世界上最大的托管公司之一。它们也是 WordPress. Org 官方推荐的。

幸运的是，[Bluehost](https://www.wpbeginner.com/refer/bluehost/) 为 WPBeginner 用户提供托管折扣、免费 SSL 证书和免费域名。基本上，您可以将本地 WordPress 安装变成一个实时网站，每月只需 2.75 美元。

[→ 单击此处领取 Bluehost 独家优惠 ←](https://www.wpbeginner.com/refer/bluehost/)

购买主机后，请参阅我们关于[如何使用 WordPress 制作网站的](https://www.wpbeginner.com/guides/)文章。

您已经在本地计算机上建立了一个完整的网站吗？那么您可能需要查看有关如何[将 WordPress 从本地服务器移动到实时网站的](https://www.wpbeginner.com/wp-tutorials/how-to-move-wordpress-from-local-server-to-live-site/)指南。

我们希望本文能帮助您了解如何在 Mac 上本地安装 WordPress。您可能还想查看我们关于[如何自定义 WordPress 标头的](https://www.wpbeginner.com/beginners-guide/how-to-customize-your-wordpress-header/)指南，或者查看我们对[管理最佳的 WordPress 托管公司](https://www.wpbeginner.com/managed-wordpress-hosting/)的比较。
