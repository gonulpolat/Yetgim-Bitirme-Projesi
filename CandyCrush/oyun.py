"""
    Bu modül Candy Crush oyununun ana oyun sınıfını içerir.
"""

import random
from config import *
from seker import Seker
from utils import *


class CandyCrush:
    '''Ana oyun sınıfı - tüm oyun mantığını yönetir'''
    
    def __init__(self):
        '''Oyunu başlat ve ilk durumu oluştur'''
        self.izgara = []  # Şeker tablosunu tutacak 2D liste
        self.secili_seker = None  # Seçili şeker (varsa)
        self.puan = 0  # Oyuncu puanı
        self.kalan_hamle = MAKSIMUM_HAMLE  # Kalan hamle sayısı
        self.animasyon_devam_ediyor = False  # Animasyon kontrolü
        self.oyun_bitti = False  # Oyun bitişi kontrolü
        self.izgarayi_olustur()
    
    def izgarayi_olustur(self):
        '''
        8x8'lik şeker tablosunu rastgele oluşturur
        Başlangıçta eşleşme olmayacak şekilde düzenler
        '''
        self.izgara = []
        for satir in range(IZGARA_BOYUTU):
            satir_listesi = []
            for sutun in range(IZGARA_BOYUTU):
                tip = random.randint(0, len(SEKER_RENKLERI) - 1)
                seker = Seker(satir, sutun, tip)
                satir_listesi.append(seker)
            self.izgara.append(satir_listesi)
        
        # Başlangıçta eşleşme varsa temizle
        self.baslangic_eslesmelerini_temizle()
    
    def baslangic_eslesmelerini_temizle(self):
        '''Oyun başlarken varolan eşleşmeleri kaldırır'''
        for _ in range(100):  # Maksimum 100 deneme
            eslesmeler = self.eslesmeler_bul()
            if not eslesmeler:
                break
            # Eşleşen şekerlerin tipini değiştir
            for satir, sutun in eslesmeler:
                yeni_tip = random.randint(0, len(SEKER_RENKLERI) - 1)
                self.izgara[satir][sutun].tip = yeni_tip
                self.izgara[satir][sutun].renk = SEKER_RENKLERI[yeni_tip]
                self.izgara[satir][sutun].sembol = SEKER_SEMBOLLERI[yeni_tip]
    
    def eslesmeler_bul(self):
        '''
        Tablodaki tüm 3'lü eşleşmeleri bulur
        
        Returns:
            list: Eşleşen şekerlerin (satir, sutun) koordinatları
        '''
        eslesmeler = set()  # Tekrar önlemek için set kullan
        
        # Yatay eşleşmeler (→)
        for satir in range(IZGARA_BOYUTU):
            for sutun in range(IZGARA_BOYUTU - 2):
                tip = self.izgara[satir][sutun].tip
                if (tip == self.izgara[satir][sutun + 1].tip == 
                    self.izgara[satir][sutun + 2].tip):
                    eslesmeler.add((satir, sutun))
                    eslesmeler.add((satir, sutun + 1))
                    eslesmeler.add((satir, sutun + 2))
        
        # Dikey eşleşmeler (↓)
        for satir in range(IZGARA_BOYUTU - 2):
            for sutun in range(IZGARA_BOYUTU):
                tip = self.izgara[satir][sutun].tip
                if (tip == self.izgara[satir + 1][sutun].tip == 
                    self.izgara[satir + 2][sutun].tip):
                    eslesmeler.add((satir, sutun))
                    eslesmeler.add((satir + 1, sutun))
                    eslesmeler.add((satir + 2, sutun))
        
        return list(eslesmeler)
    
    def sekerleri_swap(self, seker1, seker2):
        '''
        İki şekerin yerini değiştirir
        
        Args:
            seker1 (Seker): İlk şeker
            seker2 (Seker): İkinci şeker
        '''
        # Izgara üzerindeki referansları değiştir
        satir1, sutun1 = seker1.satir, seker1.sutun
        satir2, sutun2 = seker2.satir, seker2.sutun
        
        # Izgara içindeki referansları swap et
        self.izgara[satir1][sutun1] = seker2
        self.izgara[satir2][sutun2] = seker1
        
        # Şekerlerin kendi pozisyon bilgilerini güncelle
        seker1.hedef_pozisyon_ayarla(satir2, sutun2)
        seker2.hedef_pozisyon_ayarla(satir1, sutun1)
        
        self.animasyon_devam_ediyor = True
    
    def eslesen_sekerleri_sil(self, eslesmeler):
        '''
        Eşleşen şekerleri siler (None yapar)
        
        Args:
            eslesmeler (list): Silinecek (satir, sutun) listesi
        '''
        for satir, sutun in eslesmeler:
            self.izgara[satir][sutun] = None
        self.puan += len(eslesmeler) * PUAN_CARPANI
    
    def sekerleri_dus(self):
        '''
        Boş hücrelere üstteki şekerleri düşürür
        '''
        degisiklik_oldu = False
        
        # Her sütunu aşağıdan yukarıya tara
        for sutun in range(IZGARA_BOYUTU):
            # Boş pozisyonu bul (aşağıdan başla)
            bos_satir = None
            for satir in range(IZGARA_BOYUTU - 1, -1, -1):
                if self.izgara[satir][sutun] is None:
                    bos_satir = satir
                    break
            
            # Boş pozisyon varsa, üstteki şekerleri aşağı kaydır
            if bos_satir is not None:
                for satir in range(bos_satir - 1, -1, -1):
                    if self.izgara[satir][sutun] is not None:
                        seker = self.izgara[satir][sutun]
                        self.izgara[bos_satir][sutun] = seker
                        self.izgara[satir][sutun] = None
                        
                        seker.hedef_pozisyon_ayarla(bos_satir, sutun)
                        
                        bos_satir -= 1
                        degisiklik_oldu = True
                        
                        if bos_satir < 0:
                            break
        
        if degisiklik_oldu:
            self.animasyon_devam_ediyor = True
        
        return degisiklik_oldu
    
    def yeni_sekerler_ekle(self):
        '''
        Üstteki boş hücrelere yeni şekerler ekler
        '''
        for sutun in range(IZGARA_BOYUTU):
            for satir in range(IZGARA_BOYUTU):
                if self.izgara[satir][sutun] is None:
                    tip = random.randint(0, len(SEKER_RENKLERI) - 1)
                    seker = Seker(satir, sutun, tip)
                    # Yeni şekeri ızgaranın üstünden başlat
                    seker.y = IZGARA_Y - (IZGARA_BOYUTU - satir) * HUCRE_BOYUTU
                    seker.animasyon_bitti = False
                    self.izgara[satir][sutun] = seker
                    self.animasyon_devam_ediyor = True
    
    def animasyonlari_guncelle(self):
        '''
        Tüm şekerlerin animasyonlarını günceller
        
        Returns:
            bool: Tüm animasyonlar bitti mi?
        '''
        tum_animasyonlar_bitti = True
        
        for satir in self.izgara:
            for seker in satir:
                if seker is not None:
                    if not seker.animasyon_guncelle():
                        tum_animasyonlar_bitti = False
        
        if tum_animasyonlar_bitti:
            self.animasyon_devam_ediyor = False
        
        return tum_animasyonlar_bitti
    
    def eslesmeleri_isle(self):
        '''
        Eşleşmeleri bulur ve işler
        '''
        eslesmeler = self.eslesmeler_bul()
        
        if eslesmeler:
            self.eslesen_sekerleri_sil(eslesmeler)
            return True
        return False
    
    def otomatik_islem_yap(self):
        '''
        Animasyon bittiyse otomatik işlemleri yap
        '''
        if self.animasyon_devam_ediyor or self.oyun_bitti:
            return
        
        # Şekerleri düşür
        dusme_oldu = self.sekerleri_dus()
        
        if dusme_oldu:
            return
        
        # Boş yer varsa yeni şeker ekle
        bos_var = False
        for satir in self.izgara:
            for seker in satir:
                if seker is None:
                    bos_var = True
                    break
            if bos_var:
                break
        
        if bos_var:
            self.yeni_sekerler_ekle()
            return
        
        # Eşleşme var mı kontrol et
        self.eslesmeleri_isle()
    
    def tiklama_isle(self, fare_x, fare_y):
        '''
        Fare tıklamasını işler
        '''
        # Oyun bittiyse veya animasyon devam ediyorsa tıklamayı kabul etme
        if self.animasyon_devam_ediyor or self.oyun_bitti:
            return
        
        # Hamle kalmadıysa tıklamayı kabul etme
        if self.kalan_hamle <= 0:
            return
        
        # Fare ızgara içinde mi?
        pozisyon = piksel_to_izgara(fare_x, fare_y)
        if pozisyon is None:
            return
        
        satir, sutun = pozisyon
        tiklanan_seker = self.izgara[satir][sutun]
        
        if tiklanan_seker is None:
            return
        
        # İlk tıklama: Şeker seç
        if self.secili_seker is None:
            self.secili_seker = tiklanan_seker
            tiklanan_seker.secili = True
            return
        
        # Aynı şekere tekrar tıklama: Seçimi kaldır
        if tiklanan_seker == self.secili_seker:
            self.secili_seker.secili = False
            self.secili_seker = None
            return
        
        # Komşu şekere tıklama: Değiştirmeyi dene
        if komsu_mu(self.secili_seker, tiklanan_seker):
            # Swap yap
            seker1 = self.secili_seker
            seker2 = tiklanan_seker
            
            self.sekerleri_swap(seker1, seker2)
            self.kalan_hamle -= 1  # Hamle sayısını azalt
            
            # Hamle bittiyse oyunu bitir
            if self.kalan_hamle <= 0:
                self.oyun_bitti = True
            
            # Seçimi kaldır
            seker1.secili = False
            self.secili_seker = None
        else:
            # Komşu değil, seçimi değiştir
            self.secili_seker.secili = False
            self.secili_seker = tiklanan_seker
            tiklanan_seker.secili = True
    
    def guncelle(self):
        '''
        Oyun durumunu günceller (her frame'de çağrılmalı)
        '''
        # Animasyonları güncelle
        self.animasyonlari_guncelle()
        
        # Animasyon bittiyse otomatik işlemleri yap
        self.otomatik_islem_yap()
    
    def ciz(self, ekran):
        '''
        Oyunu ekrana çizer
        
        Args:
            ekran (pygame.Surface): Çizim yapılacak ekran
        '''
        # Arka plan
        ekran.fill(BEYAZ)
        
        # UI elementlerini çiz
        bilgi_ciz(ekran, self.puan, self.kalan_hamle)
        izgara_ciz(ekran)
        
        # Tüm şekerleri çiz
        for satir in self.izgara:
            for seker in satir:
                if seker is not None:
                    seker.ciz(ekran)
        
        # Oyun bittiyse modal göster
        if self.oyun_bitti:
            modal_ciz(ekran, self.puan)
    
    def sifirla(self):
        '''Oyunu yeniden başlatır'''
        self.__init__()
