document.getElementById('collectionForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Collect form data
    const route = document.getElementById('route').value;
    const date = document.getElementById('date').value;
    const time = document.getElementById('time').value;
    const performance = parseFloat(document.getElementById('performance').value);

    // Add new row to the table
    const table = document.getElementById('collectionTable').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();
    newRow.insertCell(0).innerText = route;
    newRow.insertCell(1).innerText = date;
    newRow.insertCell(2).innerText = time;
    newRow.insertCell(3).innerText = performance.toFixed(2);

    // Update total waste collected
    const totalCollectedElement = document.getElementById('totalCollected');
    let totalCollected = parseFloat(totalCollectedElement.innerText);
    totalCollected += performance;
    totalCollectedElement.innerText = totalCollected.toFixed(2);

    // Clear form fields
    document.getElementById('route').value = '';
    document.getElementById('date').value = '';
    document.getElementById('time').value = '';
    document.getElementById('performance').value = '';
});


// JavaScript for dynamic table handling
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('collectionForm');
    const table = document.getElementById('collectionTable').getElementsByTagName('tbody')[0];
    const addButton = document.getElementById('addButton');

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        addCollection();
    });

    function addCollection() {
        const route = document.getElementById('route').value;
        const date = document.getElementById('date').value;
        const time = document.getElementById('time').value;
        const performance = document.getElementById('performance').value;

        if (route && date && time && performance) {
            const newRow = table.insertRow();
            newRow.innerHTML = `
                <td>${route}</td>
                <td>${date}</td>
                <td>${time}</td>
                <td>${performance}</td>
                <td><button class="editButton">Edit</button> <button class="deleteButton">Delete</button></td>
            `;
            clearForm();
        }
    }

    function clearForm() {
        document.getElementById('route').value = '';
        document.getElementById('date').value = '';
        document.getElementById('time').value = '';
        document.getElementById('performance').value = '';
    }

    table.addEventListener('click', function (e) {
        if (e.target.classList.contains('deleteButton')) {
            const row = e.target.parentElement.parentElement;
            table.removeChild(row);
        } else if (e.target.classList.contains('editButton')) {
            const row = e.target.parentElement.parentElement;
            const cells = row.getElementsByTagName('td');
            document.getElementById('route').value = cells[0].textContent;
            document.getElementById('date').value = cells[1].textContent;
            document.getElementById('time').value = cells[2].textContent;
            document.getElementById('performance').value = cells[3].textContent;

            // Optionally, you can remove the row after editing, or update it in place
            table.removeChild(row);
        }
    });
});
