# SubdomainFinder (EN)

## Overview

**SubdomainFinder** is a subdomain scanner designed to find and log subdomains of a target domain. It leverages multi-threading to speed up the scanning process and ensures graceful handling of interruptions.

## Features

- **Concurrent Requests**: Utilizes `ThreadPoolExecutor` to perform multiple requests simultaneously, enhancing the efficiency of the scanning process.
- **Graceful Shutdown**: Handles `Ctrl+C` interrupts to stop scanning and shut down resources cleanly.
- **Logging**: Saves discovered subdomains to a file (`found_subdomains.txt`) and prevents re-checking of already discovered subdomains.
- **Error Handling**: Suppresses error messages and manages exceptions during execution.

## How It Works

1. **Load Existing Subdomains**:
   - Reads the `found_subdomains.txt` file to retrieve any previously discovered subdomains.
   - If the file is absent, it initializes with an empty set.

2. **Subdomain Checking**:
   - Iterates through a list of subdomains (from `subDomainlist.txt`), constructs the full URL, and checks its availability.
   - If a subdomain resolves successfully, it is printed and added to `found_subdomains.txt`.

3. **Handling Interrupts**:
   - Uses signal handling to detect `Ctrl+C` interrupts, setting a shutdown event to notify threads to stop.
   - Waits for all threads to complete before exiting the program.

4. **Resource Cleanup**:
   - Ensures that the `ThreadPoolExecutor` is properly shut down and resources are released.
   - Provides feedback to the user indicating the completion of the subdomain scan and that the program has closed.

## Configuration

1. **Setup**:
   - Ensure Python is installed on your system.
   - Install the required libraries using: `pip install requests`.

2. **Configuration**:
   - **Target Domain**: Edit the `target_url` variable in the `subDomainFinder.py` script to specify the domain you want to scan. For example, set `target_url = "example.com"`.

   - **Subdomain List**: Update the `wordlist_file` variable with the path to your subdomain list file. By default, it is set to `"subDomainlist.txt"`. Ensure this file contains potential subdomains to test, one per line.

3. **Running the Script**:
   - Execute the script using the command: `python subDomainFinder.py`.
   - If needed, you can interrupt the scan by pressing `Ctrl+C`. The script will handle the shutdown process and exit gracefully.

### Example

```bash
python subDomainFinder.py
```

**Note**: The script will create and update `found_subdomains.txt` with each discovered subdomain. Make sure you have the necessary write permissions for this file.


---

---

# SubdomainFinder (TR)

## Genel Bakış

**SubdomainFinder**, hedef bir alan adının alt alanlarını bulmak ve kaydetmek için tasarlanmış bir alt alan tarayıcıdır. Tarama sürecini hızlandırmak için çoklu iş parçacığı kullanır ve kesintileri düzgün bir şekilde yönetir.

## Özellikler

- **Eşzamanlı İstekler**: `ThreadPoolExecutor` kullanarak birden fazla isteği aynı anda gerçekleştirir, böylece tarama sürecinin verimliliğini artırır.
- **Düzgün Kapanma**: `Ctrl+C` kesintilerini yönetir, taramayı durdurur ve kaynakları düzgün bir şekilde kapatır.
- **Kaydetme**: Bulunan alt alanları `found_subdomains.txt` dosyasına kaydeder ve daha önce keşfedilmiş alt alanları yeniden kontrol etmez.
- **Hata Yönetimi**: Hata mesajlarını bastırır ve yürütme sırasında oluşan istisnaları yönetir.

## Nasıl Çalışır

1. **Mevcut Alt Alanları Yükleme**:
   - `found_subdomains.txt` dosyasını okuyarak daha önce keşfedilmiş alt alanları alır.
   - Dosya yoksa, boş bir küme ile başlar.

2. **Alt Alan Kontrolü**:
   - `subDomainlist.txt` dosyasındaki alt alan listesini iteratif olarak kontrol eder, tam URL'yi oluşturur ve kullanılabilirliğini kontrol eder.
   - Bir alt alan başarılı bir şekilde yanıt alırsa, ekrana yazdırılır ve `found_subdomains.txt` dosyasına eklenir.

3. **Kesintileri Yönetme**:
   - `Ctrl+C` kesintilerini algılamak için sinyal işleme kullanır, iş parçacıklarını durdurmak için bir kapanma olayı ayarlar.
   - Tüm iş parçacıklarının tamamlanmasını bekler ve ardından programdan çıkar.

4. **Kaynak Temizleme**:
   - `ThreadPoolExecutor`'ın düzgün bir şekilde kapatıldığından ve kaynakların serbest bırakıldığından emin olur.
   - Alt alan taramasının tamamlandığını ve programın kapandığını kullanıcıya belirten geri bildirim sağlar.

## Konfigürasyon

1. **Kurulum**:
   - Sisteminizde Python'un kurulu olduğundan emin olun.
   - Gerekli kütüphaneleri yüklemek için: `pip install requests` komutunu kullanın.

2. **Konfigürasyon**:
   - **Hedef Alan Adı**: `subDomainFinder.py` scriptindeki `target_url` değişkenini taramak istediğiniz alan adı ile belirtin. Örneğin, `target_url = "example.com"` olarak ayarlayın.

   - **Alt Alan Listesi**: `wordlist_file` değişkenini alt alan listesi dosyanızın yolu ile güncelleyin. Varsayılan olarak `"subDomainlist.txt"` olarak ayarlanmıştır. Bu dosyanın her bir satırında test edilecek potansiyel alt alanlar bulunmalıdır.

3. **Scripti Çalıştırma**:
   - Scripti şu komutla çalıştırın: `python subDomainFinder.py`.
   - Tarama işlemini kesmek isterseniz, `Ctrl+C` tuşlarına basabilirsiniz. Script, kapanma işlemini yönetir ve düzgün bir şekilde kapanır.

### Örnek

```bash
python subDomainFinder.py
```

**Not**: Script, her bulunan alt alanı `found_subdomains.txt` dosyasına ekler ve günceller. Bu dosyaya yazma izinlerinizin olduğundan emin olun.

---

