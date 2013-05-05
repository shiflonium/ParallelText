#subprocess.call(["/usr/bin/pdb", "dictionaryGrabber.py", "-o", "HE", "-d", "EN", "-f", "/home/mitchell/DEVELOPERparalleltextDEVELOPER/paralleltext/texts/Bible_Genesis/EN/ch_1.html"], env={"PATH":"/usr/local/heroku/bin:/usr/lib/lightdm/lightdm:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/lib/jvm/java/bin: /usr/lib/Canopy:/home/mitchell/DEVELOPERparalleltextDEVELOPER/paralleltext/pt_main"})

for ((i=1; i <=50; i++))
do
    python ../../content_mgmt/scripts/dictionaryGrabber.py -o HE -d EN -f=/home/mitchell/ComputerScience/473_WebsiteDesign/DEVELOPERparalleltext/paralleltext/texts/Bible_Genesis/EN/ch_i.html
done