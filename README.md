### Observations:
1. **Repository Content**:
   - The repository contains a Python script for finding subdomains.
   - The code includes functionality for dynamic input of the target domain and custom subdomain list files.

2. **README Status**:
   - The repository currently does not have a README file or it might be minimal.

### Suggested README Content

#### English

```markdown
# SubdomainFinder

SubdomainFinder is a Python script designed to discover subdomains of a target domain using a list of potential subdomains. It supports both default and custom subdomain list files and handles interruptions gracefully.

## Features
- **Dynamic Target Domain**: Allows you to input the domain you want to scan.
- **Custom Subdomain List**: Specify a custom subdomain list file or use the default (`subdomainlist.txt`).
- **Graceful Shutdown**: Handles Ctrl+C interruptions and exits gracefully.

## Requirements
- Python 3.x
- `requests` library

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Onurbykall/SubdomainFinder.git
   ```

2. **Navigate to the Directory:**
   ```bash
   cd SubdomainFinder
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Script:**
   ```bash
   python subdomain_finder.py
   ```

5. **Follow the Prompts:**
   - Enter the target domain (e.g., `example.com`).
   - Provide the path to your subdomain list file or press Enter to use the default (`subdomainlist.txt`).

## Example
```bash
python subdomain_finder.py
Enter the target domain (e.g., example.com): example.com
Enter the path to the subdomain list file (default: subdomainlist.txt): custom_subdomains.txt
```



```

#### Turkish

```markdown
# Alt Alan Adı Bulucu

Alt Alan Adı Bulucu, bir hedef alan adının alt alan adlarını bulmak için tasarlanmış bir Python scriptidir. Potansiyel alt alan adları listesini kullanarak tarama yapar ve varsayılan veya özel alt alan adı listesi dosyalarını destekler.

## Özellikler
- **Dinamik Hedef Alan Adı**: Tarayacağınız alan adını girmenizi sağlar.
- **Özelleştirilebilir Alt Alan Adı Listesi**: Kendi alt alan adı listesi dosyanızı belirtin veya varsayılan (`subdomainlist.txt`) dosyayı kullanın.
- **Nazik Kapanış**: Ctrl+C kesintilerini nazikçe yönetir ve çıkış yapar.

## Gereksinimler
- Python 3.x
- `requests` kütüphanesi

## Kullanım

1. **Depoyu Klonlayın:**
   ```bash
   git clone https://github.com/Onurbykall/SubdomainFinder.git
   ```

2. **Dizine Geçin:**
   ```bash
   cd SubdomainFinder
   ```

3. **Bağımlılıkları Kurun:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Scripti Çalıştırın:**
   ```bash
   python subdomain_finder.py
   ```

5. **İstediğiniz Bilgileri Girin:**
   - Hedef alan adını girin (örneğin, `example.com`).
   - Alt alan adı listesi dosyasının yolunu belirtin veya varsayılan (`subdomainlist.txt`) dosyayı kullanmak için Enter tuşuna basın.

## Örnek
```bash
python subdomain_finder.py
Enter the target domain (e.g., example.com): example.com
Enter the path to the subdomain list file (default: subdomainlist.txt): custom_subdomains.txt
```


## Katkıda Bulunma
Bu projeyi geliştirmek için sorunlar bildirebilir veya pull request gönderebilirsiniz.

```
