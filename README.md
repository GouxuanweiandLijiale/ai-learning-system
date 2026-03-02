今日所学总结
1. 环境配置

我们确认了 VS Code 和 Python 的设置已经正常，并且确保了 ai_lab 虚拟环境的激活。

使用 python -c "import sys; print(sys.executable)" 检查了 Python 解释器的路径，确保在 ai_lab 环境中运行。

2. Git 基础操作

熟悉了 git status, git add, git commit 等常用命令，并通过 git init 初始化了 Git 仓库。

确认了如何处理“文件删除”相关的问题（通过 git status 看到删除的文件和未提交的修改）。

3. 项目初始化

完成了 test_python.py 文件的创建，确保它能正常运行：

print("Hello! ai_lab is working.")

确保项目初始化后，Git 仓库和文件结构清晰，但在删除和重命名文件时遇到了一些问题。

4. Git 历史管理

你遇到的问题是：删除了一些文件，但它们依然存在于 Git 历史中（通过 git status 显示）。这是因为 Git 记录了历史，但并没有自动删除已删文件。

解决方案是通过 rmdir /s /q .git 清除掉 .git 文件夹，然后重新初始化 Git 仓库，开始全新的提交记录。

今天遇到的问题

Git 状态未更新：
删除文件后，Git 需要通过 git add . 和 git commit 来更新状态，否则它会继续提示这些文件已被删除但未提交。

路径不一致问题：
由于在多个不同磁盘间切换，导致了 test_python.py 文件无法找到。问题最终通过确保文件路径一致和在正确的目录下操作解决。

文件和 Git 历史混乱：
删除文件后，Git 仍保留了文件删除记录，导致 Git 提示错误。通过删除 .git 目录并重新初始化 Git 仓库解决了这个问题。