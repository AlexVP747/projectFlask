// Получаем массив кнопок
let arrayBtns = document.querySelectorAll(".delete-good")
// для каждой кнопки назначаем событие
// При клике на кнопку я буду делать ассинхронный запрос
for (let btn of arrayBtns) {
    // получаю id товара, которые записан в кнопке с помощью пользовательского атрибута
    let id = btn.dataset.id

    // добавляем кнопки прослушку события клика на мышь
    btn.addEventListener("click", async () => {
        // async - говорит о том, что функция будет работать с ассинхронным кодом
        // await - ждет пока выполнится запрос и запишет его в переменную
        // await не будет работать, если у функции нет слова async
        let response = await fetch("/deleteGoods",{
          method: "POST",

          // Устанавливаем в заголовках, то что наш запрос будет работать в формате JSON
          headers: {
              "Content-Type": "application/json",
              // 'Content-Type": 'application/x-www-from-urlencodded',
          },
          // передаем серверу id приведенный к формату json
          body:JSON.stringify(id)
        })

        // полученный ответ конвертирую из JSON в JavaScript массив
        let listGoods = await response.json()

        // Получаем div элемент, где хранится список товаров
        let container = document.querySelector("#list-goods")
        // Очищаю свой div
        container.innerHTML = ""
        console.log(listGoods)
        for (let good of listGoods){
            // создаю тег p спомощью JS
            let p = document.createElement("p")
            p.innerHTML = `Id: ${ good[0] }; Название: ${ good[1] }; Цена: ${ good[2] }`

            let button = document.createElement("button")
            button.innerHTML = "Удалить запись" // Добавляем что будет написано на кнопке
            button.classList.add("delete-good") // добавляю кнопке класс
            button.dataset.id = product[0] // добаввляем пользовательский атрибут с id

            container.append(p)
            container.append(button)

        }
        

    })
}