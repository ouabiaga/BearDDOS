
# 🐻 Bear DDoS - High-Performance Stress Testing Tool

Bear DDoS is a professional, hybrid network load and stress-testing utility written in Python. It features both a traditional multi-threaded execution layout and a modern asynchronous I/O request engine to accurately measure target server performance and WAF boundaries.

## ✨ Key Features
- **Hybrid Performance Architecture:** Choose between Threaded (Sync) and Non-blocking Async execution formats.
- **WAF-Aware Intelligence:** Automatically detects security firewall triggers, handles `429 Too Many Requests` by slowing down, and terminates on `403 Forbidden` WAF blockades gracefully.
- **Identity Masking:** Dynamic generation of `X-Forwarded-For` and `X-Real-IP` spoofing combined with random real-world browser `User-Agents`.
- **Live Performance Dashboard:** Real-time console metrics tracking packet delivery, 200 OK successes, WAF drops, and connectivity errors.

## 🚀 Installation & Requirements

Ensure you have Python 3.10+ installed on your system.

```bash
# Clone the repository
git clone  https://github.com/ouabiaga/BearDDOS.git
cd BearDDOS

# Install dependencies
pip install -r requirements.txt
```

### Create `requirements.txt`
Make sure to create a `requirements.txt` file in your repository containing:
```text
requests
colorama
aiohttp
```

## 💻 Usage & Parameters

```bash
python BearDDOS.py --url <TARGET_URL> --method <A/S> -T <THREADS/TASKS> [--random-user]
```

### Examples
* **Standard Synchronous Benchmarking:**
  ```bash
  python BearDDOS.py --url http://127.0.0.1:8080 --method S -T 20
  ```
* **Advanced Obfuscated Asynchronous Ingestion (Recommended):**
  ```bash
  python BearDDOS.py --url http://127.0.0.1:8080 --method A -T 100 --random-user
  ```

## ⚖️ Legal Disclaimer
This tool is intended strictly for authorized security auditing, educational purposes, and infrastructure stress-testing. Performing Distributed Denial of Service (DDoS) attacks against unauthorized targets is strictly illegal. The developer assumes no liability for misuse or damage caused by this software.
