### activate

```
source /path/to/mine-environments/bin/activate
```

<hr>

### 将返回一个包含 site-packages 目录路径的列表。通常第一个路径是默认的 site-packages 目录

```
y=$(python3 -c "import site; site_paths = site.getsitepackages(); print(site_paths[0])");
echo $y;
mv *.pth $y;
```

<hr>

### verified

```
python3 -c "import sys; print(sys.path)"
```

<hr>
