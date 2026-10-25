function greet(name) {
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