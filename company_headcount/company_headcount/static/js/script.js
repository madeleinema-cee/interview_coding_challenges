let selection = []
let selectionLimit = 3

function populateDropdown() {
    /**
     * populate dropdown menu, add html elements
     */
    let companyMenu = document.getElementById('dropdown-content');
    let companies = Object.keys(companyData['headcounts']);

    for (let i = 0; i < companies.length; i++) {
        let company = document.createElement('div');
        company.id = companies[i];
        company.innerHTML = companies[i];
        company.onclick = function () {
            handleDropdownItemClick(company.id);
        }
        companyMenu.appendChild(company);
    }
}

function handleDropdownItemClick(ele) {
    /**
     * Select up to three companies for plotting
     */
    if (selection.includes(ele)) {
        selection.splice(selection.indexOf(ele), 1);
    } else {
        if (selection.length === selectionLimit) {
            let removedElement = selection.splice(0, 1);
            toggleActive(removedElement[0]);
        }
        selection.push(ele);
    }
    toggleActive(ele);
}

function parseSelectedCompanyData() {
    /**
     * Parse selected company for plotting
     */
    if (selection.length === 0) {
        let defaultCompany = Object.keys(companyData['headcounts'])[0];
        handleDropdownItemClick(defaultCompany);
        parseSelectedCompanyData();
    } else {
        let selectedCompanies = {};
        for (let i = 0; i < selection.length; i++) {
            selectedCompanies[selection[i]] = companyData['headcounts'][selection[i]];
        }
        let parsedData = [];
        for (const [key, value] of Object.entries(selectedCompanies)) {
            d = {
                x: companyData['months'],
                y: value['headcount'],
                name: key
            };
            parsedData.push(d);
        }
        generatePlot(parsedData);
    }
}

function generatePlot(data) {
    /**
     * Create the plot using Plotly JS
     * @param {HTMLElement}
     */
    let plotElement = document.getElementById('plot');
    let layout = {
        autosize: true,
        showlegend: true,
        legend: {"orientation": "h"},
        title: {
            text: '<b>Headcount</b>',
            font: {
                family: 'Roboto',
                size: 24,
                weight: 500,
                color: '#2D426A, 100%',
                align: 'left',
            },
            xref: 'paper',
            x: 0
        }
    };
    let config = {responsive: true};
    Plotly.newPlot(plotElement, data, layout, config);
}

function toggleDisplay(ele) {
    /**
     * Show or hide the content of dropdown menu
     * @param {HTMLElement}
     */
    let element = document.getElementById(ele);
    let icon = document.getElementById('icon');
    let computedDisplay = window.getComputedStyle(element).display;
    if (computedDisplay === 'none') {
        element.style.display = 'block';
    } else {
        element.style.display = 'none';
        parseSelectedCompanyData();
    }
}

function iconChange(ele) {
    /**
     * change the icon when clicked
     * @param {HTMLElement}
     */
    let element = document.getElementById(ele);
    let computedDisplay = window.getComputedStyle(element).display;
    if (computedDisplay === 'block') {
        icon.classList.replace('down', 'up');
    } else {
        icon.classList.replace('up', 'down');
    }
}

function toggleActive(ele) {
    /**
     * Mark the html element as active
     * @param {HTMLElement}
     */
    let element = document.getElementById(ele);
    element.classList.toggle("active");
}

function createDropdownClickListener() {
    /**
     * When clicked, create a dropdown menu click listener
     */
    document.addEventListener('click', DropdownClickListener);
}

function DropdownClickListener(event) {
    /** Close the dropdown menu when click outside of the dropdown menu and render plot
     * @param {HTMLElement}
     */
    let dropdownContainer = document.getElementById("dropdown-container");
    let dropdown = document.getElementById("dropdown-content");
    let icon = document.getElementById('icon');


    if (!dropdownContainer.contains(event.target) && event.target !== dropdownContainer) {
        dropdown.style.display = 'none';
        icon.classList.replace('up', 'down');
        parseSelectedCompanyData();
        document.removeEventListener('click', DropdownClickListener);
    }
}
