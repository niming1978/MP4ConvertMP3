# MP4转MP3转换器 - 打包指南

本文档介绍如何将MP4转MP3转换器打包成独立的exe文件。

## 准备工作

### 1. 安装Python
确保已安装Python 3.10或更高版本：

```bash
python --version
```

### 2. 安装依赖

```bash
# 安装核心依赖
pip install moviepy imageio-ffmpeg

# 安装打包工具
pip install pyinstaller
```

### 3. 验证安装

```bash
python -c "from moviepy import VideoFileClip; print('OK')"
```

## 打包步骤

### 方法1：使用spec文件（推荐）

我们已经提供了配置好的spec文件，直接运行即可：

```bash
# 打包GUI版本（图形界面）
python -m PyInstaller build_fixed.spec

# 打包完成后的文件在 dist/ 目录
# 主程序: dist/MP4转MP3转换器_最终版.exe
```

### 方法2：手动打包

如果不想使用spec文件，可以手动打包：

```bash
# GUI版本（推荐）
pyinstaller \
    --name "MP4转MP3转换器" \
    --onefile \
    --windowed \
    --hidden-import="moviepy" \
    --hidden-import="moviepy.video.io.VideoFileClip" \
    --hidden-import="imageio_ffmpeg" \
    src/skill_seekers/cli/mp4_to_mp3_converter_gui_cn_fixed.py

# 命令行版本
pyinstaller \
    --name "MP4转MP3转换器_CMD" \
    --onefile \
    --console \
    --hidden-import="moviepy" \
    src/skill_seekers/cli/mp4_to_mp3_converter_cn.py
```

## 打包后处理

打包完成后，建议进行以下操作：

### 1. 测试程序

双击运行生成的exe文件，确保：
- [ ] 程序能够启动
- [ ] 界面显示正常
- [ ] 可以正常选择文件
- [ ] 转换功能正常工作

### 2. 清理临时文件

```bash
# 删除构建缓存（可选）
rm -rf build/
rm -rf dist/  # 如果不需要分发文件
```

### 3. 创建发布包

```bash
# 创建发布目录
mkdir release
cp "dist/MP4转MP3转换器_最终版.exe" release/
cp "使用说明.txt" release/
cp "README_CN.md" release/

# 压缩发布包
zip -r MP4转MP3转换器_v1.0.0.zip release/
```

## 常见问题

### Q1: 打包时出现"Module Not Found"错误？

**A:** 添加 `--hidden-import` 参数：

```bash
--hidden-import="package_name"
```

### Q2: 运行exe时提示"imageio metadata not found"？

**A:** 使用spec文件打包，或手动添加元数据：

```python
# 在spec文件中添加
from PyInstaller.utils.hooks import copy_metadata
datas = copy_metadata('imageio')
```

### Q3: 打包后的文件太大？

**A:** 这是正常的，因为打包包含了：
- Python解释器
- moviepy库
- ffmpeg（约40MB）
- numpy等依赖

可以使用UPX压缩减小体积：

```bash
# 安装UPX
# 然后在pyinstaller命令中添加
--upx-dir=/path/to/upx
```

### Q4: 界面文字显示异常？

**A:** 确保spec文件中包含了正确的字符编码：

```python
# -*- mode: python ; coding: utf-8 -*-
```

### Q5: 按钮显示不全？

**A:** 调整窗口高度，确保：

```python
self.root.geometry("650x600")  # 宽度x高度
```

## 自动化打包

使用提供的脚本自动完成打包：

```bash
# Windows
build_simple.bat

# 或 Linux/Mac
python build_package.py
```

## 最佳实践

1. **版本管理**
   - 在代码中定义版本号
   - 在README中更新版本
   - 使用Git标签标记发布

2. **测试**
   - 在不同Windows版本上测试
   - 测试不同类型的MP4文件
   - 测试批量转换功能

3. **发布**
   - 提供完整的说明文档
   - 包含使用截图
   - 列出已知问题和限制

4. **优化**
   - 使用最新版本的依赖
   - 及时更新安全补丁
   - 监控用户反馈

## 技术支持

如遇到问题，请：
1. 查看 [README_CN.md](./README_CN.md)
2. 查看 [使用说明.txt](./dist/使用说明.txt)
3. 提交Issue到GitHub

---

**祝打包顺利！**
