@echo off
REM ==============================================================================
REM MP4转MP3转换器 - 快速打包脚本（中文版）
REM 使用PyInstaller打包成独立exe文件
REM ==============================================================================

echo.
echo ============================================
echo MP4转MP3转换器 - 中文版打包
echo ============================================
echo.

REM 设置编码为UTF-8
chcp 65001 >nul 2>&1

REM 检查Python是否可用
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误：未找到Python。请先安装Python并添加到系统PATH。
    pause
    exit /b 1
)

echo 1. 检查依赖...
echo.

REM 安装/检查 moviepy
python -c "import moviepy" >nul 2>&1
if errorlevel 1 (
    echo 正在安装 moviepy...
    pip install moviepy
)

REM 安装/检查 imageio-ffmpeg
python -c "import imageio_ffmpeg" >nul 2>&1
if errorlevel 1 (
    echo 正在安装 imageio-ffmpeg...
    pip install imageio-ffmpeg
)

REM 安装/检查 PyInstaller
python -c "import PyInstaller" >nul 2>&1
if errorlevel 1 (
    echo 正在安装 PyInstaller...
    pip install pyinstaller
)

echo.
echo 2. 开始打包GUI版本（图形界面）...
echo ============================================
echo.

REM 清理旧的构建文件
if exist "build" (
    echo 清理构建缓存...
    rmdir /s /q build >nul 2>&1
)

if exist "dist\MP4转MP3转换器.exe" (
    echo 删除旧的exe文件...
    del /f "dist\MP4转MP3转换器.exe" >nul 2>&1
)

REM 打包GUI版本（无控制台窗口）
pyinstaller --name "MP4转MP3转换器" --noconfirm --clean --onefile --windowed --hidden-import="moviepy" --hidden-import="moviepy.video.io.VideoFileClip" --hidden-import="imageio_ffmpeg" src\skill_seekers\cli\mp4_to_mp3_converter_gui_cn.py

if errorlevel 1 (
    echo.
    echo 错误：打包GUI版本失败！
    pause
    exit /b 1
)

echo.
echo 3. 打包完成！
echo ============================================
echo.

if exist "dist\MP4转MP3转换器.exe" (
    echo 成功！文件已保存到: dist\MP4转MP3转换器.exe
    echo.
    echo 使用方法:
    echo - 双击运行，启动图形界面
    echo - 选择转换模式（单个文件或批量转换）
    echo - 选择输入和输出路径
    echo - 点击"开始转换"按钮
    echo.
    echo 提示: 首次运行可能需要几秒钟初始化和解压依赖
    echo.

    REM 打开输出目录
    explorer "dist"
) else (
    echo 错误：未找到生成的exe文件
)

echo.
pause
