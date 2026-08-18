document.addEventListener('DOMContentLoaded', () => {
    const copyButtons = document.querySelectorAll('.btn-copy');

    copyButtons.forEach(button => {
        button.addEventListener('click', () => {
            const promptId = button.getAttribute('data-target');
            const promptElement = document.getElementById(promptId);
            
            if (promptElement) {
                // Copy text to clipboard
                navigator.clipboard.writeText(promptElement.innerText).then(() => {
                    // Visual feedback
                    const originalText = button.innerText;
                    button.innerText = 'Copied!';
                    button.classList.add('copied');
                    
                    setTimeout(() => {
                        button.innerText = originalText;
                        button.classList.remove('copied');
                    }, 2000);
                }).catch(err => {
                    console.error('Failed to copy text: ', err);
                    button.innerText = 'Error';
                });
            }
        });
    });

    // Simple scrollspy to highlight active sidebar link
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.sidebar ul li a');

    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.3
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${id}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        observer.observe(section);
    });
});
