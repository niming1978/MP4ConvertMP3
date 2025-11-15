@echo off
REM ==============================================================================
REM MP4转MP3转换器 - 中文版打包脚本
REM 使用PyInstaller打包成独立exe文件
REM ==============================================================================

echo ============================================
echo MP4转MP3转换器 - 中文版打包
echo ============================================
echo.

REM 检查Python是否可用
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误：未找到Python。请先安装Python并添加到系统PATH。
    pause
    exit /b 1
)

echo 正在检查依赖...
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo 正在安装PyInstaller...
    pip install pyinstaller
)

pip show imageio-ffmpeg >nul 2>&1
if errorlevel 1 (
    echo 正在安装 imageio-ffmpeg...
    pip install imageio-ffmpeg
)

echo.
echo ============================================
echo 开始打包GUI版本（图形界面）...
echo ============================================
echo.

REM 清理旧的构建文件
if exist "dist\MP4转MP3转换器" (
    echo 清理旧的构建文件...
    rmdir /s /q "dist\MP4转MP3转换器" >nul 2>&1
)

if exist "build" (
    echo 清理构建缓存...
    rmdir /s /q build >nul 2>&1
)

REM 打包GUI版本（无控制台窗口）
pyinstaller ^
    --name "MP4转MP3转换器" ^
    --noconfirm ^
    --clean ^
    --onefile ^
    --windowed ^
    --add-data "venv\Lib\site-packages\imageio_ffmpeg\binaries;imageio_ffmpeg\binaries" ^
    --hidden-import="moviepy" ^
    --hidden-import="moviepy.video" ^
    --hidden-import="moviepy.audio" ^
    --hidden-import="moviepy.video.io" ^
    --hidden-import="moviepy.audio.io" ^
    --hidden-import="imageio" ^
    --hidden-import="imageio.plugins.ffmpeg" ^
    --hidden-import="imageio_ffmpeg" ^
    --hidden-import="PIL" ^
    --hidden-import="numpy" ^
    --exclude-module="matplotlib" ^
    --exclude-module="pytest" ^
    --exclude-module="IPython" ^
    src\skill_seekers\cli\mp4_to_mp3_converter_gui_cn.py

if errorlevel 1 (
    echo.
    echo 错误：打包GUI版本失败！
    pause
    exit /b 1
)

echo.
echo ============================================
echo GUI版本打包完成！
echo ============================================
echo.

REM 打包命令行版本
echo.
echo ============================================
echo 开始打包命令行版本...
echo ============================================
echo.

pyinstaller ^
    --name "MP4转MP3转换器_CMD" ^
    --noconfirm ^
    --clean ^
    --onefile ^
    --console ^
    --add-data "venv\Lib\site-packages\imageio_ffmpeg\binaries;imageio_ffmpeg\binaries" ^
    --hidden-import="moviepy" ^
    --hidden-import="moviepy.video" ^
    --hidden-import="moviepy.audio" ^
    --hidden-import="moviepy.video.io" ^
    --hidden-import="moviepy.audio.io" ^
    --hidden-import="imageio" ^
    --hidden-import="imageio.plugins.ffmpeg" ^
    --hidden-import="imageio_ffmpeg" ^
    --hidden-import="PIL" ^
    --hidden-import="numpy" ^
    --exclude-module="tkinter" ^
    --exclude-module="matplotlib" ^
    --exclude-module="pytest" ^
    --exclude-module="IPython" ^
    src\skill_seekers\cli\mp4_to_mp3_converter_cn.py

if errorlevel 1 (
    echo.
    echo 错误：打包命令行版本失败！
    pause
    exit /b 1
)

echo.
echo ============================================
echo 命令行版本打包完成！
echo ============================================
echo.

REM 显示打包结果
echo.
echo ============================================
echo 打包完成！
echo ============================================
echo.
echo GUI版本（双击运行）:
echo   - 文件: dist\MP4转MP3转换器.exe
echo   - 大小: 约50-80MB（包含所有依赖）
echo   - 用法: 双击运行，图形界面操作
echo.
echo 命令行版本:
echo   - 文件: dist\MP4转MP3转换器_CMD.exe
echo   - 大小: 约50-80MB（包含所有依赖）
echo   - 用法: 在命令提示符中运行
echo.
echo ============================================
echo 注意：首次运行可能需要几秒钟加载
echo       因为需要解压相关组件到临时目录
echo ============================================
echo.

REM 打开输出目录
explorer "dist"

pause
