// Array to store contacts
let contacts = [];

// Function to add or edit a contact
function addOrEditContact() {
    const firstName = document.getElementById("first-name").value;
    const lastName = document.getElementById("last-name").value;
    const email = document.getElementById("email").value;
    const phone = document.getElementById("phone").value;
    const contactId = document.getElementById("edit-contact-id").value;

    // Check if we are editing an existing contact
    if (contactId) {
        const contact = contacts.find(c => c.id === parseInt(contactId));
        if (contact) {
            contact.firstName = firstName;
            contact.lastName = lastName;
            contact.email = email;
            contact.phone = phone;
        }
        document.getElementById("edit-contact-id").value = "";
    } else {
        // Create a new contact object
        const newContact = {
            id: contacts.length + 1,
            firstName,
            lastName,
            email,
            phone,
            creationDate: new Date(),
            isFavorite: false
        };
        contacts.push(newContact);
    }

    clearForm();
    displayContacts();
    return false; // Prevent form submission
}

// Function to display all contacts
function displayContacts() {
    const contactsList = document.getElementById("contacts-list");
    contactsList.innerHTML = ""; // Clear previous content

    contacts.forEach(contact => {
        const contactDiv = document.createElement("div");
        contactDiv.className = "contact";

        const contactDetails = `
            <strong>${contact.firstName} ${contact.lastName}</strong>
            <br>Email: ${contact.email}
            <br>Phone: ${contact.phone}
            <br>Created on: ${contact.creationDate.toLocaleDateString()}
            <br>
            <button onclick="editContact(${contact.id})">Edit</button>
            <button onclick="deleteContact(${contact.id})">Delete</button>
            <label>
                <input type="checkbox" onchange="toggleFavorite(${contact.id})" ${contact.isFavorite ? "checked" : ""}> Favorite
            </label>
        `;

        contactDiv.innerHTML = contactDetails;
        contactsList.appendChild(contactDiv);
    });

    // Update favorites list
    displayFavorites();
}

// Function to display favorite contacts
function displayFavorites() {
    const favoritesList = document.getElementById("favorites-list");
    favoritesList.innerHTML = ""; // Clear previous content

    contacts.filter(c => c.isFavorite).forEach(contact => {
        const contactDiv = document.createElement("div");
        contactDiv.className = "contact";

        const contactDetails = `
            <strong>${contact.firstName} ${contact.lastName}</strong>
            <br>Email: ${contact.email}
            <br>Phone: ${contact.phone}
            <br>Created on: ${contact.creationDate.toLocaleDateString()}
            <br>
        `;

        contactDiv.innerHTML = contactDetails;
        favoritesList.appendChild(contactDiv);
    });
}

// Function to edit a contact
function editContact(contactId) {
    const contact = contacts.find(c => c.id === contactId);
    if (contact) {
        document.getElementById("edit-contact-id").value = contact.id;
        document.getElementById("first-name").value = contact.firstName;
        document.getElementById("last-name").value = contact.lastName;
        document.getElementById("email").value = contact.email;
        document.getElementById("phone").value = contact.phone;
    }
}

// Function to delete a contact
function deleteContact(contactId) {
    contacts = contacts.filter(c => c.id !== contactId);
    displayContacts();
}

// Function to toggle favorite status
function toggleFavorite(contactId) {
    const contact = contacts.find(c => c.id === contactId);
    if (contact) {
        contact.isFavorite = !contact.isFavorite;
    }
    displayContacts();
}

// Function to clear the form after submission or editing
function clearForm() {
    document.getElementById("edit-contact-id").value = "";
    document.getElementById("first-name").value = "";
    document.getElementById("last-name").value = "";
    document.getElementById("email").value = "";
    document.getElementById("phone").value = "";
}
