Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "c:\Users\rahul\safety-intelligence-dashboard"
WshShell.Run """C:\Users\rahul\AppData\Local\Programs\Python\Python314\pythonw.exe"" ""c:\Users\rahul\safety-intelligence-dashboard\serve.py""", 0, False
