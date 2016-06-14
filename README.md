## grouper example
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

## installing in linux
to use group in your project just enter in the folder and run the script

to install grouper just link the main script to a folder in your path
```bash
ln -s /path/to/grouper/grouper.py /usr/bin
```

## template files

## grouper.json
grouper is a json file. it is composed by keys of dictionary poiting to a list of files and a "outputs" key taking the template files:
