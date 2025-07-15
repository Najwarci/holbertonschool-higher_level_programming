## 📘 JavaScript DOM Manipulation

The **DOM (Document Object Model)** is an interface that allows JavaScript to access and dynamically manipulate the structure of an HTML document.

### 🔍 Selecting Elements

```javascript
// By ID
document.getElementById('my-id');

// By class name
document.getElementsByClassName('my-class');

// By tag name
document.getElementsByTagName('div');

// By CSS selector
document.querySelector('.my-class');        // First matching element
document.querySelectorAll('ul li');         // All matching elements
