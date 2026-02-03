
download npm file from https://www.oracle.com/downloads/ 
then extract it using 7zip 


```` pwsh
scoop install 7zip
7z x file.rpm -ofile
````

it become cpio file now 


```` pwsh
7z x something.cpio -ofinal_files
````

for runing the program wsl needed 

```` pwsh
wsl --install
````

online suggest fedora for better w

```` pwsh
wsl --install -d Fedora
````



sudo apt update
sudo apt install rpm alien
