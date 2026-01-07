# **Bugs**

### **Bug-1**

**Заголовок:** 

Создается объявление с отрицательным seller\_id

**Шаги:**

Отправить POST запрос на https://qa-internship.avito.com/api/1/item с телом: {"sellerID": -228, "name": "Монитор Asus", "price": 1000, "statistics": {"likes": 1, "viewCount": 1, "contacts": 1}}

**ОР:**

Объявление не создано, при создании айтема в ручке https://qa-internship.avito.com/api/1/item приходит ответ с ошибкой 400, в ручке https://qa-internship.avito.com/api/1/-228/item нет созданного айтема у селлера

**ФР:**

Объявление создано, при создании айтема в ручке https://qa-internship.avito.com/api/1/item приходит ответ с id объявления, в ручке https://qa-internship.avito.com/api/1/-228/item айтем появляется у селлера

**Приоритет:** 

HIGH

---

### **Bug-2**

**Заголовок:** 

Создается объявление с likes \< 0

**Шаги:**

Отправить POST запрос на https://qa-internship.avito.com/api/1/item с телом: {"sellerID": 111321, "name": "Монитор ACER", "price": 1000, "statistics": {"likes": -1, "viewCount": 1, "contacts": 1}}  

**ОР:**

Объявление не создано, при создании айтема в ручке https://qa-internship.avito.com/api/1/item приходит ответ с ошибкой 400, в ручке https://qa-internship.avito.com/api/1/111321/item нет созданного айтема у селлера 

**ФР:**

Объявление создано, при создании айтема в ручке https://qa-internship.avito.com/api/1/item приходит ответ с id объявления, в ручке https://qa-internship.avito.com/api/1/111321/item айтем появляется у селлера

**Приоритет:** 

HIGH

### **Bug-3**

**Заголовок:** 

Создается объявление с viewCount \< 0

**Шаги:**

Отправить POST запрос на https://qa-internship.avito.com/api/1/item с телом: {"sellerID": 111321, "name": "Монитор ACER", "price": 1000, "statistics": {"likes": 1, "viewCount": -1, "contacts": 1}}

**ОР:**

Объявление не создано, при создании айтема в ручке https://qa-internship.avito.com/api/1/item приходит ответ с ошибкой 400, в ручке https://qa-internship.avito.com/api/1/111321/item нет созданного айтема у селлера 

**ФР:**

Объявление создано, при создании айтема в ручке https://qa-internship.avito.com/api/1/item приходит ответ с id объявления, в ручке https://qa-internship.avito.com/api/1/111321/item айтем появляется у селлера

**Приоритет:** 

HIGH

### **Bug-4**

**Заголовок:** 

Создается объявление с contacts \< 0

**Шаги:**

Отправить POST запрос на https://qa-internship.avito.com/api/1/item с телом: {"sellerID": 111321, "name": "Монитор ACER", "price": 1000, "statistics": {"likes": 1, "viewCount": 1, "contacts": -1}}

**ОР:**

Объявление не создано, при создании айтема в ручке https://qa-internship.avito.com/api/1/item приходит ответ с ошибкой 400, в ручке https://qa-internship.avito.com/api/1/111321/item нет созданного айтема у селлера 

**ФР:**

Объявление создано, при создании айтема в ручке https://qa-internship.avito.com/api/1/item приходит ответ с id объявления, в ручке https://qa-internship.avito.com/api/1/111321/item айтем появляется у селлера

**Приоритет:** 

HIGH

