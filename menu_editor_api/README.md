#  Menu Editor App API

This is an menu editing API made with Python Flask. 


## Getting Started

### 1. Download file
In order to have the API working, you need to have to download or clone the repository. 

### 2. Install Dependencies
Once you unzipped the file on your local machine, go to its directory and install dependencies by running:

macOS and Linux:
```
pip3 install -r requirements.txt
```

Windows:
```
python3 -m pip install -r requirements.txt
```

### 3. Run app
```
python3 run.py
```
### 3. Test API

#### In browser, try:

I. Create entity:

http://127.0.0.1:5000/api/menu/create?entity=item&name='foodname'&description='fooddescription'&price='price'

II. Get menu or an entity:

http://127.0.0.1:5000/api/menu/

http://127.0.0.1:5000/api/menu/get?entity=item

http://127.0.0.1:5000/api/menu/get/1?entity=item

III. Update entity:

http://127.0.0.1:5000/api/menu/update/2?entity=item_modifiers&item_id=1&modifier_id=2


IV. Delete entity:

http://127.0.0.1:5000/api/menu/delete/1?entity=section
 
