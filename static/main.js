let current = 1;
const currentId = document.querySelector('#current');
currentId.textContent = current;

const inputs = document.getElementsByTagName('input');
        
for (const input of inputs) {
    input.addEventListener('focus', function() {
        this.placeholder = ''; // Clear placeholder on focus
    });

    input.addEventListener('blur', function() {
        if (this.value === '') {
            if (this.name === 'situation') {
                this.placeholder = 'Опишите Ситуацию'; // Restore placeholder if input is empty
            }

            else if(this.name === 'thought') {
                this.placeholder = 'Мысль'
            }

            else if(this.name === 'correction') {
                this.placeholder = 'Коррекция'
            }

            else if(this.name === 'correctionThought') {
                this.placeholder = 'Выравнивающая мысль'
            }
        }
    });
}

const buttons = document.querySelectorAll('.dropbtn');
const feelingsButton = buttons[0];
const feelingsContent = document.querySelectorAll('.dropdown-content#feelingsContent')[0];
// Add a click event listener to the button
feelingsButton.addEventListener('click', function(event) {
    // Toggle the 'clicked' class on button click
    event.preventDefault();
    if (feelingsContent.style.display == 'none') feelingsContent.style.display = 'block';
    else feelingsContent.style.display = 'none';
});

const thElements = document.querySelectorAll('#feelingsContent th');
let dropContents = document.querySelectorAll('.dropdown-content.feelings');

thElements.forEach((th, index) => {
    th.addEventListener('click', function(event) {
        event.preventDefault();
        event.stopPropagation();
        dropContents[index].classList.toggle('active');
        dropContents.forEach((content, contentIndex) => {
            if (index !== contentIndex) {
                content.classList.remove('active');
            }
        });
    });
});

const flawsButton = buttons[1];
const flawsContent = document.querySelectorAll('.dropdown-content.flaws')[0];
// Add a click event listener to the button
flawsButton.addEventListener('click', function(event) {
    // Toggle the 'clicked' class on button click
    event.preventDefault();
    if (flawsContent.style.display == 'none') {
        flawsContent.style.display = 'block';
    }
    else flawsContent.style.display = 'none';
});

const fearsButton = buttons[2];
const fearsContent = document.querySelectorAll('.dropdown-content#fearsContent')[0];
// Add a click event listener to the button
fearsButton.addEventListener('click', function(event) {
    // Toggle the 'clicked' class on button click
    event.preventDefault();
    if (fearsContent.style.display == 'none') fearsContent.style.display = 'block';
    else fearsContent.style.display = 'none';
});

const thElementsFears = document.querySelectorAll('#fearsContent th');
let dropContentsFears = document.querySelectorAll('.dropdown-content.fears');

thElementsFears.forEach((th, index) => {
    th.addEventListener('click', function(event) {
        event.preventDefault();
        event.stopPropagation();
        dropContentsFears[index].classList.toggle('active');
        dropContentsFears.forEach((content, contentIndex) => {
            if (index !== contentIndex) {
                content.classList.remove('active');
            }
        });
    });
});

const denialsButton = buttons[3];
const denialsContent = document.querySelectorAll('.dropdown-content#denialsContent')[0];
// Add a click event listener to the button
denialsButton.addEventListener('click', function(event) {
    // Toggle the 'clicked' class on button click
    event.preventDefault();
    if (denialsContent.style.display == 'none') denialsContent.style.display = 'block';
    else denialsContent.style.display = 'none';
});

const needsButton = buttons[4];
const needsContent = document.querySelectorAll('.dropdown-content#needsContent')[0];
// Add a click event listener to the button
needsButton.addEventListener('click', function(event) {
    // Toggle the 'clicked' class on button click
    event.preventDefault();
    if (needsContent.style.display == 'none') needsContent.style.display = 'block';
    else needsContent.style.display = 'none';
});

const rolesButton = buttons[5];
const rolesContent = document.querySelectorAll('.dropdown-content#rolesContent')[0];
// Add a click event listener to the button
rolesButton.addEventListener('click', function(event) {
    // Toggle the 'clicked' class on button click
    event.preventDefault();
    if (rolesContent.style.display == 'none') rolesContent.style.display = 'block';
    else rolesContent.style.display = 'none';
});

const principlesButton = buttons[6];
const principlesContent = document.querySelectorAll('.dropdown-content#principleContent')[0];
// Add a click event listener to the button
principlesButton.addEventListener('click', function(event) {
    // Toggle the 'clicked' class on button click
    event.preventDefault();
    if (principlesContent.style.display == 'none') principlesContent.style.display = 'block';
    else principlesContent.style.display = 'none';
});

