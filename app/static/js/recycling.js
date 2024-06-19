document.getElementById('recyclingForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Collect form data
    const item = document.getElementById('item').value;
    const weight = parseFloat(document.getElementById('weight').value);
    const date = new Date().toLocaleDateString();

    // Add new row to the table
    const table = document.getElementById('recyclingTable').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();
    newRow.insertCell(0).innerText = item;
    newRow.insertCell(1).innerText = weight.toFixed(2);
    newRow.insertCell(2).innerText = date;

    // Update total weight and CO2 saved
    const totalWeightElement = document.getElementById('totalWeight');
    const co2SavedElement = document.getElementById('co2Saved');

    let totalWeight = parseFloat(totalWeightElement.innerText);
    totalWeight += weight;
    totalWeightElement.innerText = totalWeight.toFixed(2);

    // Assuming 1 kg of recycled material saves 1.5 kg of CO2
    const co2Saved = totalWeight * 1.5;
    co2SavedElement.innerText = co2Saved.toFixed(2);

    // Clear form fields
    document.getElementById('item').value = '';
    document.getElementById('weight').value = '';
});
