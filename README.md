## My Website Automated Testing with Selenium!
實做兩種架構的自動化測試

### 第一部分：  
使用Selenium + python內建的unittest模組，做單元測試架構的自動化測試  
>檔案架構  
>searchTestUnitTest.py  

測試執行指令  
```javascript
  python searchTestUnitTest.py
```

### 第二部分：  
使用Selenium + pytest模組，做單元測試架構的自動化測試 
>檔案架構  
>searchTestPytest.py  

測試執行指令  
```javascript
  pytest searchTestPyTest.py -v
```

### 第三部分：  
使用Selenium + behave模組，做BDD架構的自動化測試  
>檔案架構  
>features/  
>features/searchTestBDD.feature  
>features/environment.py  
>features/steps/  
>features/steps/searchTestBDD.py  

測試執行指令  
```javascript
  behave -v
```