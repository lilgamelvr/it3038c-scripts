function getIP{ 

    (get-netipaddress).ipv4address | Select-String "192*" 

} 

$IP = getIP | Select-Object -first 1

$USER = Get-LocalUser | Select-Object -first 1

$DATE = Get-Date -UFormat "%A %d %B %Y"

$BODY = "This machine's IP is " + $IP + " User is " + $USER + " Hostname is " + $env:computername + " PowerShell Version " + $HOST.Version.Major + " Today's Date is " + $DATE

Write-Output $BODY

$BODY | Out-File -FilePath .\Lab3.txt