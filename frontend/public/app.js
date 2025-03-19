document.addEventListener('DOMContentLoaded', () => {
  const messageDiv = document.getElementById('message');
  const fetchButton = document.getElementById('fetchButton');

  fetchButton.addEventListener('click', async () => {
    try {
      const response = await fetch('/api/hello');
      const data = await response.json();
      
      messageDiv.textContent = data.message;
      messageDiv.style.color = '#28a745';
    } catch (err) {
      messageDiv.textContent = 'Error fetching data';
      messageDiv.style.color = '#dc3545';
      console.error('Error:', err);
    }
  });
});