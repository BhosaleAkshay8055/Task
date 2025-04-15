## First clone this repo and then create virtual env

command:
'''
python -m venv myenv

cd myenv/Scripts

./activate    
```

# required permission then run below command

```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

``` 
and then
```
./activate
```



Then back to the main directory cd .. (2 times windows pc)

Then install dependencies
```
pip install -r requirements.txt
```

create database like: DATABASE_URL = "postgresql://postgres:odoo@localhost:5432/vibeosysDb"

Then excute below command for start application
```

uvicorn main:app --reload

```


