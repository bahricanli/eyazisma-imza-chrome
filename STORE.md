# Mağaza yayını

Ad: e-Yazışma İmza
Yayıncı: BahriCanli
Kısa açıklama: Dernek portalındaki elektronik imza işlemini yerel kart uygulamasına bağlar.
Kategori: Productivity / İş araçları

## Açıklama

LKD ve PKD portallarında elektronik imzalama ekranını tek tıklamayla açın.
Bilgisayarınıza kurulu e-Yazışma İmza uygulamasıyla bağlantı kurar; kart ve
sertifika kontrol ekranını da eklenti menüsünden açabilirsiniz.

Yerel imza uygulaması ve kartınıza uygun sürücü ayrıca kurulmalıdır. Eklenti tek
başına USB karta erişmez. PIN ve imza onayı yalnızca yerel uygulamada alınır.

## İzin gerekçeleri

nativeMessaging: kurulu yerel uygulamanın durumunu kontrol etmek ve imza/kart
ekranını açmak. İçerik betikleri: yalnız iki portalın yazışma sayfalarındaki
imzalama düğmelerini bağlamak. Başka sitelere erişilmez.

## İnceleyici notları

Yerel uygulama kaynağı: https://github.com/bahricanli/eyazisma-imza
En az sürüm: v0.2.9. Kalıcı klasöre kurup --install-browser-host çalıştırın.
Chrome mağazasının atadığı kimliği --chrome-extension-id ile kaydedin.
Eklenti menüsündeki kart kontrolü portal hesabı olmadan denenebilir. Gerçek
imza için portal hesabı ve fiziksel e-imza kartı gerekir; test erişimi için
kullanıcı/publisher ile iletişime geçilmelidir. Gerçek PIN veya kişisel hesap
mağaza metnine eklenmemelidir.

ZIP: npm run build. Gizlilik: PRIVACY.md. Kaynaklar minify edilmez.
Yayıncı hesabı ve mağaza ekran görüntüleri tamamlandı.

Gizlilik sayfası: https://bahricanli.github.io/eyazisma-imza-chrome/
Destek: https://github.com/bahricanli/eyazisma-imza-chrome/issues

## Mağaza başvurusu

Chrome mağaza kimliği: `pgengianfoeihehebpjilcckgpadgohk`.
Mağaza paketinden geliştirmeye özel `key` alanı çıkarılır. Geliştirme kimliği
mağaza kimliğinden farklıdır; yerel uygulamada mağaza kimliğini kullanın:

```sh
eyazisma-imza --install-browser-host --chrome-extension-id pgengianfoeihehebpjilcckgpadgohk
```

28 Ekim 2026: 0.1.2 paketi Chrome mağazasına yüklendi. Açıklama, Türkçe dil,
Araçlar kategorisi, simge, ekran görüntüsü, izin/veri kullanım beyanları ve
gizlilik URL'si kaydedildi. Yayıncı adı BahriCanli. Yayıncı iletişim e-postası doğrulandı; 0.1.2 sürümü incelemeye gönderildi.

Yerel imza bağlantısı dışında veri toplanmaz; Chrome beyanında yerelde işlenen
geçici kimlik doğrulama bağlantısı, ilgili portal sayfa yolu ve bağlantı içeriği
şeffaf biçimde işaretlendi. PIN/özel anahtar/PDF eklentiden geçmez.

Son durum: 28 Ekim 2026 — İncelenmeyi bekliyor. Onaydan sonra otomatik yayın seçildi.
