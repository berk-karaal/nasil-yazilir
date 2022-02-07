# nasil-yazilir
Adminler tarafından eklenen yazımı karıştırılan kelimleri kullanıcıya sunan basit bir Django Rest Framework çalışması.<br>
[nasil-yazilir.herokuapp.com](https://nasil-yazilir.herokuapp.com)

### Günlük quizler nasıl oluşturuluyor?
Günlük quiz url'ine([daily/](https://nasil-yazilir.herokuapp.com/daily/)) request atıldığında server eğer o günün(request'in atıldığı gün) quizi oluşturulmuşsa onu response'luyor. Eğer o günün quizi oluşturulmamışsa, önceliği hiç gösterilmeyen veya bir quizde kullanımı en eski olan kelimelere vererek yeni bir quiz oluşturup kaydediyor ve o quizi response'luyor.

Eğer bir gün *daily/* ye hiç request olmazsa o günün quizi oluşturulmaz.

(admin sayfasından önceden planlanmış(tarihi ve kelimeleri) quizler oluşturulabilir)

---

# Kullanılabilir method'lar

## [words/](https://nasil-yazilir.herokuapp.com/words/)
**GET** -> Database'deki tüm kelimeleri listeler <br>
**POST** -> Kelime ekle (request.user.is_staff sağlanmalı)

## [daily/](https://nasil-yazilir.herokuapp.com/daily/)
**GET** -> Günlük quizi verir

## [random-quiz/](https://nasil-yazilir.herokuapp.com/random-quiz/)
**GET** -> Database'deki kelimelerden rastgele oluşturulmuş bir quiz verir
