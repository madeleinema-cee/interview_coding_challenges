let selection = []
let selectionLimit = 3

function toggleDisplay(ele) {
    let element = document.getElementById(ele);
    if (element.style.display === 'none' || element.style.display === '') {
        element.style.display = 'block';
    } else {
        element.style.display = 'none'
    }
}

function toggleActive(ele) {
    let element = document.getElementById(ele)
    element.classList.toggle("active");
}

function handleDropdown(ele) {
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

function generatePlot(data) {
    let plotElement = document.getElementById('plot');
    let companyData = parseCompanyData(data);
    let layout = {
        title: {
            text: 'Headcount',
            font: {
                family: 'Roboto sans-serif',
                size: 24,
                weight: '500',
                color: '#2D426A, 100%'
            }
        }
    }
    Plotly.newPlot(plotElement, companyData, layout);
}

function parseCompanyData(data) {
    let months = data['months']
    let headcounts = data['headcounts']
    console.log(headcounts)
    let parsedData = [];
    for (const [key, value] of Object.entries(headcounts)) {
        d = {
            x: months,
            y: value['headcount'],
            name: key
        }
        parsedData.push(d)
    }
    return parsedData
}