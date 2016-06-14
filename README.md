# grouper
index.html
```html
<!DOCTYPE html>
<html>
  <head>
    %(head)s
  </head>
  <script type="text/javascript">
    %(init)s
    %(main)s
  </script>
</html>
```
grouper.json
```json
{
  "head": ["head.html"],
  "init": ["constants.js", "config.js"],
  "main": ["main.js"],
  
  "outputs":
  {
    "index.html": "build/index.html"
  }
}
```
grouping:
```bash
cd ./project_path
grouper
```
A single file named "build/index.html" will be created with the content of these 4 files
