let arrayBtns = document.querySelectorAll(".delete-good")

for (let btn of arrayBtns) {
    let id = btn.dataset.id
    btn.addEventListener("click", () => {
        fetch("/deleteGoods",{
          method: "POST",
          headers: {
              "Content-Type": "application/json",
              // 'Content-Type": 'application/x-www-from-urlencodded',
          },
          body:JSON.stringify(id)
        })
    })
}