while true
do
        sudo zmap -N 15 -p 80 -o list.lst -i eth1
        awk '$0="https://"$0' list.lst > l1
        python3 speyeder.py -f l1      
done
