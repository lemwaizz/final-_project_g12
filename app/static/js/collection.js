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
