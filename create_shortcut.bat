@echo off
setlocal

:: 创建VBScript文件来创建快捷方式
echo Set oWS = WScript.CreateObject^("WScript.Shell"^) > CreateShortcut.vbs
echo sLinkFile = "%USERPROFILE%\Desktop\视频截图工具.lnk" >> CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut^(sLinkFile^) >> CreateShortcut.vbs
echo oLink.TargetPath = "D:\video_screenshot_tool\start_gui.vbs" >> CreateShortcut.vbs
echo oLink.WorkingDirectory = "D:\video_screenshot_tool" >> CreateShortcut.vbs
echo oLink.Save >> CreateShortcut.vbs

:: 运行VBScript创建快捷方式
cscript CreateShortcut.vbs

:: 删除临时VBScript文件
del CreateShortcut.vbs

echo 快捷方式已创建到桌面
echo 按任意键退出...
pause >nul