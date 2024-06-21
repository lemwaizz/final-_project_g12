// Define an array to store recycling entries
let recyclingData = [];

// DOM elements
const form = document.getElementById('recyclingForm');
const tableBody = document.querySelector('#recyclingTable tbody');

// Event listener for form submission
form.addEventListener('submit', function(event) {
    event.preventDefault();

    // Capture form inputs
    const item = document.getElementById('item').value.trim();
    const weight = parseFloat(document.getElementById('weight').value);
    const date = new Date().toLocaleDateString(); // Capture current date

    // Validate inputs
    if (item && !isNaN(weight)) {
        // Add entry to data array
        recyclingData.push({ item, weight, date });

        // Clear form inputs
        document.getElementById('item').value = '';
        document.getElementById('weight').value = '';

        // Update table display
        renderTable();
    }
});

// Function to render the table
function renderTable() {
    // Clear existing table rows
    tableBody.innerHTML = '';

    // Render each entry in the data array
    recyclingData.forEach((entry, index) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${entry.item}</td>
            <td>${entry.weight}</td>
            <td>${entry.date}</td>
            <td>
                <button onclick="editEntry(${index})">Edit</button>
                <button onclick="deleteEntry(${index})">Delete</button>
            </td>
        `;
        tableBody.appendChild(row);
    });

    // Update environmental impact
    updateEnvironmentalImpact();
}

// Function to update environmental impact
function updateEnvironmentalImpact() {
    // Calculate total weight recycled and CO2 saved
    const totalWeight = recyclingData.reduce((acc, entry) => acc + entry.weight, 0);
    const co2Saved = totalWeight * 0.5; // Example CO2 saved calculation

    // Update DOM elements
    document.getElementById('totalWeight').textContent = totalWeight.toFixed(2);
    document.getElementById('co2Saved').textContent = co2Saved.toFixed(2);
}

// Function to edit an entry
function editEntry(index) {
    // Populate form with selected entry for editing
    const selectedEntry = recyclingData[index];
    document.getElementById('item').value = selectedEntry.item;
    document.getElementById('weight').value = selectedEntry.weight;

    // Remove selected entry from data array
    recyclingData.splice(index, 1);

    // Re-render table after editing
    renderTable();
}

// Function to delete an entry
function deleteEntry(index) {
    // Remove selected entry from data array
    recyclingData.splice(index, 1);

    // Re-render table after deletion
    renderTable();
}

// Initial rendering of the table
renderTable();
