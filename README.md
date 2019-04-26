# Necə istifadə etməli?
    1. Faylları clone edin
    2. hər hansı terminal vasitəsilə folderin içinə daxil olun
    3. docker-compose up komandasını işə salın.
    
    Bu zaman docker-compose faylındakı komandalara uyğun olaraq konteynerlər yaradılmağa başlayacaq
    Bütün proses bitdikdən sonra məlumat avtomatik olaraq bazaya yazılmağa başlayacaq.
    
Hər hansı bir anda python kodlara dəyişiklik etdikdə:
    
    docker-compose down -v 
komandasını işə salın və yaradılmış şəbəkə, konteyner və s. məlumatların 
    hamısını silin.

Daha sonra 

    docker-compose up --build

icra edin.

## Məlumat Bazasına bağlanmaq

docker-compose faylının içində məlumat bazasında bağlanmaq üçün phpmyadmin və adminer konteynerləri də təyin edilmişdir. 
Proses bitdikdən sonra chrome vasitəsilə məlumat bazasına qoşula bilərsiniz. 
    
    Bunun üçün localhost:8080 url-ini ziyarət edin. Bu zaman sizdən istifadəçi adı və şifrə tələb olunacaq.
    
    İstifadəçi adı: root
    Şifrə: password
    
    docker-compose faylında yuxarıdakı məlumatları istədiyinizlə əvəz edə bilərsiniz.