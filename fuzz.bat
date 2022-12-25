
:L
set w=%random%
set /a a=1919 
set /a b=1199
set /a y=%w%%%%a% 
set /a x=%w%%%%b%
cd C:\Users\agio\Desktop\新建（不明桌面图标）\AndroidKiller_v1.3.1\bin\adb
adb shell input tap %x%.0 %y%.0
echo %x%.0 %y%.0 >>C:\Users\agio\Desktop\新建（不明桌面图标）\gua\log.txt

goto L