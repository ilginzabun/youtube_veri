from pytube import YouTube
import time

def bilgileri_göster():
    try:
        url = YouTube(input("Bilgileri Görmek İçin Linki Yapıştırınız:"))
        video_sure = url.length / 60
        print("-" * 45)
        print("Video Başlığı:", url.title)
        print("Videonun Sahibi:", url.author)
        print("Videonun Küçük Resmi:", url.thumbnail_url)
        print("İzlenme Sayısı:", url.views)
        print("Video Uzunluğu:", video_sure, "dakika")
        print("-" * 45)
    except Exception as e:
        print("Bir hata oluştu:", e)

def video_indir():
    try:
        url = YouTube(input("Lütfen İndirilecek Video Linkini Yapıştırınız:"))
        video_sure = url.length / 60
        indirme_bağlantısı = url.streams.filter(progressive=True).first()
        indirme_bağlantısı.download()
        print("-" * 45)
        print("Video Başlığı:", url.title)
        print("Videonun Sahibi:", url.author)
        print("İzlenme Sayısı:", url.views)
        print("Video Uzunluğu:", video_sure, "dakika")
        print("-" * 45)
    except Exception as e:
        print("Bir hata oluştu:", e)

def ses_indir():
    try:
        url = YouTube(input("Lütfen İndirilecek Ses Linkini Yapıştırınız:"))
        video_sure = url.length / 60
        indirme_bağlantısı = url.streams.filter(mime_type="audio/mp4").first()
        indirme_bağlantısı.download()
        print("-" * 45)
        print("Ses Başlığı:", url.title)
        print("Ses Sahibi:", url.author)
        print("İzlenme Sayısı:", url.views)
        print("Video Uzunluğu:", video_sure, "dakika")
        print("-" * 45)
    except Exception as e:
        print("Bir hata oluştu:", e)

while True:
    seç = input("1-Youtube Video Bilgilerini Göster\n2-Video indir\n3-Ses İndir\n4-Çıkış\n")
    
    if seç == "1":
        bilgileri_göster()
    elif seç == "2":
        video_indir()
    elif seç == "3":
        ses_indir()
    elif seç == "4":
        print("Çıkış Yapılıyor...")  
        print("5")
        time.sleep(1) 
        print("4")
        time.sleep(1) 
        print("3")
        time.sleep(1) 
        print("2")
        time.sleep(1) 
        print("1")
        time.sleep(1) 
        print("Uygulamadan çıkıldı...") 
        break
    else:
        print("Geçersiz bir seçim yaptınız.")
    
    devam = input("Devam Edilsin mi? (E/H)")
    if devam.lower() != 'e':
        break
