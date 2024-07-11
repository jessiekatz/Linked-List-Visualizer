async function addNode() {
    const value = document.getElementById('nodeValue').value;
    if (value !== '') {
        await fetch(`/api/linkedlist/add?value=${value}`, { method: 'POST' })
            .then(response => response.json())
            .then(data => displayList(data));
    }
    // let divse = document.getElementById('linkedListContainer')
    // let nodeDiv = createElement("div")
    // nodeDiv.textContent = value
    // divse.appendChild(nodeDiv)
}

async function removeNode() {
    const value = document.getElementById('nodeValue').value;
    if (value !== '') {
        await fetch(`/api/linkedlist/remove?value=${value}`, { method: 'POST' })
            .then(response => response.json())
            .then(data => displayList(data));
    }
}

async function reverseList() {
    await fetch(`/api/linkedlist/reverse`, { method: 'POST' })
        .then(response => response.json())
        .then(data => displayList(data));
}

async function displayList(data) {
    const linkedListContainer = document.getElementById('linkedListContainer');
    linkedListContainer.innerHTML = '';

    data.forEach(nodeValue => {
        const nodeElement = document.createElement('div');
        nodeElement.textContent = nodeValue;
        linkedListContainer.appendChild(nodeElement);
    });
}

async function printList() {
    await fetch(`/api/linkedlist/print`)
        .then(response => response.json())
        .then(data => displayList(data));
}

document.addEventListener('DOMContentLoaded', printList);
