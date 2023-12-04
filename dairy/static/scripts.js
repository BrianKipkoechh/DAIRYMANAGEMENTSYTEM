// scripts.js

// Ensure jQuery is loaded before Bootstrap
if (typeof jQuery === 'undefined') {
    throw new Error('Bootstrap\'s JavaScript requires jQuery. Please include jQuery before Bootstrap\'s JavaScript.');
}

// Your custom scripts can go here

// Example: Activate Bootstrap tooltips
$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip();
});

// Example: Activate Bootstrap popovers
$(document).ready(function () {
    $('[data-toggle="popover"]').popover();
});
