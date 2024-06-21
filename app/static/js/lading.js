// JavaScript for letter-by-letter animation
document.addEventListener('DOMContentLoaded', function () {
    const animatedTexts = document.querySelectorAll('.animated-text');

    animatedTexts.forEach(text => {
        const letters = text.textContent.split('');
        text.textContent = '';

        letters.forEach((letter, idx) => {
            const letterSpan = document.createElement('span');
            letterSpan.textContent = letter;
            letterSpan.style.animationDelay = `${idx * 50}ms`;
            text.appendChild(letterSpan);
        });
    });
});
