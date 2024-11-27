const form = document.getElementById('loginForm');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const login = document.getElementById('login').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('/enter', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ login, password })
        });

        if (!response.ok) {
            const errorData = await response.json();
            resultDiv.innerText = `Ошибка: ${errorData.detail}`; // Отображение ошибки
        } else {
            // Если логин и пароль верные, перенаправляем на страницу успеха
            window.location.href = '/success';
        }
    } catch (error) {
        resultDiv.innerText = `Ошибка: ${error}`;
    }
});
