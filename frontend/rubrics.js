const domain = 'http://localhost:8000/api/';

const list = document.querySelector('#list');
const itemId = document.querySelector('#id');
const itemName = document.querySelector('#name');

async function loadItem(evt) {
    evt.preventDefault();
    const result = await fetch(evt.target.href);
    if (result.ok) {
        const data = await result.json();
        itemId.value = data.id;
        itemName.value = data.name;
    } else {
        console.log(result.statusText);
    }
}

async function loadList() {
    const result = await fetch(`${domain}rubrics`);

    if(result.ok) {
        const data = await result.json();
        let s = '<ul>', d;
        for (let i = 0; i < data.length; i++) {
            d = data[i];
            s += `<li>${d.name}
                      <a href="${domain}rubrics/${d.id}/" class="detail">Вывести</a>
                  </li>`
        }
        s += '</ul>';

        list.innerHTML = s;
        let links = list.querySelectorAll('ul li a.detail');

        links.forEach((link) => {
            link.addEventListener('click', loadItem);
        });
    } else {
        console.log(result.statusText);
    }
}

loadList();
