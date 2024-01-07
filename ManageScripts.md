### activate

```
source /path/to/mine-environments/bin/activate
```

<hr>

### 将返回一个包含 site-packages 目录路径的列表。通常第一个路径是默认的 site-packages 目录

```
python3 -c "import site; print(site.getsitepackages())"
```

<hr>

### verified

```
python3 -c "import sys; print(sys.path)"
```

<hr>
