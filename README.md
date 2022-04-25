# proxy-rotation
Multithreaded implementation of proxy rotation for different projects in Python 3.9

Use:

<b>First, buy a key on the site best-proxies.ru and paste it into the required field in the rotation.py file</b>

```python
  import rotation as rt

  proxy = rt.find_work_proxy()
  proxies = {
    'http': f'socks5://{proxy}'
    'https': f'socks5://{proxy}'
  }
```
