// Search functionality for stocks
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchStock');
    const stockGrid = document.getElementById('stockGrid');

    if (searchInput && stockGrid) {
        searchInput.addEventListener('input', function(e) {
            const query = e.target.value.toLowerCase();
            const cards = stockGrid.querySelectorAll('.stock-card');

            cards.forEach(card => {
                const code = card.getAttribute('data-code').toLowerCase();
                const name = card.getAttribute('data-name').toLowerCase();

                if (code.includes(query) || name.includes(query)) {
                    card.style.display = '';
                    card.style.animation = 'fadeIn 0.3s ease';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    }

    // Auto-hide flash messages after 4 seconds
    const flashes = document.querySelectorAll('.flash');
    flashes.forEach(flash => {
        setTimeout(() => {
            flash.style.opacity = '0';
            flash.style.transform = 'translateX(100%)';
            setTimeout(() => flash.remove(), 400);
        }, 4000);
    });

    // Animate confidence bar on result page
    const confidenceFill = document.querySelector('.confidence-fill');
    if (confidenceFill) {
        const width = confidenceFill.style.width;
        confidenceFill.style.width = '0%';
        setTimeout(() => {
            confidenceFill.style.width = width;
        }, 300);
    }
});

// Add fadeIn animation
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
`;
document.head.appendChild(style);
