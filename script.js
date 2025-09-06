document.getElementById('transactionForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const amount = e.target.amount.value;
    const response = await fetch('/transaction', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({amount: parseFloat(amount)}),
    });
    const result = await response.json();
    alert(result.message || result.error);
  });
  