# Necə istifadə etməli?
    1. Faylları clone edin
    2. hər hansı terminal vasitəsilə folderin içinə daxil olun
    3. docker-compose up --build komandasını işə salın.
    
    Bu zaman docker-compose faylındakı komandalara uyğun olaraq konteynerlər yaradılmağa başlayacaq.

docker-compose komandası konteynerləri eyni anda yaratmağa başladığı üçün birinci dəfə tapaz konteyneri
işə düşməyəcək. Çünki, konteynerin, yəni skriptin normal işləməsi üçün mysql məlumat bazası tam işlək vəziyyətdə olmalıdır, ancaq mysql-in işə düşməsi gecikdiyi üçün tapaz konteyneri ondan əvvəl yaranır. Bu zaman xəta əmələ gəlir. Bunun üçün bütün proses yekunlaşdıqdan sonra aşağıdakı komandanı işə salmaq lazımdır:

    docker container start tapaz

Beləliklə konteyner işə düşəcək və məlumatlar toplanaraq məlumat bazasına yazılacaq. Yuxarıda qeyd olunan problem mysql-in docker səhifəsində qeyd edilmişdir. hub.docker.com saytına daxil olun, axtarış yerinə mysql yazın və bu barədə daha ətraflı oxuyun.
    
Hər hansı bir anda python kodlara dəyişiklik etdikdə:
    
    docker-compose down -v 
komandasını işə salın və yaradılmış şəbəkə, konteyner və s. məlumatların 
    hamısını silin. 
    
QEYD: mysql_data_folder MySQL bazasına aid məlumatları özündə saxlayır və -v həmin folderə toxunmur, beləliklə hər dəfə yeni docker-compose up --build komandasını işlətdikdə sizin məlumatlar öz yerində qalır.
docker-compose faylında həmin sətir deaktivdir, aktivləşdirərək yuxarıda qeyd olunan asanlıqdan yararlana bilərsiniz.

Daha sonra 

    docker-compose up --build

icra edin.

## Məlumat Bazasına bağlanmaq

docker-compose faylının içində məlumat bazasında bağlanmaq üçün phpmyadmin konteyneri də təyin edilmişdir. 
Proses bitdikdən sonra chrome vasitəsilə məlumat bazasına qoşula bilərsiniz. 
    
    Bunun üçün localhost:8080 url-ini ziyarət edin. Bu zaman sizdən istifadəçi adı və şifrə tələb olunacaq.
    
    İstifadəçi adı: root
    Şifrə: password
    
    docker-compose faylında yuxarıdakı məlumatları istədiyinizlə əvəz edə bilərsiniz.