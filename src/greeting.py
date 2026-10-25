function greet(name) {
    // Return a friendly greeting.
    if (!name) {
        name = "World";
    }
    return `Hello, ${name}!`;
}

function main() {
    console.log(greet("Migration Agent"));
}

if (require.main === module) {
    main();
}