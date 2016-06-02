#include <Misc.au3>
;Sleep(1000)


;While True
;MsgBox (0, "", _IsFullScreenAndClicked ())
;WEnd

;While 1
	;Sleep(1)
;WEnd

Func _IsFullScreenAndClicked ()
    Local $hwnd = WinGetHandle ("[ACTIVE]")
    Local $aWinRect = WinGetPos ($hwnd)
    If ($aWinRect[2] >= @DesktopWidth) Or ($aWinRect[3] >= @DesktopHeight) Then
		While 1
			If _IsPressed("20") Then
				;ShellExecute("builder.py")
				Return True
			EndIf
		WEnd
    Return False
	EndIf
EndFunc



While 1
	Sleep(1000)
	If _IsFullScreenAndClicked ()  Then
		MsgBox(0,"test","test")
		ShellExecute("builder.pyw")
		Sleep(20000)
	EndIf

WEnd

Func _exit()
	Exit
EndFunc