## 定义和用法

filter() 方法创建一个新的数组，新数组中的元素是通过检查指定数组中符合条件的所有元素。

**注意：** filter() 不会对空数组进行检测。

**注意：** filter() 不会改变原始数组。

## 语法
`array.filter(function(currentValue,index,arr), thisValue)

## 参数说明

| 参数                                  | 描述                                                                                                                                                                                                                                                            |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| _function(currentValue, index,arr)_ | 必须。函数，数组中的每个元素都会执行这个函数  <br>函数参数:  <br><br>\| 参数             \| 描述             \|<br>\| -------------- \| -------------- \|<br>\| _currentValue_ \| 必须。当前元素的值      \|<br>\| _index_        \| 可选。当前元素的索引值    \|<br>\| _arr_          \| 可选。当前元素属于的数组对象 \|<br> |
| _thisValue_                         | 可选。对象作为该执行回调时使用，传递给函数，用作 "this" 的值。  <br>如果省略了 thisValue ，"this" 的值为 "undefined"                                                                                                                                                                              |

`
## 示例
返回数组 _ages_ 中所有元素都大于 18 的元素:

```JavaScript
var ages = [32, 33, 16, 40];
function checkAdult(age) { return age >= 18;}
  function myFunction() {    
  document.getElementById("demo").innerHTML = ages.filter(checkAdult);}
```

返回数组 ages 中所有元素都大于输入框指定数值的元素:

```JavaScript
<p>最小年龄: <input type="number" id="ageToCheck" value="18"></p>
  <button onclick="myFunction()">点我</button><p>所有大于指定数组的元素有？ <span id="demo"></span></p><script>var ages = [32, 33, 
  12, 40];function 
  checkAdult(age) {    return age >= 
  document.getElementById("ageToCheck").value;}function myFunction() {    
  document.getElementById("demo").innerHTML = ages.filter(checkAdult);}
  </script>
```

[[小黑的书架]] 