@echo off
set /p commitMessage="Enter the commit message: "
git add .
git commit -m "%commitMessage%"
git push origin master
pause
