Dataset.py dosyası, yüz tanıma sistemi için veri toplama ve bu verileri uygun formatta kaydetme amacı taşır. Kullanıcının yüz verilerini toplayarak, bu verileri eğitim ve tanıma işlemlerinde kullanılmak üzere serileştirir ve dosyaya kaydeder.
![image](https://github.com/tubaagurbuz/Face-recognition/assets/72495697/a64cd674-88cd-4532-9a58-0770fbedee3a)

Görüntülerdeki yüzleri algılamak için OpenCV'nin Haar Cascade sınıflandırıcısı kullanılır.
![image](https://github.com/tubaagurbuz/Face-recognition/assets/72495697/144452dd-fc68-483a-ba51-f3fccbba0c87)
![image](https://github.com/tubaagurbuz/Face-recognition/assets/72495697/0aa8cceb-d22f-4ccd-8a8a-0ef6fe634d4a)   Bu kod satırı, OpenCV kütüphanesi kullanılarak yüz algılama modelini yükler ve bir yüz algılayıcı (face detector) oluşturur. Eğitilmiş bir model (XML dosyası) kullanılarak, görüntülerde nesne tespiti yapılır.
![image](https://github.com/tubaagurbuz/Face-recognition/assets/72495697/9ffc8499-997c-4932-897a-c9921411aab6)


Attendance.py dosyası, yüz tanıma kullanarak otomatik katılım (attendance) takibi yapar. Eğitimli bir model kullanarak, kameradan alınan görüntülerdeki yüzleri tanır ve tanınan kişilerin katılım bilgilerini kaydeder.
![Uploading image.png…]()

