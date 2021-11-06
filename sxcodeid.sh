# code by @riskiakbar279
# website : riskiakbar279.rf.gd
# artikel  : sxcodeprogrammerid.xyz

#import system
 figlet SXCODE ID SEC| lolcat
                  
 sleep 1
 echo "CODE BY RISKIAKBAR279" | lolcat        
 sleep 1                      
 echo "INFORMATION GATHERING"|lolcat
 echo "untuk cara pakai baca di link berikut : [https://]"|lolcat
  sleep 1
                                        
 echo "[1] BUG-scan   " | toilet -f term -F border |lolcat
 echo "[2] DIR-scan   " | toilet -f term -F border |lolcat                   
 echo "[3] NEWSHODAN     " | toilet -f term -F border |lolcat           
 echo "[4] DORK-scan  " | toilet -f term -F border |lolcat
 echo "[5] CEK 200K  " | toilet -f term -F border |lolcat               
 echo "[6] DOMMAP " | toilet -f term -F border |lolcat
 echo "[7] HASHDENEC " | toilet -f term -F border |lolcat
 echo "[8] 200KAKTIF" | toilet -f term -F border |lolcat 
 echo "[0] BAHAN      " | toilet -f term -F border |lolcat
 echo "[x] EXIT       " | toilet -f term -F border
read -p "PILIH NOMOR :" no;



case $no in
1)
python2 scanbug.py
;;
2)
python2 scandir.py
;;
3) 
python2 scanshodan.py
;;
4) 
python3 scangodork.py
;;
5) 
python2 scan200k.py
;;  
6)
python2 scanmap.py
;;
7)
 python3 hasher-bugs.py
;;
8)
 python2 domainscanaktif.py
;;
99)
 bahan.sh
;;
x)
exit
;;
*) echo "undefinded"
esac
         
  
