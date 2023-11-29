set R="C:\Program Files\R\R-4.3.1\bin\R.exe"

REM stats
%R% --vanilla < wm.R > wm.out
%R% --vanilla --args 5 < tm.R > tm.out

