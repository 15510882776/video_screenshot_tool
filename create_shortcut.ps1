$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("C:\Users\15510\Desktop\视频截图工具.lnk")
$Shortcut.TargetPath = "D:\video_screenshot_tool\start_gui.vbs"
$Shortcut.WorkingDirectory = "D:\video_screenshot_tool"
$Shortcut.Save()
Write-Host "快捷方式创建成功"