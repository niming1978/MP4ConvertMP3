<div align="center">

# 🎵 MP4转MP3转换器

### 将MP4视频文件转换为MP3音频文件的桌面工具

[![Windows](https://img.shields.io/badge/Windows-10%2F11-blue.svg)](https://www.microsoft.com/windows/)
[![Python](https://img.shields.io/badge/Python-3.12-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![中文](https://img.shields.io/badge/语言-中文-red.svg)](#)

</div>

---

## 📸 截图

<div align="center">

| 主界面 | 批量转换 |
|--------|----------|
| ![主界面](screenshots/main.png) | ![批量转换](screenshots/batch.png) |

</div>

---

## ✨ 功能特点

### 🎯 核心功能
- ✅ **单个文件转换** - 选择MP4文件，一键转换为MP3
- ✅ **批量转换** - 整个目录的所有MP4文件一次性转换
- ✅ **进度显示** - 实时显示转换进度和状态
- ✅ **日志记录** - 详细记录转换过程，方便排查问题

### 🔧 技术特点
- 🚀 **完全独立运行** - 无需安装Python、FFmpeg或其他任何依赖
- 💻 **跨平台GUI** - 基于Tkinter，原生Windows体验
- 📝 **纯中文界面** - 所有提示、按钮、错误信息均为中文
- 📦 **单文件分发** - 只需一个exe文件，双击即用

### 🎨 用户体验
- 🎯 **简洁直观** - 三步完成转换：选择文件 → 点击转换 → 完成
- ⚡ **快速高效** - 基于moviepy和ffmpeg，转换速度快
- 💾 **自动保存** - 智能生成输出文件名，避免重复操作
- 🔔 **完成提醒** - 转换完成后自动提示

---

## 📥 下载使用

### 🚀 快速开始

1. **下载程序**
   - 前往 [Releases](https://github.com/yourusername/mp4-to-mp3-converter/releases) 页面
   - 下载最新版本的 `MP4转MP3转换器.exe`

2. **运行程序**
   ```bash
   # 双击运行（无需安装）
   MP4转MP3转换器.exe
   ```

3. **开始转换**
   - 选择转换模式（单个文件/批量转换）
   - 选择输入文件或目录
   - 点击"开始转换"按钮
   - 等待转换完成

### 📦 文件列表

```
dist/
├── MP4转MP3转换器.exe    # 主程序（56MB）
├── 使用说明.txt          # 详细使用文档
└── ...
```

---

## 🖥️ 系统要求

| 项目 | 要求 |
|------|------|
| **操作系统** | Windows 10/11 (64位) |
| **存储空间** | 至少 100MB 可用空间 |
| **内存** | 至少 512MB RAM |
| **权限** | 需要读取/写入文件权限 |

---

## 📖 使用说明

### 🎯 单个文件转换

1. 启动程序，选择"单个文件"模式
2. 点击"浏览..."选择要转换的MP4文件
3. （可选）选择输出MP3文件的保存位置
4. 点击"开始转换"按钮
5. 等待进度条完成，查看日志确认成功

### 📁 批量转换目录

1. 选择"批量转换（目录）"模式
2. 点击"浏览..."选择包含MP4文件的输入目录
3. 点击"浏览..."选择保存MP3文件的输出目录
4. 点击"开始转换"按钮
5. 程序会自动转换目录中的所有MP4文件
6. 查看日志了解转换结果（成功/失败数量）

### 📊 界面说明

- **转换模式**：切换单个文件和批量转换
- **进度条**：显示当前转换进度（0-100%）
- **状态标签**：显示"准备就绪"、"转换中"等状态
- **转换日志**：详细记录每个文件的转换过程
- **开始转换**：绿色按钮，启动转换过程
- **清空日志**：灰色按钮，清除日志内容
- **退出**：红色按钮，退出程序

---

## 🛠️ 技术栈

### 核心技术
- **Python 3.12** - 编程语言
- **MoviePy** - 视频处理库
- **FFmpeg** - 音视频编解码（通过imageio-ffmpeg）
- **Tkinter** - GUI图形界面框架

### 打包工具
- **PyInstaller** - 将Python程序打包成独立exe
- **UPX** - 可执行文件压缩

### 开发环境
- **操作系统**: Windows 11
- **Python版本**: 3.12.10
- **IDE**: VS Code / PyCharm

---

## 🚀 开发指南

### 环境搭建

```bash
# 克隆项目
git clone https://github.com/yourusername/mp4-to-mp3-converter.git
cd mp4-to-mp3-converter

# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt
```

### 安装依赖

```bash
# 核心依赖
pip install moviepy imageio-ffmpeg

# 开发依赖
pip install pyinstaller
```

### 从源码运行

```bash
# 运行GUI版本
python src/skill_seekers/cli/mp4_to_mp3_converter_gui_cn.py

# 运行命令行版本
python src/skill_seekers/cli/mp4_to_mp3_converter_cn.py --help
```

### 打包程序

```bash
# 使用spec文件打包
python -m PyInstaller build_fixed.spec

# 打包后的文件在 dist/ 目录
# MP4转MP3转换器.exe
```

---

## 📂 项目结构

```
MP4-to-MP3-Converter/
├── src/
│   └── skill_seekers/
│       └── cli/
│           ├── mp4_to_mp3_converter_gui_cn.py      # GUI版本（中文）
│           ├── mp4_to_mp3_converter_gui_cn_fixed.py # 修复版
│           └── mp4_to_mp3_converter_cn.py          # 命令行版本（中文）
├── build_fixed.spec                                 # PyInstaller配置
├── requirements.txt                                 # 依赖列表
├── README_CN.md                                     # 中文说明文档
├── dist/
│   ├── MP4转MP3转换器.exe                          # 主程序
│   └── 使用说明.txt                                 # 使用文档
└── screenshots/                                     # 截图
    ├── main.png
    └── batch.png
```

---

## 🐛 常见问题

### Q: 程序无法启动？
**A:**
- 确保操作系统是Windows 10/11 (64位)
- 检查是否有杀毒软件阻止了程序运行
- 尝试以管理员身份运行

### Q: 转换失败？
**A:**
- 检查输入文件是否为有效的视频文件
- 确保输出目录有写入权限
- 检查磁盘空间是否充足
- 查看日志区域的错误信息

### Q: 转换后的文件在哪里？
**A:**
- 单个文件：默认在MP4文件同目录
- 批量转换：在指定的输出目录

### Q: 支持哪些视频格式？
**A:**
- 主要支持MP4格式
- 也支持AVI、MKV等常见格式（取决于FFmpeg支持）

### Q: 可以转换多大的文件？
**A:**
- 理论上没有文件大小限制
- 转换速度取决于文件大小和电脑性能
- 建议单个文件不超过2GB

---

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

### 报告Bug
- 使用GitHub Issue模板
- 提供操作系统版本、错误截图、日志信息
- 提供重现步骤

### 功能建议
- 欢迎提出新功能建议
- 我们会评估可行性和实用性

### 代码贡献
1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

---

## 🙏 致谢

- [MoviePy](https://github.com/Zulko/moviepy) - 视频处理库
- [FFmpeg](https://ffmpeg.org/) - 音视频编解码
- [PyInstaller](https://www.pyinstaller.org/) - 打包工具

---

## 📞 联系方式

- 项目地址: [https://github.com/yourusername/mp4-to-mp3-converter](https://github.com/yourusername/mp4-to-mp3-converter)
- 问题反馈: [Issues](https://github.com/yourusername/mp4-to-mp3-converter/issues)
- 电子邮件: your.email@example.com

---

<div align="center">

**如果觉得这个项目有帮助，请给个 ⭐ Star！**

</div>
