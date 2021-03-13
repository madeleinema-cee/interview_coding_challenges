let selection = []
let selectionLimit = 3

function populateDropdown() {
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
                weight: '500',
                color: '#2D426A, 100%',
                align: 'left'
            }
        }
    };
    let config = {responsive: true};
    Plotly.newPlot(plotElement, data, layout, config);
}

function toggleDisplay(ele) {
    let element = document.getElementById(ele);
    let computedDisplay = window.getComputedStyle(element).display;
    if (computedDisplay === 'none') {
        element.style.display = 'block';
    } else {
        element.style.display = 'none';
    }
}

function toggleActive(ele) {
    let element = document.getElementById(ele);
    element.classList.toggle("active");
}

function createDropdownClickListener() {
    document.addEventListener('click', DropdownClickListener);
}

function DropdownClickListener(event) {
    let dropdownContainer = document.getElementById("dropdown-container");
    let dropdown = document.getElementById("dropdown-content");

    if (!dropdownContainer.contains(event.target) && event.target !== dropdownContainer) {
        dropdown.style.display = 'none';
        parseSelectedCompanyData();
        document.removeEventListener('click', DropdownClickListener);
    }
}
