**ID: test\_valid\_item**

**Заголовок:** Создание объявления с валидными данными

**Предусловие:** Создан уникальный seller\_id

**Шаги:**

1\. Отправить POST запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item) с телом: {"sellerID": 111321, "name": "Механическая клавиатура", "price": 1000, "statistics": {"likes": 1, "viewCount": 1, "contacts": 1}}

2\. Получить ответ от сервера

3\. Сохранить полученный id объявления

4\. Отправить GET запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/1/item/:id для проверки созданного объявления по идентификатору

5\. Отправить GET запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/1/:seller\_id/item/ для проверки наличия созданного объявления во всех объявлениях продавца

**Ожидаемый результат:**

В шаге 4 есть результат запроса объявления с такими же данными, как в теле POST (Шаг 1\)

В шаге 5 в объявлениях селлера есть созданное объявление с таким же id

**Постусловие:**

Отправить запрос DELETE на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/2/item/:id

---

**ID: test\_negative\_seller**

**Заголовок:** Создание объявления с отрицательным seller\_id

**Предусловие:** Создан уникальный отрицательный seller\_id

**Шаги:**

Отправить POST запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item) с телом: {"sellerID": \-228, "name": "Монитор Asus", "price": 1000, "statistics": {"likes": 1, "viewCount": 1, "contacts": 1}}

**Ожидаемый результат:**

Объявление не создано, приходит ответ со статусом 400

**Постусловие:**

Отправить запрос DELETE на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/2/item/:id

---

**ID: test\_noname\_item**

**Заголовок:** Создание объявления с пустым name

**Предусловие:** Создан уникальный seller\_id

**Шаги:**

Отправить POST запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item) с телом: {"sellerID": 111321, "name": "", "price": 1000, "statistics": {"likes": 1, "viewCount": 1, "contacts": 1}}

Ожидаемый результат:

Объявление не создано, приходит ответ со статусом 400

**Постусловие:**

Отправить запрос DELETE на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/2/item/:id

---

**ID: test\_negative\_price**

Заголовок: Создание объявления с отрицательным price

Предусловие: Создан уникальный seller\_id

**Шаги:**

Отправить POST запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item) с телом: {"sellerID": 111321, "name": "Монитор Asus", "price": \-1000, "statistics": {"likes": 1, "viewCount": 1, "contacts": 1}}

**Ожидаемый результат:**

Объявление не создано, приходит ответ со статусом 400

**Постусловие:**

Отправить запрос DELETE на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/2/item/:id

---

**ID: test\_zero\_likes**

**Заголовок:** Создание объявления с likes \= 0

**Предусловие:** Создан уникальный seller\_id

**Шаги:**

Отправить POST запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item) с телом: {"sellerID": 111321, "name": "Монитор Zowie", "price": 1000, "statistics": {"likes": 0, "viewCount": 1, "contacts": 1}}

**Ожидаемый результат:**

Объявление не создано, приходит ответ со статусом 400

**Постусловие:**

Отправить запрос DELETE на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/2/item/:id

---

**ID: test\_zero\_views**

**Заголовок:** Создание объявления с viewCount \= 0

**Предусловие:** Создан уникальный seller\_id

**Шаги:**

Отправить POST запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item) с телом: {"sellerID": 111321, "name": "Монитор DEXP", "price": 1000, "statistics": {"likes": 1, "viewCount": 0, "contacts": 1}}

**Ожидаемый результат:**

Объявление не создано, приходит ответ со статусом 400

**Постусловие:**

Отправить запрос DELETE на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/2/item/:id

---

**ID: test\_zero\_contacts**

**Заголовок:** Создание объявления с contacts \= 0

**Предусловие:** Создан уникальный seller\_id

**Шаги:**

Отправить POST запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item) с телом: {"sellerID": 111321, "name": "Монитор LG", "price": 1000, "statistics": {"likes": 1, "viewCount": 1, "contacts": 0}}

**Ожидаемый результат:**

Объявление не создано, приходит ответ со статусом 400

**Постусловие:**

Отправить запрос DELETE на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/2/item/:id

---

**ID: test\_negative\_likes**

**Заголовок:** Создание объявления с likes \< 0

**Предусловие:** Создан уникальный seller\_id

**Шаги:**

Отправить POST запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item) с телом: {"sellerID": 111321, "name": "Монитор ACER", "price": 1000, "statistics": {"likes": \-1, "viewCount": 1, "contacts": 1}}

**Ожидаемый результат:**

Объявление не создано, приходит ответ со статусом 400

**Постусловие:**

Отправить запрос DELETE на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/2/item/:id

---

**ID: test\_negative\_views**

**Заголовок:** Создание объявления с viewCount \< 0

**Предусловие:** Создан уникальный seller\_id

**Шаги:**

