!include "MUI2.nsh"

Name "CHILD Language"
OutFile "CHILDInstaller.exe"
InstallDir "$PROGRAMFILES\CHILD"
InstallDirRegKey HKLM "Software\CHILD" "Install_Dir"
RequestExecutionLevel admin

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_LANGUAGE "English"

Section "Install"

  SetOutPath "$INSTDIR"
  File "..\child.py"
  File "..\pi_helper.py"
  File "..\generate_pi.child"

  ; Copy launcher
  SetOutPath "$INSTDIR\bin"
  File "..\bin\child.bat"

  ; Add PATH
  WriteRegStr HKLM "SYSTEM\CurrentControlSet\Control\Session Manager\Environment" "PATH" "$INSTDIR\bin;%PATH%"
  
  ; Create versioned folder for updates
  CreateDirectory "$INSTDIR\versions"
  ; You can copy future updates there, e.g. child_v1.0.py

  ; Add start menu shortcut
  CreateDirectory "$SMPROGRAMS\CHILD"
  CreateShortCut "$SMPROGRAMS\CHILD\CHILD.lnk" "$INSTDIR\bin\child.bat" "" "$INSTDIR\child.py"

  ; Register file associations
  WriteRegStr HKCR ".child" "" "CHILDScript"
  WriteRegStr HKCR ".chld" "" "CHLDScript"
  WriteRegStr HKCR "CHILDScript\shell\open\command" "" '"$INSTDIR\bin\child.bat" "%1"'
  WriteRegStr HKCR "CHLDScript\shell\open\command" "" '"$INSTDIR\bin\child.bat" "%1"'

SectionEnd

Section "Uninstall"

  Delete "$INSTDIR\child.py"
  Delete "$INSTDIR\pi_helper.py"
  Delete "$INSTDIR\generate_pi.child"
  Delete "$INSTDIR\bin\child.bat"
  RMDir /r "$INSTDIR\bin"
  RMDir /r "$INSTDIR\versions"
  RMDir "$INSTDIR"

  Delete "$SMPROGRAMS\CHILD\CHILD.lnk"
  RMDir "$SMPROGRAMS\CHILD"

  ; Remove registry entries
  DeleteRegKey HKCR ".child"
  DeleteRegKey HKCR ".chld"
  DeleteRegKey HKLM "Software\CHILD"

SectionEnd