// Prevent closing when clicking inside the dropdowns
dropContents.forEach(dropdown => {
        dropdown.addEventListener('click', function(event) {
        event.stopPropagation();
    });
});

dropContentsFears.forEach(dropdown => {
        dropdown.addEventListener('click', function(event) {
        event.stopPropagation();
    });
});

// Prevent closing when clicking outside the dropdowns
const table = document.querySelectorAll('table')[0];
document.addEventListener('click', function(event) {
    dropContents.forEach(content => {
        if (!content.contains(event.target)) {
            content.classList.remove('active');
        }
    })

    if (!feelingsButton.contains(event.target)) {
        feelingsContent.style.display = 'none';
    }

    if (!flawsContent.contains(event.target) && !flawsButton.contains(event.target)) {
        flawsContent.style.display = 'none';
    }

    if (!denialsContent.contains(event.target) && !denialsButton.contains(event.target)) {
        denialsContent.style.display = 'none';
    }

    if (!fearsContent.contains(event.target) && !fearsButton.contains(event.target)) {
        fearsContent.style.display = 'none';
    }
    
    if (!needsContent.contains(event.target) && !needsButton.contains(event.target)) {
        needsContent.style.display = 'none';
    }

    if (!rolesContent.contains(event.target) && !rolesButton.contains(event.target)) {
        rolesContent.style.display = 'none';
    }
    
    if (!principlesContent.contains(event.target) && !principlesButton.contains(event.target)) {
        principlesContent.style.display = 'none';
    }
});

document.querySelector('form').addEventListener('submit', function(event) {
    current++;
    currentId.textContent = current;
    event.preventDefault();
    fetch('/process', {
        method: 'POST',
        body: new FormData(this)
    })
    .then(response => response.json())
    .then(data => {
        // Copy the result to the clipboard
        navigator.clipboard.writeText(data.result)
            .then(() => {
                alert('Скопировано!');
                window.location.href = '/';
            })
            .catch(error => console.log(error));
    })
    .catch (error => console.log(error))
    
    // get all the data from the form
    let formData = new FormData(event.target);
    let formObject = Object.fromEntries(formData.entries());
    
    // add form data to local storage
    setCookie('formData', JSON.stringify(formObject), new Date(new Date().getTime() + 365 * 24 * 60 * 60 * 1000));
    window.scrollTo(0, 0);
    clearContent();
})

function setCookie(cname, cvalue, expires) {
    let d = new Date();
    d.setTime(d.getTime() + 24 * 60 * 60 * 1000);
    expires = "expires" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

window.onload = function() {
    // retrieve form data from local storage
    let formData = JSON.parse(getCookie('formData'));
    let item;
    if (formData) {
        Object.keys(formData).forEach(key => {
            item = document.querySelector(`[name="${key}"]`)
            item.value = formData[key];
            if (item.type === "checkbox") {
                item.checked = true;
            }
        });
    }
    const checked = Array.from(document.querySelectorAll(`input[type="checkbox`)).filter(checkbox => checkbox.checked);
    checked.forEach(checkbox => {
        appendCheckboxValue(checkbox);
    });
};

function clearContent() {
    document.querySelectorAll('input[type="text"], input[type="checkbox"]').forEach(item => {
        if (item.type === 'text') {
            item.value = '';
        }
        if (item.type === "checkbox") {
            item.checked = false;
        }
    });

    document.querySelectorAll('.dropdown-content').forEach(content => {
        content.classList.remove('active');
    });

    setCookie('formData', '', new Date(0));

    const appended = document.querySelectorAll('div[data-target="appended"]');
    appended.forEach(div => {
        div.parentNode.removeChild(div);
    });
}


document.querySelectorAll('input[type=checkbox]').forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        if (checkbox.checked) {
            appendCheckboxValue(checkbox);
        }
        else {
            let className = checkbox.closest('.dropdown-content').classList[1];
            let label = document.querySelector(`label[data-target=${className}]`);
            let div = Array.from(label.querySelectorAll('div')).find(div => div.textContent === checkbox.value);
            if (div) {
                div.parentNode.removeChild(div);
            }
        }
    })
});

function appendCheckboxValue(checkbox) {
    let className = checkbox.closest('.dropdown-content').classList[1];
    let label = document.querySelector(`label[data-target=${className}]`);
    let div = document.createElement('div');
    let text = document.createTextNode(checkbox.value);

    div.appendChild(text);
    div.style = "margin-top: 5px; font-size: 12px; font-weight: bold";
    div.setAttribute("data-target", "appended");
    label.appendChild(div);
}
