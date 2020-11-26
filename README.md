# Recursive image minification

This script is util to minify multiple images files inside multiple folders

#### How to install dependencies

`pip install -r requerements.txt`

#### How to use

Set quality var:

`quality=30`

and 

`images_destination='compressed'`

Then execute

###### Input Folder structure example:

```
images/
+-- nature.png
+-- trees/
    +-- Sauce.jpg
    +-- Fresno.jpg
+-- flowers/
    +-- roses/
        +-- Climbing Roses.jpg
        +-- English Roses.pjg  
    +-- dahlias/
        +-- Mignon Dahlias.jpg
        +-- Pompon Dahlias.jpg
        +-- ...
    
```

###### Output Folder structure example:

```
Compressed/
+-- nature.png
+-- trees/
    +-- Sauce.jpg
    +-- Fresno.jpg
+-- flowers/
    +-- roses/
        +-- Climbing Roses.jpg
        +-- English Roses.pjg  
    +-- dahlias/
        +-- Mignon Dahlias.jpg
        +-- Pompon Dahlias.jpg
        +-- ...
    
```