Отправить POST запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item) с телом: {"sellerID": 111321, "name": "Монитор Samsung", "price": 1000, "statistics": {"likes": 1, "viewCount": \-1, "contacts": 1}}

**Ожидаемый результат:**

Объявление не создано, приходит ответ со статусом 400

**Постусловие:**

Отправить запрос DELETE на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/2/item/:id

---

**ID: test\_negative\_contacts**

**Заголовок:** Создание объявления с contacts \< 0

**Предусловие:** Создан уникальный seller\_id

**Шаги:**

Отправить POST запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item) с телом: {"sellerID": 111321, "name": "Монитор Sony", "price": 1000, "statistics": {"likes": 1, "viewCount": 1, "contacts": \-1}}

**Ожидаемый результат:**

Объявление не создано, приходит ответ со статусом 400

**Постусловие:**

Отправить запрос DELETE на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/2/item/:id

---

**ID: test\_get\_item**

**Заголовок:** Получение объявления по идентификатору

**Предусловие:** Создан уникальный seller\_id и создано валидное объявление с хешем(id)

**Шаги:**

1. Отправить GET запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/1/item/:id  
2. Получить ответ от сервера

**Ожидаемый результат:**

В ответе от сервера с объявлением должны совпадать данные из тела созданного объявления (хеш(id), sellerID, name, price, likes, viewCount, contacts)

---

**ID: test\_get\_notexist\_item**

**Заголовок:** Получение невалидного объявления по идентификатору

**Предусловие:** Наличие хеша невалидного(несозданного) объявления. Например, abc

**Шаги:**

1. Отправить GET запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/1/item/abc  
2. Получить ответ от сервера

**Ожидаемый результат:**

Информации по объявлению нет, приходит ответ со статусом 400

---

**ID: test\_delete\_notexist\_item**

**Заголовок:** Удаление несуществующего объявления

**Предусловие:** Наличие хеша несуществующего объявления. Например, abc

**Шаги:**

1. Отправить DELETE запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/2/item/abc  
2. Получить ответ от сервера

**Ожидаемый результат:**

Объявление не удаляется, приходит ответ со статусом 400

---

**ID: test\_delete\_item**

**Заголовок:** Удаление существующего объявления

**Предусловие:** Создан хеш(id) и уникальный seller\_id (Например, 111321\)

**Шаги:**

1. Отправить DELETE запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/2/item/:id  
2. Получить ответ от сервера  
3. Отправить GET запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/1/item/:id  
4. Получить ответ от сервера  
5. Отправить GET запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/1/111321/item  
6. Получить ответ от сервера

**Ожидаемый результат:**

1\. На шаге 1 объявление успешно удалено, приходит ответ со статусом 200

2\. На шаге 3 объявление не находится по хешу(id), приходит ответ со статусом 404

3\. На шаге 5 нет объявления с созданным хешем(id) во всех объявлениях селлера.

---

**ID: test\_statistics**

**Заголовок:** Получение статистики валидного объявления

**Предусловие:** Создан хеш(id) и уникальный seller\_id (Например, 111321\)

**Шаги:**

1. Отправить GET запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/1/statistic/:id  
2. Получить ответ от сервера  
3. Отправить GET запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/2/statistic/:id  
4. Получить ответ от сервера

**Ожидаемый результат:**

В шагах 1 и 3 в ответе от сервера со статистикой объявления должны совпадать данные из тела созданного объявления (likes, viewCount, contacts)

---

**ID: test\_notexist\_statistics**

**Заголовок:** Получение статистики несуществующего объявления

**Предусловие**: Наличие несуществующего хеша(id) объявления. Например, abc

**Шаги:**

1. Отправить GET запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/1/statistic/:id  
2. Получить ответ от сервера  
3. Отправить GET запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/2/statistic/:id  
4. Получить ответ от сервера

**Ожидаемый результат:**

В шагах 1 и 3 приходит ответ от сервера со статусом 400, статистики нет.

---

**ID: test\_deleted\_item\_statistics**

**Заголовок:** Получение статистики удалённого объявления

**Предусловие:** Создан хеш(id) и уникальный seller\_id (Например, 111321\)

**Шаги:**

1. Отправить DELETE запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/2/item/:id  
2. Получить ответ от сервера  
3. Отправить GET запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/1/statistic/:id  
4. Получить ответ от сервера  
5. Отправить GET запрос на [https://qa-internship.avito.com/api/1/item](https://qa-internship.avito.com/api/1/item)/api/2/statistic/:id  
6. Получить ответ от сервера

**Ожидаемый результат:**

1. На шаге 1 объявление удалено

      2\. На шаге 3 и 5 приходит ответ от сервера со статистикой объявления, совпадающий с данными из тела созданного объявления (likes, viewCount, contacts)  
