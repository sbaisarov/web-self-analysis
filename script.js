<script>
        const input = document.getElementById('myInput');

        input.addEventListener('focus', function() {
            this.placeholder = ''; // Clear placeholder on focus
        });

        input.addEventListener('blur', function() {
            if (this.value === '') {
                this.placeholder = 'Enter your text here...'; // Restore placeholder if input is empty
            }
        });
    </script>