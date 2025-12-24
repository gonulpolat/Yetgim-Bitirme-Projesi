# 🍬 Candy Crush -  by GonulPolat
Python ve Pygame kullanılarak geliştirilmiş, modern ve eğlenceli bir eşleşme-3 (match-3) puzzle oyunu.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Pygame](https://img.shields.io/badge/pygame-2.0+-green.svg)

## 📋 İçindekiler

- [Özellikler](#-özellikler)
- [Ekran Görüntüleri](#-ekran-görüntüleri)
- [Kurulum](#-kurulum)
- [Nasıl Oynanır](#-nasıl-oynanır)
- [Proje Yapısı](#-proje-yapısı)


## ✨ Özellikler

- 🎮 **8x8 Izgara Sistemi** - Klasik Candy Crush benzeri oyun tahtası
- 🍩 **6 Farklı Şeker Tipi** - Renkli ve emoji destekli şekerler
- 🎯 **Hamle Limiti** - 20 hamle ile stratejik düşünme
- 💯 **Puan Sistemi** - Her eşleşme için puan kazanma
- 🎬 **Düzgün Animasyonlar** - Şekerlerin düşme ve kayma animasyonları
- 🔄 **Otomatik Eşleşme** - Zincirleme eşleşmeler otomatik tespit edilir
- 🏆 **Oyun Sonu Modalı** - Güzel tasarlanmış sonuç ekranı
- ⚙️ **Modüler Kod Yapısı** - Temiz, anlaşılır ve genişletilebilir

## 🎮 Ekran Görüntüleri


![Oyun](screenshots/game.png)

![Oyun Sonu](screenshots/game-end.png)

## 🚀 Kurulum

### Gereksinimler

- Python 3.7 veya üzeri
- pip (Python paket yöneticisi)
- pygame==2.6.1


## 🎯 Nasıl Oynanır

### Temel Kurallar

1. **Şeker Seçme:** Bir şekere tıklayın (yeşil arka plan belirir)
2. **Değiştirme:** Komşu bir şekere tıklayın (sadece yatay/dikey)
3. **Eşleşme:** 3 veya daha fazla aynı tipte şeker yan yana gelirse patlar
4. **Puan:** Her eşleşen şeker için 10 puan kazanırsınız
5. **Hamle:** Toplam 20 hamle hakkınız var

### Oyun Kontrolleri

| Tuş | Açıklama |
|-----|----------|
| **Sol Tık** | Şeker seç/değiştir |
| **R** | Oyunu yeniden başlat |
| **ESC** | Oyundan çık |

### Stratejiler

- 🎯 **4-5'li Eşleşmeler:** Daha fazla puan için büyük eşleşmeler yapmaya çalışın
- 🔄 **Zincirleme:** Tek hamlede birden fazla eşleşme yaratın
- 📊 **Planlama:** Son hamlelerinizi stratejik kullanın
- 🎲 **Şans:** Bazen beklemek yeni fırsatlar yaratabilir

## 📁 Proje Yapısı

```
Yetgim-Bitirme-Projesi/
│
├── main.py              
├── config.py          
├── seker.py             
├── oyun.py      
├── utils.py            
├── README.md              
├── requirements.txt             
└── .gitignore
```

### Dosya Açıklamaları

#### `config.py`
Oyunun tüm sabit değerlerini içerir:
- Pencere boyutları
- Renkler
- Şeker tipleri
- Oyun ayarları (FPS, hamle limiti, puan çarpanı)

#### `seker.py`
Her bir şekeri temsil eden `Seker` sınıfı:
- Pozisyon yönetimi
- Animasyon kontrolü
- Çizim fonksiyonları

#### `oyun.py`
Ana oyun mantığını içeren `CandyCrush` sınıfı:
- Izgara yönetimi
- Eşleşme algoritmaları
- Şeker düşürme ve yeni şeker ekleme
- Puan hesaplama

#### `utils.py`
Genel amaçlı yardımcı fonksiyonlar:
- UI çizim fonksiyonları
- Koordinat dönüşümleri
- Modal pencere

#### `main.py`
Oyun döngüsü ve event yönetimi:
- Pygame başlatma
- Ana oyun döngüsü
- Klavye ve fare input yönetimi