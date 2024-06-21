document.getElementById('scheduleForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Collect form data
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const address = document.getElementById('address').value;
    const date = document.getElementById('date').value;
    const time = document.getElementById('time').value;

    // Display a notification
    const notification = document.getElementById('notification');
    notification.textContent = `Thank you, ${name}! Your waste collection is scheduled for ${date} at ${time}. You will receive a confirmation email at ${email}.`;

    // Here you would typically send the data to the server using fetch or AJAX
    // Example:
    // fetch('your-server-endpoint', {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify({ name, email, address, date, time })
    // }).then(response => response.json())
    // .then(data => {
    //     console.log('Success:', data);
    // }).catch((error) => {
    //     console.error('Error:', error);
    // });
});



